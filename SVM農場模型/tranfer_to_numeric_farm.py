# cd ./fake_news_feature/SVM農場模型
# python tranfer_to_numeric_farm.py --d Size_5000

# import tool
import os
from tqdm import tqdm

import json
import copy
from SVM_feature_engineering import feature_class

# import argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--d", default = "Size_100", type=str)
parser.add_argument("--B", default = False, type=bool)
parser.add_argument("--test", default = False, type=bool)
args = parser.parse_args()


def buf_func(file_):
    data_path = "./SVM判別器農場資料/%s/" % args.d
    with open(data_path + file_) as json_file:
        data = json.load(json_file)

    if( args.test):
        data = data[:2]  
    
    print("Start to deal with %s" % file_)
    data_numeric = [feature_func(i[0]) + feature_func(i[1]) for i in tqdm(data)]
    
    # new add 
    data_numeric = [ [ float(j) for j in i] for i in data_numeric]

    path = "./SVM_數值資料/%s/%s" % (args.d, file_)
    with open(path, 'w') as outfile:
        json.dump(data_numeric, outfile)
    
    print("success to save file in  %s" % path )

def create_index_dict():
    a, b = copy.deepcopy(feature_func.index_dict), copy.deepcopy(feature_func.index_dict)
    for i, v in enumerate(a):
        a[v] = "<title:> %s" % a[v]

    for i, v in enumerate(b):
        a[i+len(b)] = "<body:> %s" % b[v]

    path = "./SVM_數值資料/%s/%s" % (args.d, "index_dict.json")
    with open(path, 'w') as outfile:
        json.dump(a, outfile)

def main():
    os.mkdir("./SVM_數值資料/%s" % args.d)
    buf_func("X_train.json")
    buf_func("X_test.json")
    create_index_dict()

if __name__ == "__main__":
    path = "./SVM判別器農場資料/%s" % args.d
    assert os.path.exists(path), "%s不存在" % path
    
    feature_func = feature_class(ifBOW = args.B)
    main()
    
