#pragma once

#include <experimental/coroutine>

#include <memory>
#include <string_view>
#include <vector>

#include <arrow/api.h>
#include <arrow/memory_pool.h>
#include <arrow/stl.h>
#include <arrow/type_traits.h>
#include <boost/hana.hpp>
#include <range/v3/all.hpp>
#include <range/v3/experimental/utility/generator.hpp>

#include <xbow/meta.hpp>

namespace xb { namespace arrow { namespace views {
    using ranges::experimental::generator;
    namespace hana = boost::hana;
    // Define a range of all the unsigned shorts:
    template <ranges::unsigned_integral UI>
    auto bit_mask_view(UI data) -> generator<bool> {
        constexpr auto n = sizeof(data);

        for (int n = sizeof(data); --n >= 0;) {
            UI mask = 1;

            co_yield(mask & data);
            mask <<= 1;
            co_yield(mask & data);
            mask <<= 1;
            co_yield(mask & data);
            mask <<= 1;
            co_yield(mask & data);
            mask <<= 1;
            co_yield(mask & data);
            mask <<= 1;
            co_yield(mask & data);
            mask <<= 1;
            co_yield(mask & data);
            mask <<= 1;
            co_yield(mask & data);
            mask <<= 1;
        }
    }

    namespace details {
        struct string_array_view_t : ranges::view_facade<string_array_view_t> {
        private:
            friend ranges::range_access;
            using arrow_array_t = ::arrow::StringArray;
            using result_t = std::string_view;
            using offset_t = arrow_array_t::offset_type;

            std::shared_ptr<::arrow::StringArray> array;
            mutable ranges::semiregular_box<std::string_view> value;

            struct cursor {
            private:
                ptrdiff_t i;
                string_array_view_t* view;

            public:
                using difference_type = ptrdiff_t;
                using value_type = std::optional<std::string_view>;

                cursor() = default;
                explicit cursor(string_array_view_t* view, ptrdiff_t i) : view(view), i(i) {}

                result_t read() const {
                    const auto s = view->array->GetView(i);
                    return std::string_view(s.data(), s.length());
                }
                void prev() { i--; }
                void next() { i++; }
                bool equal(cursor const& that) const { return view == that.view && i == that.i; }
                void advance(difference_type n) { i += static_cast<int>(n); }
                auto distance_to(const cursor& that) const -> difference_type { return that.i - i; }
            };

        public:
            string_array_view_t() = default;
            explicit string_array_view_t(const std::shared_ptr<::arrow::StringArray>& array)
                : array(array) {}
            auto size() const { return array->length(); }

        private:
            cursor begin_cursor() { return cursor{this, 0}; }
            cursor end_cursor() { return cursor{this, size()}; }
        };

        struct optional_string_array_view_t : ranges::view_facade<optional_string_array_view_t> {
        private:
            friend ranges::range_access;
            using arrow_array_t = ::arrow::StringArray;
            using result_t = std::optional<std::string_view>;
            using offset_t = arrow_array_t::offset_type;

            std::shared_ptr<::arrow::StringArray> array;
            mutable ranges::semiregular_box<std::string_view> value;

            struct cursor {
            private:
                ptrdiff_t i;
                optional_string_array_view_t* view;

            public:
                using difference_type = ptrdiff_t;
                using value_type = std::optional<std::string_view>;

                cursor() = default;
                explicit cursor(optional_string_array_view_t* view, ptrdiff_t i)
                    : view(view), i(i) {}

                result_t read() const {
                    const uint8_t* bit_mask = view->array->null_bitmap_data();
                    bool is_valid = bit_mask[i / 8] & (~uint8_t(0) & (1 << (i % 8)));
                    if (!is_valid) return std::nullopt;
                    const auto s = view->array->GetView(i);
                    return std::string_view(s.data(), s.length());
                }
                void prev() { i--; }
                void next() { i++; }
                bool equal(cursor const& that) const { return view == that.view && i == that.i; }
                void advance(difference_type n) { i += static_cast<int>(n); }
                auto distance_to(const cursor& that) const -> difference_type { return that.i - i; }
            };

        public:
            optional_string_array_view_t() = default;
            explicit optional_string_array_view_t(
                const std::shared_ptr<::arrow::StringArray>& array)
                : array(array) {}
            auto size() const { return array->length(); }

        private:
            cursor begin_cursor() { return cursor{this, 0}; }
            cursor end_cursor() { return cursor{this, size()}; }
        };

        template <typename A>
        auto array_view(const std::shared_ptr<A>& array) -> decltype(auto) {
            if constexpr (std::is_same_v<A, ::arrow::StringArray>) {
                return string_array_view_t(array);
            } else {
                using T = typename A::value_type;
                // Get the pointer to the null bitmap.
                // const uint8_t* null_bitmap = array->null_bitmap_data();
                const auto* data = const_cast<T*>(reinterpret_cast<const T*>(array->raw_values()));
                return ranges::span(data, array->length());
            }
        }

