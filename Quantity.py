#!/usr/bin/env python
# coding: utf-8

# # import tool 

# In[84]:


import json
import re
import jieba


# In[85]:


class token:
    def __init__(self, str_):
        assert type(str_) == str, "input 要是 string"
        self.token = str_
    
    def __len__(self):
        return(len(self.token))
    
    def __repr__(self):
        return("<token>: %s" % self.token)


# In[86]:


# test = token("不要")


# In[87]:


class sentence:
    def __init__(self, str_):
        assert type(str_) == str, "input 要是 string"
        self.sentence = str_
        buf = jieba.lcut(self.sentence, cut_all = False, HMM = True)
        self.token_list = [token(i) for i in buf]
        self.token_num = len(self.token_list)
    
    def __len__(self):
        return(len(self.sentence))    

    def __repr__(self):
        return "<sentence>: %s" % self.sentence


# In[88]:


# test = sentence("不要嘴我要活下去")


# In[89]:


class paragraph:
    def __init__(self, str_):
        assert type(str_) == str, "input 要是 string"
        self.paragraph = str_
        buf = re.split('[。，?]', str_) 
        self.sentence_list = [sentence(i) for i in buf if len(i) > 0]
        self.sentence_num = len(self.sentence_list)
        self.word_num = sum( [len(i) for i in self.sentence_list] ) 
        self.token_num = sum( [i.token_num for i in self.sentence_list] ) 
    
    def __len__(self):
        return( len(self.paragraph) )
    
    def __repr__(self):
        return "<paragraph:> %s ..." % self.paragraph[:10]


# In[90]:


# test = paragraph("昨天，我堂哥喬遷大喜，我不勝榮幸，和他分享那份喜悅。")


# In[96]:


class article:
    def __call__(self, str_):
        assert type(str_) == str, "input 要是 string"
        self.article = str_
        buf = self.article.split("\u200b")
        self.paragraph_list = [paragraph(i) for i in buf if len(i) > 0]
        
        self.paragraph_num = len(self.paragraph_list)
        self.sentence_num = sum([i.sentence_num for i in self.paragraph_list])
        self.token_num = sum([i.token_num for i in self.paragraph_list])
        self.paragraph_word_avg = sum([len(i) for i in self.paragraph_list])/self.paragraph_num
        self.paragraph_token_avg = sum([i.token_num for i in self.paragraph_list])/self.paragraph_num
        
        buf = sum( [len(sent) for i in self.paragraph_list for sent in i.sentence_list] )
        self.token_len_avg =  buf / self.token_num
        
        buf = sum([sent.token_num for i in self.paragraph_list for sent in i.sentence_list])
        self.sentence_token_avg = buf/ self.sentence_num
        
        dic = {"character_num": len(self.article), 
           "paragraph_num" : self.paragraph_num, 
           "sentence_num" : self.sentence_num, 
           "token_num" : self.token_num, 
           "paragraph_word_avg" : self.paragraph_word_avg, 
           "paragraph_token_avg" : self.paragraph_token_avg, 
           "token_len_avg": self.token_len_avg,
           "sentence_token_avg": self.sentence_token_avg}  
        
        return(dic)
    
    def __len__(self):
        return( len(self.article) )
    
    def __repr__(self):
        return "<article:> %s ..." % self.article[:20]
    


# In[97]:


# text = "昨天，我堂哥喬遷大喜，我不勝榮幸，和他分享那份喜悅。\u200b結婚十多年了，他們一直在為下一代努力奮鬥著，生活的多姿多彩，他們沒有時間和心情去好好的欣賞這個世界上美好的風景。一直到今年疫情的原因，因為疫情的存在，耽擱了我們，同樣也耽擱了他們的事業，不過也好，這樣就能好好的休息一下，好好的享受一下這明媚的春光了。說說他們一家子吧，\u200b他們一家人和我們每一個人都一樣，都很普通。有愁苦，有喜悅，有煩憂又有歡樂。我們有的他們一樣不少。這麼多年了，他們生活依然很和睦。雖然有時因為一些生活瑣事兒也吵個不停，但這似乎是他們生活的調味劑，就像生活這道菜一樣，有酸甜也有苦辣。一直很平淡也很沒意思。增添一點調節劑也不失為一種很好的催化劑。其實生活的調味劑有很多的，生活條件是一方面，另外就是生活激情。不止這些，還有生活的情調。這不，他們的新房裝修好了。現在為了以後的生活質量，現在再為這個新家準備著。畢竟這是他們以後溫暖的小窩。這種感覺真好。我也想到了我以後的日子，攜著愛人的手，居住這我們溫暖的小窩，過著溫馨的日子。這種日子挺好的。……為了接下來的好日子，好好生活，好好掙錢，趕緊談個戀愛，找到一個美好的另一半。想想都是很美好的。"

# test = article()

#test(text)
