# import tools
from emotional_score import emotional_score
emotional_feature = emotional_score()

from ckip_stat import ckip_static
ckip_feature = ckip_static() 

from Punctuation import Punctuation
punctuation_feature = Punctuation()

from Informality import Swear_words, Netspeak
swear_words_feature = Swear_words()
netspeak_feature = Netspeak()

from Quantity import article
quantity_feature = article()

class feature_class:
    def __init__(self, feature_func = [ckip_feature, 
                                       netspeak_feature, 
                                       swear_words_feature, 
                                       quantity_feature, 
                                       emotional_feature, 
                                       punctuation_feature], ifBOW = True):
        self.feature_func = feature_func
        self.ifBOW = ifBOW
        
        self.create_index_dict()
        
    
    def create_index_dict(self):
        buf = {}
        for func_i in self.feature_func:
            buf_i = func_i("測試")
            buf.update(buf_i) 
            
        self.keys = list(buf.keys())  
        if( not self.ifBOW):
            self.keys = self.keys[7383:]
        
        self.index_dict = dict(zip(range(len(self.keys)), self.keys))
        
    def before_feature_enginnering(self, str_):
        str_ = str_.replace("[UNK]", "")
        str_ = str_.replace("\n", " ")
        return(str_)
    
    def __call__(self, str_):
        str_ = self.before_feature_enginnering(str_)
        
        buf = {}
        for func_i in self.feature_func:
            buf_i = func_i(str_)
            buf.update(buf_i)
        
        buf = list(buf.values())
        
        if( not self.ifBOW):
            buf = buf[7383:]
            
        return( buf )
    
if( __name__ == "__main__"):
    test = feature_class(ifBOW = False)
    buf_i = test("測試用")
    print(buf_i)
    print(test.index_dict)