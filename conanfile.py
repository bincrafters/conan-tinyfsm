#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools


class TinyfsmConan(ConanFile):
    name = "tinyfsm"
    version = "0.3.2"
    license = "MIT"
    author = "Alexander Zaitsev zamazan4ik@tut.by"
    url = "https://github.com/ZaMaZaN4iK/conan-tinyfsm"
    homepage = "https://github.com/digint/tinyfsm"
    description = "A simple C++ finite state machine library"
    topics = ("state-machine", "cpp11")
    no_copy_sources = True

    _source_subfolder = "source_subfolder"

    def source(self):
        checksum = "8d1b8c2451add006f99fdcff07197bfc2e8972868d315243be06cfd0b1e879f5"
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version), sha256=checksum)      
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy("*hpp", dst="include", src=os.path.join(self._source_subfolder, "include"))
        self.copy("COPYING", dst="licenses", src=self._source_subfolder)

    def package_info(self):
        self.info.header_only()
