#!/usr/bin/env python
# coding: utf-8

import os
from collections import Counter
import json
import numpy as np

from ckip import ckip

class ckip_static(ckip):  
    def __init__(self):
        assert os.path.exists("pos_dictionary.json"), "pos_dictionary.json不在同目錄"
        assert os.path.exists("ner_dictionary.json"), "ner_dictionary.json不在同目錄"
        
        with open('pos_dictionary.json') as json_file:
            self.ori_pos_dict = json.load(json_file)
            
        with open('ner_dictionary.json') as json_file:
            self.ori_ner_dict = json.load(json_file)
            
        super().__init__()
    
    def __call__(self, str_):
        self.segmentation(str_)
        self.pos_stat()
        self.avg_pos_count_dict = self.dict_normalize(self.pos_count_dict)
        
        self.pos_adv_stat()
        self.avg_pos_adv_count_dict = self.dict_normalize(self.pos_adv_count_dict)
        
        self.ner_stat()
        self.avg_ner_count_dict = self.dict_normalize(self.ner_count_dict)
        
        buf = {}
        buf.update(self.pos_count_dict)
        buf.update(self.avg_pos_count_dict)
        buf.update(self.pos_adv_count_dict)
        buf.update(self.avg_pos_adv_count_dict)
        buf.update(self.ner_count_dict)
        buf.update(self.avg_ner_count_dict)
        return(buf)
        
    def dict_normalize(self, dict_):
        value = np.array(list(dict_.values()))
        keys = ["<0-1> %s" % i for i in list(dict_.keys())]
        if( sum(value) > 0):
            value = value/sum(value)
            return( dict(zip(keys, value)) )
        else:
            return( dict(zip(keys, value)) )
    
    def pos_stat(self):
        self.pos_count_dict = self.ori_pos_dict.copy()
        dict_pos_result = dict(Counter(self.pos_sentence_list[0]))
        self.pos_count_dict.update(dict_pos_result)
    
    def ner_stat(self):
        self.ner_count_dict = self.ori_ner_dict.copy()
        ner_list = [i[2] for i in list(self.entity_sentence_list[0])]
        dict_ner_result = dict(Counter(ner_list))
        self.ner_count_dict.update(dict_ner_result)         
    
    def pos_adv_stat(self):
        self.pos_adv_count_dict = { }
        self.pos_adv_count_dict["# adj"] = self.pos_count_dict["A"]
        self.pos_adv_count_dict["# conj"] = self.pos_count_dict["Caa"] + self.pos_count_dict["Cab"] + self.pos_count_dict["Cbb"] + self.pos_count_dict["Cba"]
        self.pos_adv_count_dict["# adv"] = self.pos_count_dict["D"] + self.pos_count_dict["Da"] + self.pos_count_dict["Dfa"] + self.pos_count_dict["Dfb"] + self.pos_count_dict["Dk"]
        self.pos_adv_count_dict["# Int"] = self.pos_count_dict["I"] 
        
        # count N
        N_list = ["Na", "Nb", "Nc", "Ncd", "Nd", "Nep", 
                  "Neqa","Neqb", "Nes", "Neu", "Nf", "Ng", "Nh", "Nv"]
        self.pos_adv_count_dict["# N"] = 0
        for i in N_list:
            self.pos_adv_count_dict["# N"] = self.pos_adv_count_dict["# N"] + self.pos_count_dict[i]
        
        # count prep
        self.pos_adv_count_dict["# prep"] = self.pos_count_dict["P"]
        
        # count V
        V_list = ["VA", "VAC", "VB", "VC", "VCL", "VD", "VF", 
                  "VE", "VG", "VH", "VHC", "VI", "VJ", "VK", "VL", "V_2"]
        
        self.pos_adv_count_dict["# V"] = 0
        for i in V_list:
            self.pos_adv_count_dict["# V"] = self.pos_adv_count_dict["# V"] + self.pos_count_dict[i]
            
        # count punc
        punc_list =  ["COLONCATEGORY", "COMMACATEGORY", "DASHCATEGORY", "DOTCATEGORY","ETCCATEGORY",
                      "EXCLAMATIONCATEGORY", "PARENTHESISCATEGORY","PAUSECATEGORY", "PERIODCATEGORY", 
                      "QUESTIONCATEGORY", "SEMICOLONCATEGORY","SPCHANGECATEGORY"]
        
        self.pos_adv_count_dict["# punc"] = 0
        for i in punc_list:
            self.pos_adv_count_dict["# punc"] = self.pos_adv_count_dict["# punc"] + self.pos_count_dict[i]
                    