        template <typename ConcreteArrowArrayObj>
        struct optional_array_view_t
            : ranges::view_facade<optional_array_view_t<ConcreteArrowArrayObj>> {
        private:
            friend ranges::range_access;
            using arrow_array_t = typename ConcreteArrowArrayObj::element_type;
            using T = typename arrow_array_t::value_type;
            using result_t = std::optional<T>;

            // Get the pointer to the null bitmap.
            // const uint8_t* null_bitmap = array->null_bitmap_data();
            const T* data;
            const uint8_t* bit_mask;
            const int size_;
            std::optional<T> value;

            struct cursor {
            private:
                int bit_ix;
                int byte_ix;
                optional_array_view_t* view;
                mutable uint8_t mask;

            public:
                using difference_type = ptrdiff_t;
                using value_type = std::optional<T>;

                cursor() = default;
                explicit cursor(optional_array_view_t* view)
                    : view(view), bit_ix(0), byte_ix(0), mask(read_mask(0)) {}
                explicit cursor(optional_array_view_t* view, int i)
                    : view(view),
                      bit_ix(bit_mask_bit_ix(i)),
                      byte_ix(bit_mask_byte_ix(i)),
                      mask(read_mask(i)) {}

                auto read_mask(int i) const { return view->bit_mask[i / 8]; }

                auto bit_mask_byte_ix(int i) const { return i / 8; }
                auto bit_mask_bit_ix(int i) const { return i % 8; }
                auto ix() const { return byte_ix * 8 + bit_ix; }

                void update_cursor() {
                    view->value = mask & (~uint8_t(0) & (1 << bit_ix))
                                      ? std::optional{view->data[ix()]}
                                      : std::nullopt;
                }

                const result_t& read() const { return view->value; }
                void prev() {
                    bit_ix--;
                    if (bit_ix < 0) {
                        bit_ix = 7;
                        byte_ix--;
                        mask = view->bit_mask[byte_ix];
                    }
                    update_cursor();
                }
                void next() {
                    bit_ix++;
                    if (bit_ix >= 8) {
                        bit_ix = 0;
                        byte_ix++;
                        mask = view->bit_mask[byte_ix];
                    }
                    update_cursor();
                }
                bool equal(cursor const& that) const {
                    return view == that.view && byte_ix == that.byte_ix && bit_ix == that.bit_ix;
                }
                void advance(difference_type n) {
                    auto i = ix() + static_cast<int>(n);
                    bit_ix = bit_mask_bit_ix(i);
                    byte_ix = bit_mask_byte_ix(i);
                    mask = read_mask(i);
                    update_cursor();
                }
                auto distance_to(const cursor& that) const -> difference_type {
                    return that.ix() - ix();
                }
            };

            cursor begin_cursor() { return cursor{this, 0}; }
            cursor end_cursor() { return cursor{this, size()}; }

            cursor begin_cursor() const { return cursor{this, 0}; }
            cursor end_cursor() const { return cursor{this, size()}; }

        public:
            optional_array_view_t() = default;
            explicit optional_array_view_t(const ConcreteArrowArrayObj& array)
                : data(const_cast<T*>(reinterpret_cast<const T*>(array->raw_values()))),
                  bit_mask(array->null_bitmap_data()),
                  size_(array->length()) {}
            const result_t& cached() { return *value; }
            auto size() const { return size_; }
        };

        template <typename ConcreteArrowArrayObj>
        auto optional_array_view(const ConcreteArrowArrayObj array) -> decltype(auto) {
            using arrow_array_t = typename ConcreteArrowArrayObj::element_type;
            if constexpr (std::is_same_v<arrow_array_t, ::arrow::StringArray>) {
                return optional_string_array_view_t(array);
            } else {
                return optional_array_view_t<ConcreteArrowArrayObj>(array);
            }
        }
    }  // namespace details

    constexpr auto array_view = boost::hof::pipable(BOOST_HOF_LIFT(details::array_view));
    constexpr auto optional_array_view =
        boost::hof::pipable(BOOST_HOF_LIFT(details::optional_array_view));

    auto null_bitmap_view(const ::arrow::Array& array, int i) -> bool {
        const uint8_t* null_bitmap = array.null_bitmap_data();

        const int byte_ix = i >> 8;
        const int bit_ix = i & 0xFF;

        const uint8_t data = null_bitmap[byte_ix];
        const uint8_t mask = 1 << bit_ix;

        return data & mask;
    }

    template <ranges::semiregular T>
    auto chunked_array_view(const ::arrow::ChunkedArray& chunks) -> generator<
        decltype(array_view(std::static_pointer_cast<meta::arrow_array_t<T>>(chunks.chunk(0))))> {
        using A = meta::arrow_array_t<T>;
        for (auto i : ranges::views::ints(0, chunks.num_chunks())) {
            const auto chunk = std::static_pointer_cast<A>(chunks.chunk(i));
            co_yield array_view(chunk);
        }
    }

    template <xb::meta::record R>
    auto to_range(const std::shared_ptr<::arrow::Table>& table) {
        namespace hana = boost::hana;
        using namespace hana::literals;

        namespace views = ranges::views;
        namespace actions = ranges::actions;

        return hana::unpack(hana::transform(hana::unpack(hana::make_range(
                                                             0_c, hana::size(hana::accessors<R>())),
                                                         hana::make_tuple),
                                            [&](auto i_c) {
                                                constexpr auto i = decltype(i_c)::value;
                                                using T = std::remove_cvref_t<decltype(hana::second(
                                                    hana::accessors<R>()[i_c])(R{}))>;
                                                return chunked_array_view<T>(*table->column(i));
                                            }),
                            views::zip) |
               views::transform([](auto&& chunk) {
                   return std::apply(views::zip, chunk) | views::transform([](auto&& row) {
                              auto convertible_tuple = std::apply(hana::make_tuple, row);
                              constexpr auto n = hana::size(convertible_tuple);
                              auto precise_tuple = hana::transform(
                                  hana::zip(hana::unpack(hana::make_range(0_c, hana::int_c<n>),
                                                         hana::make_tuple),
                                            convertible_tuple),
                                  [](auto i_x) {
                                      using T = std::remove_cvref_t<decltype(hana::second(
                                          hana::accessors<R>()[i_x[0_c]])(R{}))>;
                                      return T{i_x[1_c]};
                                  });

                              return hana::unpack(precise_tuple, [](const auto&... args) {
                                  hana::size(hana::make_tuple(args...));
                                  return R{args...};
                              });
                          });
               });
    }

}}}  // namespace xb::arrow::views