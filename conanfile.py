import sys
from conans import ConanFile, CMake


class XBowConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = (
        "boost/1.75.0",
        #"openssl/1.1.1j",
        "rapidjson/cci.20200410",
        "aws-c-common/0.4.25",
        "abseil/20200923.3",
        "lz4/1.9.3",
        "thrift/0.14.1",
        "utf8proc/2.6.0",
        "arrow/2.0.0",
        "magic_enum/0.7.2",
        "range-v3/0.11.0",
        "catch2/2.13.4",
        "date/3.0.0",
        "xtl/0.6.21",
        "nlohmann_json/3.9.1",
        "xsimd/7.4.9",
        "xtensor/0.21.5",
        "spdlog/1.8.5",
        "protobuf/3.15.5",
        "fmt/7.1.3",
        "pybind11/2.6.2"
    )
    # below, virtualrunenv allows `source build/activate_run.sh` in 
    # bash shell which in turn allows calling the build_requires tools
    # like cmake, ninja, and nasm.
    generators = "cmake", "virtualbuildenv", "virtualenv", "cmake_find_package"
    build_policy = "missing" 
    default_options = (
        "*:shared=False",
        "spdlog:header_only=True",
        "arrow:parquet=True",
        "arrow:with_csv=True",
        "arrow:with_protobuf=True",
        "arrow:with_snappy=True",

        # broken
        #"arrow:with_lz4=False",
        #"arrow:with_s3=False",
        #"arrow:with_utf8proc=False",

        # no recipe yet (according to conan!)
        #"arrow:with_grpc=True",
        #"arrow:with_flight_rpc=True",
        #"arrow:with_backtrace=True",
        #"arrow:with_cuda=True",
        #"arrow:with_llvm=True",
        #"arrow:with_orc=True",
    )

    @property
    def python_interpreter(self):
        if getattr(sys, "frozen", False):
            return "python"
        return sys.executable

    def build(self):
        cmake = CMake(self, generator='Ninja')
        cmake.definitions['PYTHON_EXECUTABLE'] = self.python_interpreter
        cmake.verbose = False
        print("{cmake.command_line=}")
        cmake.configure()
        cmake.build()
        cmake.test()

