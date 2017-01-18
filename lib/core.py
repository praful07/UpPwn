from lib.flaws.extension import Extension
from lib.seleniumManager import SeleniumMng

class Core(object):

    def __init__(self, opts):
        #print opts
        self.target_url = opts.url
        self.verbosity = opts.verbosity
        self.seleniumMng = SeleniumMng(opts.on_success, self.target_url)


    def run(self):
        print "UpPwn is running.."
        print "Scan potential vulnerabilities with:"
        extension = Extension(self.seleniumMng)
        print "\t- " + extension.name + ":"
        extension.scan()



    def stop(self):
        print "UpPwn is stopping.."
