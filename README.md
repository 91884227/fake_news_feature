# fake_news_feature

###### tags: `README`


# Quantity.py
> 目前只用 \u200b 來分段 需要再改進。



* USAGE
```python
from Quantity import article
quantity = article()
quantity("我不相信Y") 
```

```python
RETURN:
{'character_num': 5,
 'paragraph_num': 1,
 'sentence_num': 1,
 'token_num': 4,
 'paragraph_word_avg': 5.0,
 'paragraph_token_avg': 4.0,
 'token_len_avg': 1.25,
 'sentence_token_avg': 4.0}
```


# clickbait_pattern.py
> 計算input 內 聳動pattern 的數量
> 需要再改進pattern

```python
from clickbait_pattern import clickbait_pattern
clickbait_p = clickbait_pattern()
clickbait_p("你不可不知的38個")
# {'clickbait_pattern': 2}
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



