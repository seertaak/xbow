from conans import ConanFile, tools, CMake
from conans.errors import ConanInvalidConfiguration
import os


class XFrameConan(ConanFile):
    name = "xframe"
    version="0.3.0"
    description = "xframe"
    generators = "cmake", "cmake_find_package"
    settings = "os", "compiler", "build_type", "arch"
    scm = {
        "type": "git",
        "subfolder": "xframe",
        "url": "https://github.com/xtensor-stack/xframe.git",
        "revision": "master"
    }
    requires = (
        "xsimd/7.4.9",
        "xtensor/0.21.5",
        "xtl/0.6.21",
    )

    def get_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="xframe")
        return cmake

    def build(self):
        self.get_cmake().build()

    def package(self):
        self.get_cmake().install()

    def package_info(self):
        self.cpp_info.libs = ["xframe"]

