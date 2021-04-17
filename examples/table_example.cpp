#include <chrono>
#include <tuple>
#include <vector>

#include <boost/algorithm/string.hpp>
#include <fmt/core.h>
#include <fmt/ostream.h>
#include <fmt/ranges.h>
#include <range/v3/all.hpp>
#include <range/v3/view/adaptor.hpp>
#include <spdlog/spdlog.h>

#include <xbow/arrow.hpp>
#include <xbow/date.hpp>

using namespace std::literals;
using std::string, std::vector, std::array;
using namespace ranges;
using namespace date::literals;
using fmt::print, fmt::format;
namespace pfr = boost::pfr;

// clang-format off
// Below: define a "record", which is just a value type which in addition wraps
// Boost.Hana's BOOST_HANA_DEFINE_STRUCT macro. This macro generates machinery
// which can be used to retrieve field names and types, as well as accessors that
// can read fields based on a compile-time integer (or string) representing the
// index (or name, respectively) of the field. Note that this dereferencing takes
// place in constant time. It's the same as accessing a struct member - it is *not*
// like accessing an item in a hash map (say). This reflective metadata is sufficient
// do the (ugly) Arrow C++ API raw lifting. For example, for the first field,
// an arrow Int32Builder will be used for writing data (what we call the *action*
// side, since the side-effect of an arrow being created is effected), and a
// Int32Array will be used for reading (the *views* side: here we take an regular
// arrow array or table, and wrap it with a range-v3 compatible range). For the
// "name" field, a arrow::StringBuilder and arrow::StringArray will be used, respectively.
// And so on.
def_record(suspect,
    (int32_t, id),
    (string, name),
    (double, salary)
);
// clang-format on

auto main(int argc, const char* argv[]) -> int {
    const auto t = xb::today();
    const auto inferred_schema = xb::arrow::meta::schema_of<suspect>();

    auto suspects = vector<suspect>{
        {1, "Keyser Söze"s, 1000.0}, {2, "Kobayashi"s, 500.0},   {3, "Fred Fenster"s, 500.0},
        {4, "Jack Baer"s, 100.0},    {5, "Dean Keaton"s, 800.0}, {6, "Michael McManus"s, 100.0},
    };

    print("input rows: {}\n", suspects);

    // below: traverse the rows, changing name to upper case, skipping every other element,
    // cycling over rows so that they repeat and taking exactly 20 of these rows, and finally
    // this range-v3 range is converted to a regular arrow table.
    // This code shows that we can take a bog-standard range-v3 pipeline and convert it to
    // an arrow object. This could later, for example, be written to a parquet file (WIP).
    const auto table = suspects | views::transform([](auto&& p) -> suspect& {
                           boost::to_upper(p.name);
                           return p;
                       }) |
                       views::stride(2) | views::cycle | views::take(20) |
                       xb::arrow::actions::to_table;

    if (table->Validate() != ::arrow::Status::OK())
        throw std::runtime_error(
            format("Unable to validate schema: {}", table->schema()->ToString()));

    // below: note that to_range<suspect>(table) returns a range consisting of chunks, each of which
    // is also a range. These chunks correspond exactly to the actual low-level chunks in the
    // arrow file. We view::join this range to produce a single, collated range, which we then
    // convert to a std::vector<suspect> for the sole reason of printing. Note how easily we
    // taped together the chunks! Normally this would be two-level for loop involving laborious
    // extraction of each field, type-casting, urgh!
    print("round-tripped rows: {}\n",
          xb::arrow::views::to_range<suspect>(table) | views::join | to<std::vector<suspect>>);

    print("inferred schema:\n{}\n", inferred_schema->ToString());
    print("round-tripped schema:\n{}\n\n", table->schema()->ToString());
    assert(*inferred_schema == *table->schema());

    return EXIT_SUCCESS;
}