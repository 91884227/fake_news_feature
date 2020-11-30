# fake_news_feature

###### tags: `README`

# ckip_stat.py
> output 包含 BOW NER POS 的 feature

* usage
```python
from ckip_stat import ckip_static
test = ckip_static()
test("三點你去你的台北")
```
```python
# return:
# { 'GPE': 1, 'PERSON': 0, ...}
```


# Punctuation.py

* usage

```python
from Punctuation import Punctuation
punctuation = Punctuation()
punctuation("you suck  !!!!!!!【「")
```

```python
# return
{'#!': 7, '#...': 0, '# ?': 0, '# ~': 0, '# 「': 2, '# total': 9}
```

# Informality.py
* usage
```python
from Informality import Swear_words, Netspeak
swear_words = Swear_words()
netspeak = Netspeak()

swear_words("靠腰食潲") # {'swear_words': 2}
netspeak("GG948794狂") # {'Netspeaks': 3}
```

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
ckip_class.segmentation("三點你去你的台北")
# {'ws': ['三點', '你', '去', '你', '的', '台北'],
# 'pos': ['Nd', 'Nh', 'VCL', 'Nh', 'DE', 'Nc'],
# 'ner': {(0, 2, 'TIME', '三點'), (6, 8, 'GPE', '台北')}}
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



