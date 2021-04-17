#include <boost/preprocessor/stringize.hpp>
#include <pybind11/pybind11.h>

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(xbowpy, m) {
    m.doc() = "xbowpy";  // optional module docstring
    m.def("add", &add, "A function which adds two numbers");

#ifdef VERSION_INFO
    m.attr("__version__") = BOOST_PP_STRINGIZE(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
