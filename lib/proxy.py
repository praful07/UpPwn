import sys, os
import threading
from miproxy.proxy import AsyncMitmProxy, ProxyHandler


class Proxy(object):

    def __init__(self):
        self.proxy = AsyncMitmProxy(RequestHandlerClass=MitmProxyHandler,
                        server_address=('', 4198), ca_file="misc/ca.pem")

    def __run(self):
        try:
            original_stderr = sys.stderr
            sys.stderr = open(os.devnull, 'w')
            self.proxy.serve_forever()
            sys.stderr = original_stderr
        except:
            pass

    def start(self):
        self.thread = threading.Thread(target=self.__run)
        self.thread.start()

    def stop(self):
        self.proxy.server_close()
        #self.thread.join()

class MitmProxyHandler(ProxyHandler):

    def mitm_request(self, data):
        return data

    def mitm_response(self, data):
        #print '<< %s' % repr(data[:100])
        return data
