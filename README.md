# fake_news_feature

###### tags: `README`


# ckip.py
> 計算input 內 聳動pattern 的數量
> 需要再改進

```python
from clickbait_pattern import clickbait_pattern
clickbait_p = clickbait_pattern()
clickbait_p("我不相信你") # 0
```

# ckip.py
> 中研院斷詞
```python=
from ckip import ckip
ckip_class = ckip()
ckip_class("我不相信你") 
# {'ws': ['我', '不', '相信', '你'], 'pos': ['Nh', 'D', 'VK', 'Nh'], 'ner': set()}
```


## real_fake_news_dataset - DTL_Data 
不知道欄位所代表的意義為何　已寄信詢問
![](https://i.imgur.com/g1aC39f.png)

-> 中研院回復
![](https://i.imgur.com/Bqm5j0Y.png)



## real_fake_news_dataset - GoogleFactCheck
僅有文字 沒有文章 標題?? 已寄信詢問
![](https://i.imgur.com/DzkDLhT.png)

-> 中研院回復
![](https://i.imgur.com/ODMbYQ1.png)



