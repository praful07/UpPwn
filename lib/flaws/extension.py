from lib.flaw import Flaw
from shutil import copyfile
import os

class Extension(Flaw):

    def __init__(self, seleniumMng):
        Flaw.__init__(self)
        self.name = "Extension"
        self.seleniumMng = seleniumMng

    def exploit(self):
        pass

    def scan(self):
        ext_php = "php"
        ext_img = ["png", "jpeg", "jpg"]

        for i, ext in enumerate(ext_img):
            path = self.test_dir + self.php_file + "." + ext_php + "." + ext
            copyfile(self.test_dir + self.php_file + ".php", path)
            print "\t\t" + path + " => " + str(self.seleniumMng.uploadFile(path))
            os.remove(path)
            self.seleniumMng.screenshot("screen-" + str(i) + ".png")
            self.seleniumMng.reload()


    def _edit_ext(self):
        pass
