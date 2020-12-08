import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


class GP2_crawler:
    def __init__(self, timesleep = 5):
        assert os.path.exists('./geckodriver'), "geckodriver不在同目錄"
#         options = Options()
#         options.add_argument("--disable-notifications")
        opts = Options()
        opts.set_headless(headless=True)
        self.browser = webdriver.Firefox(options = opts, executable_path="./geckodriver")
        self.URL = "http://server-a1.ddns.net:5153/"
        # self.browser.get(self.URL)
        self.timesleep = timesleep 
    
    def __del__(self):
        self.browser.close()
        self.browser.quit()
    
    def __call__(self, str_, length_ = 600):
        self.browser.get(self.URL)
        
        # send seed
        seed = self.browser.find_element_by_id("seed")
        seed.send_keys(Keys.CONTROL, 'a')
        seed.send_keys(Keys.BACKSPACE)
        seed.send_keys(str_)    
        
        # send sample
        nsamples = self.browser.find_element_by_id("nsamples")
        nsamples.send_keys(Keys.LEFT)
        
        # send length
        length = self.browser.find_element_by_id("length")
        length.send_keys(Keys.CONTROL, 'a')
        length.send_keys(Keys.BACKSPACE)
        length.send_keys(length_)   
        
        # send Enter
        submit = self.browser.find_element_by_id("submit")
        submit.send_keys(Keys.ENTER)
        
        time.sleep(self.timesleep)
        # get text
        while( True):
            try: 
                self.browser.find_element_by_id("spinner")
                time.sleep(self.timesleep)
            except:
                break 
                
        buf = self.browser.find_element_by_id("currentSampleText").text
        
        # browser_back
        # self.browser.back()
        
        return(buf)    

def strB2Q(s):
    """把字串半形轉全形"""
    rstring = ""
    for uchar in s:
        u_code = ord(uchar)
        if u_code == 32:  # 全形空格直接轉換
            u_code = 12288
        elif 33 <= u_code <= 126:  # 全形字元（除空格）根據關係轉化
            u_code += 65248
        rstring += chr(u_code)
    return rstring

# test = GP2_crawler()
# test( strB2Q("義偉貞她媽率!!!\n"), 500)