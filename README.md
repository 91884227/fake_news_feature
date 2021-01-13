# fake_news_feature

###### tags: `README`

# generate_SVM_farm_data.py
檔案在 ./SVM判別器農場資料/
* usage
```python
python generate_SVM_farm_data.py [--num num] 
```
| parameter | 說明 | e.g. |
| -------- | -------- | -------- |
| num     | 資料大小   | 100   |


# transfer_to_numeric_feature.py
檔案在 ./SVM模型 下

將放在 SVM判別器的資料 做 feature engineering

* usage
```python=
python transfer_to_numeric_feature.py [--d datafolder] [--B ifBOW] [--test Bool] 
```
| parameter | 說明 | e.g. |
| -------- | -------- | -------- |
| d    | 資料集名稱 (需放在)   |  Size_50  |
| B    | 是否用 Bag-of-word Feature   | False   |
| test   | 是否為測試   | False   |

# SVM_feature_engineering.py
檔案在 ./SVM模型 下
* usage
```python
from SVM_feature_engineering import feature_class
test = feature_class(ifBOW = False) # Ture if you want to use BAG-OF-WORD Fearure
buf_i = test("測試用") # 輸出list
buf_i.index_dict # index 和 feature 對應的 dictionary
```

# generate_SVM_data.py
在  /SVM判別器資料 下生成 /Size_num的資料夾
內含 X_test X_train y_train y_test
* usage
```python
python generate_SVM_data.py [--num num] 
```
| parameter | 說明 | e.g. |
| -------- | -------- | -------- |
| num     | 資料大小   | 100   |

* 附註 目前因GPT資料最大為6000 故NUM 設定最多為6000

# emotional_score.py
* usage
```python
from emotional_score import emotional_score
test = emotional_score()
test("你去吃大便") # {"emotional score": 0.12}
```

# GPT2_generate_text.py
* usage
```python
python GPT2_generate_text.py [--titlefile] [--savename][--limit][--TLUB][--TLLB][--Start]
```
* parameter

| parameter | 說明 | e.g. |
| -------- | -------- | -------- |
| titlefile     | 標題黨的檔案位置   | Text     |
| savename     | 儲存的黨名     | Text     |
| limit     | 最多做幾筆資料    | 10    |
| TLUB     | GPT2生成文章的最短長度     | 50     |
| TLLB     | GPT2生成文章的最長長度    | 100     |
| Start     | 資料要從哪一筆開始做     | 1000     |


# GPT2_crawler.py
* usage
```python
from GPT2_crawler import GP2_crawler, strB2Q
test = GP2_crawler()
```


# ckip_stat.py
> output 包含 BOW NER POS 的 feature

* usage
```python
from ckip_stat import ckip_static
test = ckip_static() # 預設: 華語八千詞表_dictionary.json 

test("三點你去你的台北")
```
```python
# return:
# { 'GPE': 1, 'PERSON': 0, ...}
```

* dictionary 可改成以下:

| Column 1 | Column 2 | 
| -------- | -------- | 
| 華語八千詞表_dictionary.json     | Text     |
| pts_8000_dictionary.json     | Text     |


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



