# import tool
import os
from tqdm import tqdm
import json
import random

# import self-define tool
from GPT2_crawler import GP2_crawler, strB2Q

# argparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--titlefile", default = "./cts_title.json", type = str)
parser.add_argument("--savename", default = "cts", type = str)
parser.add_argument("--limit", default = None, type = int)
parser.add_argument("--TLUB", default = 500, type = int)
parser.add_argument("--TLLB", default = 900, type = int)

args = parser.parse_args()

# read data in
print("start to read data in")
assert os.path.exists(args.titlefile), "%s 不再目錄下" % args.titlefile
with open('cts_title.json') as json_file:
    data = json.load(json_file)
    
assert type(data) == list, "資料應為 [title1, title2, title3, ... , titlen] 的形式"
assert type(data[0]) == str, "資料應為  [title1, title2, title3, ... , titlen] 的形式"

print("start to load driver")
GP2_generator = GP2_crawler()

buf = []
count = 0

for i in tqdm(data):
    if( type(args.limit) != int or  count < args.limit):
        count = count + 1
    else:
        break
        
    title_length = random.randint(args.TLUB, args.TLLB)
    # title_length = 100
    try:
        generate_text = GP2_generator( strB2Q("%s\n" % i), title_length)
        buf = buf + [generate_text]
    except:
        print("error for generate %s" %i )
        
del GP2_generator

save_name = "GPT2_text_%s.json" % args.savename
with open(save_name, 'w', encoding='utf8') as outfile:
    json.dump(buf, outfile, ensure_ascii=False)

print("save data in %s" % save_name)