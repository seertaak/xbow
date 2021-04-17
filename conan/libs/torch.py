from conans import ConanFile, tools, CMake
from conans.errors import ConanInvalidConfiguration
import os


class TorchConan(ConanFile):
    name = "torch"
    version="1.7.1"
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        tools.download("https://download.pytorch.org/libtorch/cpu/libtorch-cxx11-abi-shared-with-deps-1.7.1%2Bcpu.zip", "torch.zip")
        tools.unzip("torch.zip")

    def package(self):
        self.copy("libtorch/*")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self, folder="libtorch")

