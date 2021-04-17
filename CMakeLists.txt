cmake_minimum_required(VERSION 3.17.0)

project(xbow VERSION 0.1
        DESCRIPTION "xbow: ranges for Arrow C++ API."
        LANGUAGES CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

enable_testing()

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CONAN_CMAKE_CXX_STANDARD 20)

set(sources
        include/xbow/arrow.hpp
        include/xbow/country.hpp
        include/xbow/date.hpp
        include/xbow/meta.hpp
        include/xbow/arrow/actions.hpp
        include/xbow/arrow/views.hpp
        include/xbow/arrow/meta.hpp
        src/xbowpy.cpp
        )

# "Base" includes/compiler defns, etc.
add_library(xbow STATIC ${sources})
conan_target_link_libraries(xbow)
target_compile_features(xbow PUBLIC cxx_std_20)
target_compile_options(xbow PUBLIC
        -Wno-logical-op-parentheses
        -Wno-ambiguous-reversed-operator
        -Wunused-command-line-argument
        -Wl,--export-dynamic
        -Wno-unused-result
        )
target_compile_definitions(xbow PUBLIC
        BOOST_HANA_CONFIG_ENABLE_STRING_UDL
        BOOST_STACKTRACE_LINK
        )
target_include_directories(xbow PUBLIC
        include
        /home/mpercossi/.pyenv/versions/3.9.2/include/python3.9
        /home/mpercossi/.pyenv/versions/3.9.2/envs/xbow/lib/python3.9/site-packages/pybind11/include
        )

# Python interop
pybind11_add_module(xbowpy ${sources})

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(xbowpy PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
target_link_libraries(xbowpy PRIVATE xbow)

add_executable(print_schema examples/print_schema.cpp)
target_link_libraries(print_schema PRIVATE xbow)

add_executable(table_example examples/table_example.cpp)
target_link_libraries(table_example PRIVATE xbow)

add_executable(test_xbow tests/test_xbow.cpp)
target_link_libraries(test_xbow PRIVATE xbow)

add_test(xbow bin/test-xbow)


