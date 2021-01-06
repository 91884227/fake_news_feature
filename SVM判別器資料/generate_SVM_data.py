# import tool
import json
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import random
import os

# import argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--num", default = 100, type=int)
args = parser.parse_args()


# assert message
assert args.num<6000, "num 應小於6000"
assert os.path.exists('../真實新聞資料/'), "真實新聞資料 不在上一層目錄"
assert os.path.exists('../GPT生成資料/'), "GPT生成資料 不在上一層目錄"

# read data 
path_list = ['ck101_ok.json','cna_ok.json','cts_ok.json','pts_ok.json','tvbs_ok.json']
real_data = []
for path in path_list:
    with open('../真實新聞資料/%s' % path) as json_file:
        real_data_for = json.load(json_file)
        real_data = real_data + real_data_for

gpt_data = []
for path in os.listdir("../GPT生成資料"):
    with open('../GPT生成資料/%s' % path) as json_file:
        gpt_data_for = json.load(json_file)
        gpt_data = gpt_data + gpt_data_for

# random choose
real_data = random.choices(real_data, k=args.num//2)
gpt_data = random.choices(gpt_data, k=args.num//2)

# extrace body
real_data = [i["body"] for i in real_data]

# Generate X&y
X = real_data + gpt_data
y = [0]*(args.num//2) + [1]*(args.num//2)
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42)

# save result
os.mkdir("Size_%s" % args.num)
with open("./Size_%s/%s.json" % (args.num, "X_train"), 'w', encoding='utf8') as outfile:
    json.dump(X_train, outfile, ensure_ascii=False)
    
with open("./Size_%s/%s.json" % (args.num, "X_test"), 'w', encoding='utf8') as outfile:
    json.dump(X_test, outfile, ensure_ascii=False)
    
with open("./Size_%s/%s.json" % (args.num, "y_train"), 'w', encoding='utf8') as outfile:
    json.dump(y_train, outfile, ensure_ascii=False)
    
with open("./Size_%s/%s.json" % (args.num, "y_test"), 'w', encoding='utf8') as outfile:
    json.dump(y_test, outfile, ensure_ascii=False)

print("save data in Size_%s" % args.num)