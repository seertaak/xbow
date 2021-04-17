#include <chrono>
#include <cstdint>
#include <memory>
#include <tuple>
#include <type_traits>
#include <vector>

#include <boost/hana.hpp>
#include <date/date.h>
#include <fmt/core.h>
#include <fmt/ostream.h>
#include <fmt/ranges.h>
#include <range/v3/all.hpp>
#include <range/v3/view/adaptor.hpp>
#include <spdlog/spdlog.h>

#include <xbow/arrow.hpp>
#include <xbow/country.hpp>
#include <xbow/date.hpp>
#include <xbow/meta.hpp>

using namespace std::literals;
using std::string, std::vector, std::array;
using namespace ranges;
using namespace date::literals;
using spdlog::info;

constexpr auto fmt_error = [](auto&& msg, auto&&... p) {
    return std::runtime_error(fmt::format(std::forward(msg), std::forward(p)...));
};

// clang-format off
def_record(point,
    (double, x),
    (double, y)
);
// clang-format on

// clang-format off
def_record(person,
    (int64_t, id),
    (xb::date, dob),
    (string, name),
    (double, cost),
    (array<double, 3>, cost_components),
    (point, p)  // NB: arbitrarily-nested record types are supported for schema conversion.
                // However, while a-n types are supportable in principle (and probably not
                // to hard to implement using binary blobs) in the actual range wrappers,
                // we currently only support basic types like numbers and strings.
);
// clang-format on

using namespace xb::meta;

auto main(int argc, const char* argv[]) -> int {
    const auto t = xb::today();
    auto rows = vector<person>{
        {1, 1978_y / date::October / 26, "Martin"s, 1.0, {2.0, 3.0, 4.0}, {0.0, 1.0}},
        {2, t - date::days(100), "Foo"s, 1.0, {2.0, 3.0, 4.0}, {2.0, 3.0}},
    };
    info("rows: {}", rows);
    info("field names: {}", xb::meta::fields<person>);
    info("schema:\n{}", xb::arrow::meta::schema_of<person>()->ToString());
    info("schema:\n{}", xb::arrow::meta::schema_of<point>()->ToString());

    const auto ints = views::ints((uint8_t)0, unreachable) | views::take(256) | to<vector<uint8_t>>;
    info("rows: {}", rows);


    return EXIT_SUCCESS;
}
