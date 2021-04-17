import conanfile
from plumbum import local

conan = local["conan"]["search", "--remote", "all"]

for r in conanfile.XBowConan.requires:
    lib = r.split("/")[0]
    if lib in "openssl boost rapidjson": continue
    out = list(conan(lib).splitlines())
    latest_version = out[-1].split("/")[1]
    print(f"\"{lib}/{latest_version}\",")

