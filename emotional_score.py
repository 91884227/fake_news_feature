import requests

class emotional_score:
    def __init__(self):
        self.url = "http://140.118.155.170:5000"
    
    def __call__(self, str_):
        assert type(str_)==str, "input 要是 str"
        
        try:
            query = {'document': str_}
            response = requests.post(self.url, json = query).json()
            score = float(response['score'])
            return({"emotional score": score})
        except:
            return({"emotional score": 0})
                