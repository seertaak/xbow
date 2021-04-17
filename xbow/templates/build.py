from conans.client.conan_api import Conan as conan
from conans.model.ref import ConanFileReference

ref = ConanFileReference.loads("my-pkg/0.0.1@my-usr/release", validate=False)

conan.install_reference(ref, install_folder="tmp", generators=['deploy'])
conan.install()
