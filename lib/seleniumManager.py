from selenium import webdriver

class SeleniumMng(object):

    def __init__(self, success_str, url):
        self.driver =  webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs',
                                            service_log_path='./logs/phantomjs.log')
        self.success_str = success_str
        self.url = url
        self.driver.get(self.url)
        #self.driver.set_window_size(1024, 768)

    def reload(self):
        self.driver.get(self.url)

    def uploadFile(self, file):
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(file)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()

        try:
            self.driver.find_element_by_xpath("//*[contains(text(),'" + self.success_str + "')]")
        except:
            return False
        return True

    def screenshot(self, name):
        self.driver.save_screenshot("./screenshots/" + name)
