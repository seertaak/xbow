# _xbow_ - range-v3 views and actions for Arrow C++

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

## Plans

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
   
   
   while request:
      team_id = request.next().team_id
      team_costs = (
            employees
                .filter(E.team_id == team_id)
                .accumulate(0, std.plus, E.salary)
      )
   ```

**Note**: first build must occur in `xbow` env on the command line. That way, the python version is found by `pybind11`
and set in _CMake_ cache. After that, refreshing the CMake tab and building work in clion.