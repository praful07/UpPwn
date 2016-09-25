from lib.opts import Opts
from lib.core import Core
import sys

def UpPwn(argv):
    opts = Opts(argv)
    opts.initialize_options()
    parsed_opts = opts.parse()

    core = Core(parsed_opts)
    core.run()
    core.stop()

if __name__ == '__main__':
    UpPwn(sys.argv[1:])
