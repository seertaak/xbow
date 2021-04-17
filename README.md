# _xbow_ - [range-v3](https://github.com/ericniebler/range-v3) views and actions for Arrow C++

## Why _xbow_?

Because I want to [specify arrow types](examples/print_schema.cpp) for the rows of an
[Arrow table](https://arrow.apache.org/docs/cpp/tables.html) like this:

```cpp
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
```

... instead of [like this](https://arrow.apache.org/docs/cpp/examples/row_columnar_conversion.html). And
I want to _use_ it like this:

```cpp
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
const auto table = suspects 
                     | views::transform([](auto&& p) -> suspect& {
                        boost::to_upper(p.name);
                        return p;
                       })
                     | views::stride(2)  
                     | views::cycle 
                     | views::take(20) 
                     | xb::arrow::actions::to_table;

// below: note that to_range<suspect>(table) returns a range consisting of chunks, each of which
// is also a range. These chunks correspond exactly to the actual low-level chunks in the
// arrow file. We view::join this range to produce a single, collated range, which we then
// convert to a std::vector<suspect> for the sole reason of printing. Note how easily we
// taped together the chunks! Normally this would be two-level for loop involving laborious
// extraction of each field, type-casting, urgh!
print("round-tripped rows: {}\n",
xb::arrow::views::to_range<suspect>(table) | views::join | to<vector<suspect>>);
```
...which should produce output like this:

```
input rows: {person[id: 1, name: Keyser Söze, salary: 1000], person[id: 2, name: Kobayashi, salary: 500], person[id: 3, name: Fred Fenster, salary: 500], person[id: 4, name: Jack Baer, salary: 100], person[id: 5, name: Dean Keaton, salary: 800], person[id: 6, name: Michael McManus, salary: 100]}
round-tripped rows: {person[id: 1, name: KEYSER SöZE, salary: 1000], person[id: 3, name: FRED FENSTER, salary: 500], person[id: 5, name: DEAN KEATON, salary: 800], person[id: 1, name: KEYSER SöZE, salary: 1000], person[id: 3, name: FRED FENSTER, salary: 500], person[id: 5, name: DEAN KEATON, salary: 800], person[id: 1, name: KEYSER SöZE, salary: 1000], person[id: 3, name: FRED FENSTER, salary: 500], person[id: 5, name: DEAN KEATON, salary: 800], person[id: 1, name: KEYSER SöZE, salary: 1000], person[id: 3, name: FRED FENSTER, salary: 500], person[id: 5, name: DEAN KEATON, salary: 800], person[id: 1, name: KEYSER SöZE, salary: 1000], person[id: 3, name: FRED FENSTER, salary: 500], person[id: 5, name: DEAN KEATON, salary: 800], person[id: 1, name: KEYSER SöZE, salary: 1000], person[id: 3, name: FRED FENSTER, salary: 500], person[id: 5, name: DEAN KEATON, salary: 800], person[id: 1, name: KEYSER SöZE, salary: 1000], person[id: 3, name: FRED FENSTER, salary: 500]}
```

([It does.](examples/table_example.cpp))

## Pre-requisites

- Python 3.9.1
- Clang 11 or higher (will probably all work with recent gcc)

**Note**: installing clang is not enough. You need to use `update-alternatives` on Ubuntu to make sure that `c++`
and `cc` call `clang++-11` and `clang-11`, respectively.

## Installation

1. Install [conan](https://conan.io/); this is used to download C++ libraries such as
   [boost](https://www.boost.org/) and [arrow](https://github.com/apache/arrow/tree/master/cpp):
    ```bash
    # install conan 
    pip install conan
    # install third-party libs in debug mode using conan...
    conan install . -if build/debug --profile:host=conan/profile/tools --profile:build=conan/profile/debug --build missing
    # ...same for release mode.
    conan install . -if build/release --profile:host=conan/profile/tools --profile:build=conan/profile/release --build missing
   
    conan export conan/libs/arrow.py xbow/stable
   
    # for CLion conan plugin.
    ln conan/profile/debug ~/.conan/profiles/debug
    ln conan/profile/release ~/.conan/profiles/release
    ```
2. Install C++ build tools ([CMake](https://cmake.org/), [Ninja](https://ninja-build.org/), and
   [nasm](https://www.nasm.us/)) and any libraries mentioned in this project's
   [conanfile.py](./conanfile.py).

## Development Environment

To make the build tools available in your shell (rather than just in the compile step):

```bash
source build/debug/activate.sh
```

For example:

```bash
# "BEFORE"
cmake
# =>
# Could not find command-not-found database. Run 'sudo apt update' to populate it.
# cmake: command not found

# now set up shell
source build/debug/activate.sh 

# "AFTER": -- cmake, nasm, ninja work.
cmake
# =>
# Usage
# 
#   cmake [options] <path-to-source>
#   cmake [options] <path-to-existing-build>
#   cmake [options] -S <path-to-source> -B <path-to-build>
# 
# Specify a source directory to (re-)generate a build system for it in the
# current working directory.  Specify an existing build directory to
# re-generate its build system.

Run 'cmake --help' for more information.
```

## Building

```bash
# build debug
conan build . -bf build/debug

# build release
conan build . -bf build/debug

# Alternative, using only cmake:

# build debug
source build/debug/activate.sh    # ... to be able to use cmake.
cd build/debug
cmake .

# build release
source build/release/activate.sh    # ... to be able to use cmake.
cd build/release
cmake .
```

## Usage

Usage examples can be found [in the tests](https://github.com/seertaak/xbow/blob/main/tests/test_xbow.cpp),
and [in the examples directory.](https://github.com/seertaak/xbow/tree/main/examples)

### Defining Custom Tables

Use the _def_record_ macro to define the types of rows of tables you want to 
manipulate in _xbow_. This leverages 
[Boost.Hana](https://www.boost.org/doc/libs/1_76_0/libs/hana/doc/html/index.html#tutorial-introspection-adapting)
to create static introspection machinery, which is used by _xbow_ to figure out the right concrete 
types for the Arrow array objects.

**Example**:

```cpp
def_record(point,
    (double, x),
    (double, y)
);

def_record(person,
    (int64_t, id),
    (xb::date, dob),
    (string, name),
    (double, cost),
    (array<double, 3>, cost_components),
    (point, p)  
);
```

**Notes**:

1. In principle, the record types can be nested as in the example above. This will work for the purpose
   of Arrow schema generation. Aggregates such as arrays and vectors are also supported. (Again, in principle
   you can use element type, with the caveat below.)
2. However, round-tripping (actual range use) currently doesn't support structures within structures. It's
   planned, and it's certainly possible using the reflective setup.
3. Currently only numeric and string types are supported, with partial support for boolean arrays (stored as
   bitmasks).
4. Partial support, with more planned, for dates and timestamp - these map from their Arrow concrete types to
   suitable modern C++ counterparts: hinnant's [date](https://github.com/HowardHinnant/date) and std's 
   [chrono](https://en.cppreference.com/w/cpp/chrono) libraries, respectively.

### Actions: Ranges To Arrow Objects

One use-case is that we already have a range or container with objects of our 
(appropriately defined - see above) row type, and our goal is to create the 
concomitant Arrow objects. This is accomplished using _xbows's_ 
[**actions**](https://g
Usage examples can be found [in the tests](https://github.com/seertaak/xbow/blob/main/tests/test_xbow.cpp),
and [in the examples directory.](https://github.com/seertaak/xbow/tree/main/examples).
ithub.com/seertaak/xbow/blob/main/include/xbow/arrow/actions.hpp), so 
called because they are side-effecting: they create new Arrow objects, which 
involves memory allocation.

```cpp
// convert a scalar range (i.e. a single column) into the appropriate Arrow array
// object.
template <range R>
auto to_arrow_array(R&& input) -> meta::array_obj<xb::meta::element_t<R>>;

// convert a range over an appropriately defined 
template <ranges::range Range>
auto to_table(Range&& rows);
```

### Views: Views on Arrow Ojects

In the other direction, we start with an Arrow array or table, and want to 
query or manipulate the data using range-v3 ranges. In this case, no allocation
is necessary, and so we adopt the 
[**view**](https://github.com/seertaak/xbow/blob/main/include/xbow/arrow/views.hpp) 
terminology. 

```cpp
// given a suitably defined record type (see above) convert an Arrow Table to a range 
// over items of the row type.
template <xb::meta::record R>
auto to_range(const std::shared_ptr<::arrow::Table>& table);

// convert a concrete Arrow array object to a view, no memory is allocated. (e.g.
// strings are represented as std::string_views whose pointer points to the Arrow
// memory itself, rather than creating copies. The range produced by this version 
// does not allow null elements. If you have missing elements, use 
// optional_array_view, below.
template <typename A>
auto array_view(const std::shared_ptr<A>& array) -> decltype(auto);

// Same as above, but allowing missing elements. Let's say you create A has element
// "StringType". Then optional_array_view will produce a range of 
// std::optional<std::string>. That is to say, nullity/non-nullity are represented
// using std::optional.
template <typename A>
auto optional_array_view(const std::sharedhttps://en.cppreference.com/w/cpp/chrono_ptr<A>& array) -> decltype(auto);

// Arrow tables are created out of so-called chunked arrays. They're usually pretty
// horrible to deal with. This helper function creates a range of ranges; the outer
// range obviously representing the chunks.
template <ranges::semiregular T>
auto chunked_array_view(const ::arrow::ChunkedArray& chunks) -> unspecified;

```

## Future Plans

Much tighter integration with Python. Use PEP484 and python's AST introspection to
generate the appropriate record class from a Python specification. Even more ambitious:
allow using Numba or Cython to generate UDFs that compiled inline with the aggregation
code to allow ultimate performance and flexibility.

1. A python file defines functions and types which are passed to functions and template types.
   ```python
   @data
   class employee:
       id: int
       team_id: int
       name: str
       dob: date
       salary: float
   
   employees = dataframe[person].read_parquet('/data/employees.parquet')
   E = employees.accessors
   
   
   while requesthttps://en.cppreference.com/w/cpp/chrono:
      team_id = request.next().team_id
      team_costs = (
            employees
                .filter(E.team_id == team_id)
                .accumulate(0, std.plus, E.salary)
      )
   ```

**Note**: first build must occur in `xbow` env on the command line. That way, the python version is found by `pybind11`
and set in _CMake_ cache. After that, refreshing the CMake tab and building work in clion.