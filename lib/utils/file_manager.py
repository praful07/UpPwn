# -*- coding: utf-8 -*-
import os, sys

class FileManager(object):
    tmp_dir = "/tmp/uppwn/"

    @classmethod
    def create_tmp_env(cls):
        sys.path.insert(0,"/tmp/uppwn/")
        if not os.path.exists(cls.tmp_dir):
            os.makedirs(cls.tmp_dir)
