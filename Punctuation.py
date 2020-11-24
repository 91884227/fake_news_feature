#!/usr/bin/env python
# coding: utf-8

class Punctuation:
    def __call__(self, str_):
        assert type(str_) == str, "input 要是 string"
        buf_Exclamation = str_.count("!")
        buf_full_stop = str_.count("...")
        buf_question = str_.count("?")
        buf_wavy = str_.count("～")
        buf_Quotation = str_.count("「") + str_.count("『") + str_.count("【") + str_.count("［")
        buf_total = buf_Exclamation + buf_full_stop + buf_question + buf_wavy + buf_Quotation
        
        dic = {"#!": buf_Exclamation, 
               "#...": buf_full_stop, 
               "# ?": buf_question, 
               "# ~": buf_wavy, 
               "# 「": buf_Quotation,
               "# total": buf_total}
        return(dic)