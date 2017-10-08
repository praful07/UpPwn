# -*- coding: utf-8 -*-
from lib.utils import Xvfb, FileManager
from lib.scenario import Scenario
from lib.proxy import Proxy
import sys, time, logging

class Core(object):

    def __init__(self, parsed_opts):
        FileManager.create_tmp_env()
        self.opts = parsed_opts
        self.nb_vulnerabilities = 0

    def display_banner(self):
        banner = """
  _   _       ____
 | | | |_ __ |  _ \__      ___ __
 | | | | '_ \| |_) \ \ /\ / / '_ \\
 | |_| | |_) |  __/ \ V  V /| | | |
  \___/| .__/|_|     \_/\_/ |_| |_|
       |_|
        """
        print banner

    def run(self):
        self.display_banner()
        print "[+] UpPwn is running !"
        self.test_scenario()
        print "[+] Scenario successfully loaded"
        self.run_proxy()
        self.run_modules()
        print "[+] Work is done, {} vulnerabilities have been found !".format(self.nb_vulnerabilities)
        return True

    def test_scenario(self):
        Xvfb.start()
        self.up_s = Scenario(self.opts.scenario)
        self.up_s.build(self.opts.cookies)
        self.up_s.load()
        #if not self.up_s.has_succeeded(): return False

    def run_proxy(self):
        print "[+] Mitm proxy start"
        self.proxy = Proxy()
        self.proxy.start()

    def run_modules(self):
        print "[+] Upload vulnerabilities detection start"
        self.up_s.run()
        #time.sleep(120)

    def stop(self):
        print "[+] Close properly the proxy"
        time.sleep(15) # All tcp connection have to be ended before stopping the MiTM / Has to be fixed
        self.proxy.stop()
        Xvfb.stop()
        print "[+] UpPwn stopped !"
