# -*- coding: utf-8 -*-
import unittest, fileinput, sys, os
from lib.utils import FileManager
from shutil import copyfile
from importlib import import_module

class Scenario(object):
    def __init__(self, path):
        self.up_scenario = "/tmp/uppwn/tmp_scenario.py"
        copyfile(path, self.up_scenario)
        self.success = True

    def build(self, cookies):
        for line in fileinput.input(self.up_scenario, inplace=1):
            if line.startswith("if __name__ =="):
                print "def start():"
            elif line.startswith(" " * 8 + "self.driver.implicitly_wait(30)"):
                pass
            elif line.startswith(" " * 8 + "self.driver = webdriver.Firefox()"):
                print " " * 8 + """fp = webdriver.FirefoxProfile("%s")""" % ("./misc/firefox_profile.up")
                print " " * 8 + """self.driver = webdriver.Firefox(fp, log_path="/dev/null")"""
            elif line.startswith(" " * 8 + "driver = self.driver"):
                print line,
                print " " * 8 + "if self.base_url[-1] == '/': self.base_url = self.base_url[:-1]"
                print " " * 8 + "driver.get(self.base_url)"
                if cookies is None: continue
                for key, value in cookies.items():
                    cookie = """driver.add_cookie({"name" : "%s", "value" : "%s"})""" % (key, value)
                    print " " * 8 + cookie
            else:
                print line,


    def load(self):
        self.mod = import_module('tmp_scenario')
        self.up_test = unittest.TestLoader().loadTestsFromModule(self.mod)

    def run(self):
        null = open(os.devnull, "w")
        unittest.TextTestRunner(stream=null).run(self.up_test)

    def has_succeeded(self):
        return self.success


#if __name__ == '__main__':
#    cookies = {"spip_session":"5240_e298e98ef6d73ac6c7a564e68247cdb7"}
#    up_s = Scenario("../tests_files/scenario_rootme.py")
#    up_s.build(cookies)
#    up_s.load()
#    up_s.run()
