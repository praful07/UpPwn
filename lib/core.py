from lib.flaws.contentType import ContentType

class Core(object):

    def __init__(self, opts):
        #print opts
        self.target_url = opts.url
        self.verbosity = opts.verbosity


    def run(self):
        print "UpPwn is running.."



    def stop(self):
        print "UpPwn is stopping.."
