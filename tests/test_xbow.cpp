#define CATCH_CONFIG_MAIN

#include <boost/hana.hpp>
#include <boost/hof/placeholders.hpp>
#include <catch2/catch.hpp>
#include <fmt/format.h>
#include <optional>
#include <range/v3/all.hpp>
#include <string>

#include <xbow/arrow.hpp>

using std::vector;
using namespace arrow;
using namespace ranges;
using namespace xb::arrow::actions;
using namespace xb::arrow::views;
using xb::arrow::meta::array_obj;
using namespace boost::hof::placeholders;

template <typename T>
constexpr auto cast = views::transform([](auto&& x) { return static_cast<T>(x); });
constexpr auto square = views::transform(_1 * _1);
constexpr auto do_test = [](range auto&& rng_) {
    // below, 't' is a type constant which represents the actual value (element) type we are testing
    // the arrow "wrapper" functionality for....
    return [&](auto t) {
        // ... and below, we see the admittedly convoluted compile-time expression which yields the
        // element type given the type constant:
        using T = typename decltype(t)::type;
        // ... eat your heart out, rust -- maybe in two years?

        // This tests consists of:
        // A: the range 'rng' written to a vector<T>.
        // B: the same range written first to an arrow array object, then this array object is
        // converted back to a range, and finally this range is written to another vector<T>.
        // Finally, we simply assert that A == B.

        // below, force each element to be the type we are testing; I couldn't create elements with
        // the right types using views::ints (e.g. with int64_t compiler complains about difference
        // type exceeding 64-bits. Probably not using upper bound would fix it, but fuck it, we're
        // going with casts.)
        const auto rng = rng_ | cast<T>;

        const std::vector<T> A = rng | to<vector<T>>;  // range -> vector

        // below, array_obj<int> is identically std::shared_ptr<NumericArray<Int32Type>>; it
        // represents what the raw arrow library "outputs".
        const array_obj<T> arr = rng | to_arrow_array;  // range -> arrow array object
        const std::vector<T> B =
            arr | array_view | to<vector<T>>;  // arrow array object -> -v3 range -> vector.

        REQUIRE(A == B);
    };
};

TEST_CASE("DUMB", "[arrow]") {
    REQUIRE(true == true);
}

TEST_CASE("Integral arrays", "[arrow]") {
    hana::for_each(hana::tuple_t<int32_t, int64_t>, do_test(views::ints(0, 15) | square));
}

TEST_CASE("Optional integral arrays", "[arrow]") {
    const std::vector<std::optional<int>> A{std::optional{1}, std::nullopt, std::optional{2},
                                            std::optional{3}};

    // below, array_obj<int> is identically std::shared_ptr<NumericArray<Int32Type>>; it
    // represents what the raw arrow library "outputs".
    const array_obj<std::optional<int>> arr =
        views::all(A) | to_arrow_array;  // range -> arrow array object
    const std::vector<std::optional<int>> B =
        arr | optional_array_view |
        to<vector<std::optional<int>>>;  // arrow array object -> -v3 range -> vector.

    REQUIRE(A == B);
}

TEST_CASE("Floating point arrays", "[arrow]") {
    hana::for_each(hana::tuple_t<float, double>,
                   do_test(views::linear_distribute(0.0, 1.0, 11) | square));
}

TEST_CASE("String arrays", "[arrow]") {
    using namespace std;
    // clang-format off
    const std::vector A {
        "hello"s,
        "goodbye"s,
        "foo"s,
        "bar"s
    };
    // clang-format on

    // below, array_obj<int> is identically std::shared_ptr<NumericArray<Int32Type>>; it
    // represents what the raw arrow library "outputs".
    const array_obj<std::string> arr =
        views::all(A) | to_arrow_array;  // range -> arrow array object

    const std::vector<std::string> B =
        arr | array_view | to<vector<string>>;  // arrow array object -> v3 range -> vector.

    REQUIRE(A == B);
}

TEST_CASE("Optional string arrays", "[arrow]") {
    using namespace std;
    // clang-format off
    const std::vector<std::optional<string>> A {
        "hello"s,
        "goodbye"s,
        std::nullopt,
        "foo"s,
        std::nullopt,
        "bar"s
    };
    // clang-format on

    // below, array_obj<int> is identically std::shared_ptr<NumericArray<Int32Type>>; it
    // represents what the raw arrow library "outputs".
    const array_obj<std::string> arr =
        views::all(A) | to_arrow_array;  // range -> arrow array object

    const std::vector<std::optional<std::string>> B =
        arr | optional_array_view |         // arrow array object -> -v3 range
        to<vector<std::optional<string>>>;  // v3 range -> vector.

    REQUIRE(A == B);
}
