#pragma once

#include <optional>
#include <memory>
#include <vector>

#include <arrow/api.h>
#include <arrow/memory_pool.h>
#include <arrow/stl.h>
#include <arrow/type_traits.h>
#include <boost/hana.hpp>
#include <range/v3/all.hpp>
#include <range/v3/experimental/utility/generator.hpp>

#include <xbow/meta.hpp>

namespace xb { namespace arrow { namespace meta {
    namespace hana = boost::hana;

    template <ranges::semiregular T>
    using arrow_type_of_t = typename ::arrow::CTypeTraits<T>::ArrowType;

    template <ranges::semiregular T>
    using arrow_array_t = typename ::arrow::TypeTraits<arrow_type_of_t<T>>::ArrayType;

    template <ranges::semiregular T>
    using array_obj = std::shared_ptr<meta::arrow_array_t<T>>;

    template <typename T>
    auto arrow_type_of() -> std::shared_ptr<::arrow::DataType> {
        if constexpr (xb::meta::is_array_v<T>) {
            constexpr auto n = std::size(T{});
            return fixed_size_list(arrow_type_of<xb::meta::element_t<T>>(), n);
        } else if constexpr (ranges::random_access_range<T> && !xb::meta::is_string_v<T>) {
            // above: strings are random access ranges, but arrow has a specific type for them, so
            // the fallback else-clause is sufficient.
            return list(arrow_type_of<xb::meta::element_t<T>>());
        } else if constexpr (xb::meta::is_record_v<T>) {
            auto fields = std::vector<std::shared_ptr<::arrow::Field>>();
            hana::for_each(hana::accessors<T>(), [&](auto f) {
                using T_f = std::remove_cvref_t<decltype(hana::second(f)(T{}))>;
                const auto name = hana::first(f).c_str();
                fields.push_back(::arrow::field(name, arrow_type_of<T_f>()));
            });
            return struct_(fields);
        } else {
            return ::arrow::TypeTraits<arrow_type_of_t<T>>::type_singleton();
        }
    }

    template <typename T>
    auto schema_of() {
        auto fields = std::vector<std::shared_ptr<::arrow::Field>>();
        hana::for_each(hana::accessors<T>(), [&](auto f) {
            using T_f = std::remove_cvref_t<decltype(hana::second(f)(T{}))>;
            const auto name = hana::first(f).c_str();
            fields.push_back(::arrow::field(name, arrow_type_of<T_f>()));
        });
        return std::make_shared<::arrow::Schema>(fields);
    }
}}}  // namespace xb::arrow::meta

// Register date::sys_days as a valid C++ translation for Arrow's
// Date32 type.
template <typename T>
struct arrow::CTypeTraits<std::optional<T>> : public TypeTraits<xb::arrow::meta::arrow_type_of_t<T>> {
    using ArrowType = xb::arrow::meta::arrow_type_of_t<T>;
};
