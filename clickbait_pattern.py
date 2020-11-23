#!/usr/bin/env python
# coding: utf-8

import json
import os

class clickbait_pattern:
    def __init__(self):
        assert os.path.exists("clickbait_keyword.json"), "clickbait_keyword.json 不在同層目錄"
        with open('clickbait_keyword.json') as json_file:
            self.clickbait_data = json.load(json_file)
    
    def __call__(self, str_):
        assert type(str_) == str, "input 要是 string"
        buf = [1 for i in self.clickbait_data if i in str_]    
        return( sum(buf) )
    