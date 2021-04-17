conan install . -if build/debug --profile:host=conan/profile/tools --profile:build=conan/profile/debug --build missing
conan install . -if build/release --profile:host=conan/profile/tools --profile:build=conan/profile/release --build missing
