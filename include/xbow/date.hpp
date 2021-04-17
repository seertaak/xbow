#pragma once

#include <chrono>

#include <date/date.h>

namespace xb {
    using date = ::date::sys_days;
    using year_month_day = ::date::year_month_day;

    inline auto today() -> date {
        return ::date::floor<::date::days>(std::chrono::system_clock::now());
    }
}  // namespace xb::date

template <>
struct fmt::formatter<xb::date> {
    constexpr auto parse(format_parse_context& ctx) { return ctx.end(); }

    // Formats the point p using the parsed format specification (presentation)
    // stored in this formatter.
    template <typename FormatContext>
    auto format(const xb::date& d, FormatContext& ctx) {
        // auto format(const point &p, FormatContext &ctx) -> decltype(ctx.out()) // c++11
        // ctx.out() is an output iterator to write to.
        const auto ymd = ::date::year_month_day(d);
        return format_to(ctx.out(), "{}-{:02}-{:02}", ymd.year(), uint32_t(ymd.month()),
                         uint32_t(ymd.day()));
    }
};

// Register date::sys_days as a valid C++ translation for Arrow's
// Date32 type.
template <>
struct arrow::CTypeTraits<xb::date> : public TypeTraits<Date32Type> {
    using ArrowType = Date32Type;
};
