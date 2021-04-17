#pragma once

#include <exception>
#include <memory>
#include <optional>
#include <type_traits>

#include <boost/hof.hpp>
#include <boost/type_index.hpp>
#include <fmt/format.h>
#include <range/v3/all.hpp>

#include <xbow/arrow/meta.hpp>

namespace xb::arrow::actions {
using namespace ranges;
using ::arrow::MakeBuilder, ::arrow::NumericArray, ::arrow::NumericBuilder;
using boost::typeindex::type_id_with_cvr;

namespace details {
    template <range R>
    auto to_arrow_array_non_optional(R&& input) -> meta::array_obj<xb::meta::element_t<R>> {
        using T = xb::meta::element_t<R>;
        static_assert(!xb::meta::is_optional_v<T>);

        using AT = meta::arrow_type_of_t<T>;

        auto copy_input_to = [&](auto& output) {
            if constexpr (sized_range<R>) {
                output.Resize(size(input));
                for_each(input, [&](auto&& x) { output.UnsafeAppend(x); });
            } else if constexpr (contiguous_range<R>) {
                output.Resize(size(input));
                output.UnsafeAppend(data(input), size(input));
            } else {
                for_each(input, [&](auto&& x) { output.Append(x); });
            }
        };

        auto extract_arrow_array_obj = [](auto& builder) {
            auto result = builder.Finish();
            if (!result.ok()) {
                const auto status = result.status();
                throw std::runtime_error(fmt::format(
                    "Arrow error building array of type {}, error code {}, "
                    "message: \"{}\".",
                    type_id_with_cvr<T>().pretty_name(), int(status.code()), status.message()));
            }
            return std::static_pointer_cast<meta::arrow_array_t<T>>(result.ValueUnsafe());
        };

        if constexpr (xb::meta::number<T>) {
            auto output = NumericBuilder<AT>();
            copy_input_to(output);
            return extract_arrow_array_obj(output);
        } else if constexpr (same_as<T, bool>) {
            auto output = ::arrow::BooleanBuilder();
            copy_input_to(output);
            return extract_arrow_array_obj(output);
        } else if constexpr (same_as<T, std::string>) {
            auto output = ::arrow::StringBuilder();
            for (auto&& x : input) output.Append(x.data(), x.length());
            return extract_arrow_array_obj(output);
        }
    }

    template <range R>
    auto to_arrow_array_optional(R&& input) -> meta::array_obj<xb::meta::element_t<R>> {
        using T = xb::meta::element_t<R>;
        static_assert(xb::meta::is_optional_v<T>);
        using V = typename T::value_type;
        using AT = meta::arrow_type_of_t<T>;
        using AV = meta::arrow_type_of_t<V>;

        auto copy_input_to = [&](auto& output) {
            for_each(input, [&](auto&& x) {
                if (x)
                    output.Append(*x);
                else
                    output.AppendNull();
            });
        };

        auto extract_arrow_array_obj = [](auto& builder) {
            auto result = builder.Finish();
            if (!result.ok()) {
                const auto status = result.status();
                throw std::runtime_error(fmt::format(
                    "Arrow error building array of type {}, error code {}, "
                    "message: \"{}\".",
                    type_id_with_cvr<T>().pretty_name(), int(status.code()), status.message()));
            }
            return std::static_pointer_cast<meta::arrow_array_t<T>>(result.ValueUnsafe());
        };

        if constexpr (xb::meta::number<V>) {
            auto output = NumericBuilder<AV>();
            copy_input_to(output);
            return extract_arrow_array_obj(output);
        } else if constexpr (same_as<V, bool>) {
            auto output = ::arrow::BooleanBuilder();
            copy_input_to(output);
            return extract_arrow_array_obj(output);
        } else if constexpr (same_as<V, std::string>) {
            auto output = ::arrow::StringBuilder();
            for_each(input, [&](auto&& x) {
                if (x)
                    output.Append(*x);
                else
                    output.AppendNull();
            });
            return extract_arrow_array_obj(output);
        }
    }

    template <range R>
    auto to_arrow_array(R&& input) -> meta::array_obj<xb::meta::element_t<R>> {
        using T = xb::meta::element_t<R>;
        using AT = meta::arrow_type_of_t<T>;

        static_assert(not xb::meta::is_optional_v<float>);
        static_assert(xb::meta::is_optional_v<std::optional<float>>);

        if constexpr (xb::meta::is_optional_v<T>) {
            return to_arrow_array_optional(std::forward<R>(input));
        } else {
            return to_arrow_array_non_optional(std::forward<R>(input));
        }
    }

    template <ranges::range Range>
    auto to_table(Range&& rows) {
        namespace views = ranges::views;
        namespace actions = ranges::actions;
        namespace hana = boost::hana;
        using namespace hana::literals;
        using R = xb::meta::element_t<Range>;  // 'R' for record.
        static_assert(xb::meta::is_record_v<R>);

        const auto schema = xb::arrow::meta::schema_of<R>();

        // populate the data for each column
        std::vector<std::shared_ptr<::arrow::Array>> columns;
        hana::for_each(hana::accessors<R>(), [&](auto col_i) {
            columns.emplace_back(
                details::to_arrow_array(rows | views::transform(hana::second(col_i))));
        });

        return ::arrow::Table::Make(schema, columns);
    }
}  // namespace details

constexpr auto to_table = boost::hof::pipable(BOOST_HOF_LIFT(details::to_table));
constexpr auto to_arrow_array = boost::hof::pipable(BOOST_HOF_LIFT(details::to_arrow_array));
}  // namespace xb::arrow::actions
