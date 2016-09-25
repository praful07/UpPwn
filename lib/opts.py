import argparse

class Opts(object):

    data_opts = {
        "url" : {
            "long_param" : "--url",
            "short_param" : "-u",
            "type" : str,
            "help" : "Targeted url.",
            "required" : True
        },
        "verbosity" : {
            "long_param" : "--verbosity",
            "short_param" : "-v",
            "help" : "Activate verbosity.",
            "action" : "store_true",
            "required" : False
        }
    }

    def __init__(self, argv):
        self.argv = argv
        self.parser = argparse.ArgumentParser(
            description='UpPwn')

    def initialize_options(self):
        for opt_name, content in self.data_opts.iteritems():
            self.add_option(opt_name, content)

    def add_option(self, opt_name, opt_content):
        if "type" in opt_content:
            self.parser.add_argument(opt_content["long_param"],
                        opt_content["short_param"],
                        type=opt_content["type"],
                        help=opt_content["help"],
                        required=opt_content["required"])
        elif "action" in opt_content:
            self.parser.add_argument(opt_content["long_param"],
                        opt_content["short_param"],
                        action=opt_content["action"],
                        help=opt_content["help"],
                        required=opt_content["required"])



    def parse(self):
        return self.parser.parse_args()
    #def usage(self):
