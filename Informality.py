#!/usr/bin/env python
# coding: utf-8

import json
import os

class Swear_words:
    def __init__(self):
        assert os.path.exists("swear_words_chinese.json"), "swear_words_chinese.json 不在同目錄"
        with open('swear_words_chinese.json') as json_file:
            self.swear_words = json.load(json_file)
    
    def __call__(self, str_):
        assert type(str_) == str, "input 要是 string"
        buf = [1 for i in self.swear_words if i in str_]    
        return( {"swear_words":sum(buf)} )
    
class Netspeak:
    def __init__(self):
        assert os.path.exists("Netspeak_chinese.json"), "Netspeak_chinese.json 不在同目錄"
        with open('Netspeak_chinese.json') as json_file:
            self.netspeak = json.load(json_file)
    
    def __call__(self, str_):
        assert type(str_) == str, "input 要是 string"
        buf = [1 for i in self.netspeak if i in str_]    
        return( {"Netspeaks":sum(buf)} )   