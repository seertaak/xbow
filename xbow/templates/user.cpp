#include <cstdint>
#include <iostream>
#include <tuple>
#include <vector>

#include <arrow/api.h>
#include <arrow/memory_pool.h>
#include <arrow/stl.h>
#include <boost/hana.hpp>
#include <boost/pfr.hpp>
#include <boost/type_index.hpp>
#include <fmt/core.h>
#include <fmt/ranges.h>

#include <range/v3/all.hpp>
#include <spdlog/spdlog.h>

#include <boost/hof.hpp>
#include <cassert>

#include <xbow/arrow.hpp>
#include <boost/preprocessor/stringize.hpp>
#include <pybind11/pybind11.h>

using namespace std;
using namespace arrow;
using namespace ranges;
using spdlog::debug, spdlog::info, spdlog::warn, spdlog::error;

namespace pfr = boost::pfr;

struct data_row {
    int64_t id;
    double cost;
    vector<double> cost_components;
};
using data_row_tuple = decltype(pfr::structure_to_tuple(data_row{}));

BOOST_HOF_STATIC_LAMBDA_FUNCTION(to_tuple) = boost::hof::pipable([](auto&& x) {
    return pfr::structure_to_tuple(x);
});

BOOST_HOF_STATIC_LAMBDA_FUNCTION(to_str) = boost::hof::pipable([](auto&& row) -> string {
    return fmt::format("{}", row);
});

template <typename T>
auto cast = views::transform([](auto t) { return static_cast<T>(t); });

auto test() -> int {
    info("Welcome to spdlog, {}!!", "Martin");

    auto rows = vector<data_row>{
        {1, 1.0, {2.0, 3.0, 4.0}},
        {2, 1.0, {2.0, 3.0, 4.0}},
        {3, 1.0, {2.0, 3.0, 4.0}},
    };

    auto table = shared_ptr<Table>();
    auto names = vector<string>{"id", "cost", "cost_components"};

    info("rows:\n{}", rows | views::transform([](auto&& x) { return x | to_tuple | to_str; }) |
                          views::intersperse("\n"s) | actions::join);

    if (!stl::TableFromTupleRange(default_memory_pool(),
                                  rows | views::transform(to_tuple) | to<vector<data_row_tuple>>(),
                                  names, &table)
             .ok())
        throw runtime_error("Arrow exception.");

    auto ctx = compute::ExecContext();

    // The range needs to be pre-allocated to the respective amount of rows.
    // This allows us to pass in an arbitrary range object, not only
    // `std::vector`.
    auto test_rows = std::vector<data_row_tuple>(table->num_rows());
    if (!stl::TupleRangeFromTable(*table, {}, &ctx, &test_rows).ok())
        throw runtime_error("Arrow exception.");

    info("test rows:\n{}", test_rows | views::transform([](auto&& x) { return x | to_str; }) |
                               views::intersperse("\n"s) | actions::join);

    using namespace xb::arrow::actions;
    using namespace std::literals;
    //auto xs = views::ints(0, 100) | cast<int64_t> | to_arrow_array;
    auto xs = views::linear_distribute(0.0f, 1.0f, 41) | to_arrow_array;
    info("{}: {}", xs->ToString(),
         boost::typeindex::type_id<std::remove_cvref_t<decltype(*xs)>>().pretty_name());

    return EXIT_SUCCESS;
}

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(xbowpy, m) {
    m.doc() = "xbow";  // optional module docstring

    m.def("add", &add, "A function which adds two numbers");

#ifdef VERSION_INFO
    m.attr("__version__") = BOOST_PP_STRINGIZE(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}

