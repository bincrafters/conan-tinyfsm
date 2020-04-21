import os
from conans import ConanFile, tools


class TinyfsmConan(ConanFile):
    name = "tinyfsm"
    license = "MIT"
    author = "Alexander Zaitsev zamazan4ik@tut.by"
    url = "https://github.com/ZaMaZaN4iK/conan-tinyfsm"
    homepage = "https://github.com/digint/tinyfsm"
    description = "A simple C++ finite state machine library"
    topics = ("state-machine", "cpp11")
    no_copy_sources = True

    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy("*hpp", dst="include", src=os.path.join(self._source_subfolder, "include"))
        self.copy("COPYING", dst="licenses", src=self._source_subfolder)
