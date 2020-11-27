#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tensorflow as tf
from ckiptagger import data_utils, construct_dictionary, WS, POS, NER
from IPython.display import clear_output
clear_output()
import os


# In[29]:


class ckip:
    def __init__(self):
        print("prepare ws pos ner")
        assert os.path.exists("./ckiptagger_data"), "ckiptagger_data 不在同層目錄"
        self.ws = WS("./ckiptagger_data")
        self.pos = POS("./ckiptagger_data")
        self.ner = NER("./ckiptagger_data")
        clear_output() 
        
    def segmentation(self, str_):
        assert type(str_) == str, "input 要是 string"
        self.word_sentence_list = self.ws([str_])
        self.pos_sentence_list = self.pos(self.word_sentence_list)
        self.entity_sentence_list = self.ner(self.word_sentence_list, self.pos_sentence_list)
        
        dic = {"ws": self.word_sentence_list[0],
               "pos": self.pos_sentence_list[0],
               'ner': self.entity_sentence_list[0]}

        return(dic)

