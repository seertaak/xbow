#pragma once

#include <cstdint>
#include <iostream>
#include <memory>
#include <optional>
#include <sstream>
#include <tuple>
#include <type_traits>
#include <vector>

#include <arrow/api.h>
#include <arrow/memory_pool.h>
#include <arrow/stl.h>
#include <arrow/type_traits.h>
#include <boost/hana.hpp>
#include <boost/hof.hpp>
#include <boost/pfr.hpp>
#include <boost/preprocessor.hpp>
#include <boost/type_index.hpp>
#include <fmt/core.h>
#include <range/v3/all.hpp>
#include <range/v3/utility/semiregular_box.hpp>
#include <range/v3/view/adaptor.hpp>

#define def_record(record_name, ...)                          \
    struct record_name {                                      \
        BOOST_HANA_DEFINE_STRUCT(record_name, ##__VA_ARGS__); \
        struct view;                                          \
    };                                                        \
    struct record_name::view {};

namespace xb { namespace meta {
    using std::vector, std::string, std::string_view, std::array, std::tuple, std::stringstream,
        std::shared_ptr;
    namespace pfr = boost::pfr;
    namespace hana = boost::hana;
    using namespace hana::literals;

    template <ranges::range Rng>
    using data_t = decltype(ranges::data(std::declval<Rng&>()));

    template <ranges::range Rng>
    using element_t = std::remove_cvref_t<decltype(*ranges::begin(std::declval<Rng&>()))>;

    BOOST_HOF_STATIC_LAMBDA_FUNCTION(to_tuple) = boost::hof::pipable([](auto&& x) {
        return pfr::structure_to_tuple(x);
    });

    BOOST_HOF_STATIC_LAMBDA_FUNCTION(to_str) = boost::hof::pipable([](auto&& row) -> string {
        return fmt::format("{}", row);
    });

    template <typename T>
    using to_tuple_t = decltype(pfr::structure_to_tuple(T{}));

    template <typename T>
    constexpr auto is_record_v = hana::Struct<T>::value;

    template <typename T>
    concept record = is_record_v<T>;

    template <record T>
    constexpr auto fields = [] {
        constexpr auto fields = hana::accessors<T>();
        constexpr auto n_fields = hana::size(fields);
        std::array<std::string_view, n_fields> result;
        hana::for_each(hana::make_range(0_c, hana::int_c<n_fields>), [&](auto i) {
            constexpr int ix = decltype(i)::value;
            constexpr const char* name = hana::first(fields[i]).c_str();
            result[ix] = std::string_view{name};
        });
        return result;
    }();

    template <typename>
    constexpr auto is_string_v = false;

    template <>
    constexpr auto is_string_v<string> = true;

    template <typename>
    constexpr auto is_array_v = false;

    template <typename T, int N>
    constexpr auto is_array_v<array<T, N>> = true;

    namespace details {
        template <typename>
        struct is_optional {
            constexpr static const auto value = false;
        };
        template <typename /*destructible*/ T>
        struct is_optional<std::optional<T>> {
            constexpr static const auto value = true;
        };
    }  // namespace details

    template <typename T>
    constexpr auto is_optional_v = details::is_optional<T>::value;

    template <typename T>
    concept optional = is_optional_v<T>;

    template <typename T>
    concept floating_point = std::is_floating_point_v<T>;

    template <typename T>
    concept number = floating_point<T> || ranges::integral<T>;
}}  // namespace xb::meta

template <xb::meta::record R>
auto operator<<(std::ostream& os, const R& r) -> std::ostream& {
    namespace meta = xb::meta;
    namespace hana = boost::hana;
    using namespace hana::literals;

    os << boost::typeindex::type_id<R>() << '[';

    const auto members = hana::members(r);
    constexpr int n = hana::size(hana::accessors<R>());

    if constexpr (n > 0) {
        os << meta::fields<R>[0] << ": " << meta::to_str(members[0_c]);
    }
    if constexpr (n > 1) {
        hana::for_each(hana::make_range(1_c, hana::int_c<n>), [&](auto i) {
            os << ", " << meta::fields<R>[decltype(i)::value] << ": "
               << xb::meta::to_str(members[i]);
        });
    }

    os << ']';

    return os;
}
