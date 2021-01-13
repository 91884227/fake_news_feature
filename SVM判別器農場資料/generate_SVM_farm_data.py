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

def data_preprocessing(path_list):
    # check input type
    assert type(path_list)==list, "input type 需為 list"
    
    # check data exist
    for i in path_list:
        assert os.path.exists('../真實新聞資料/%s' % i), "%s 不在真實新聞資料內" % i
    
    # read data 
    buf_data = []
    for path in tqdm(path_list):
        with open('../真實新聞資料/%s' % path) as json_file:
            buf_data_for = json.load(json_file)
            buf_data = buf_data + buf_data_for   
    
    # choose data
    buf_data = random.choices(buf_data, k=args.num//2)
    
    # extract
    buf_data = [(i["title"], i["body"]) for i in buf_data]
    
    # replace \xa0 \u3000
    buf_data = [(i[0], i[1].replace("\xa0", " ")) for i in buf_data]
    buf_data = [(i[0], i[1].replace("\u3000", " ")) for i in buf_data]
    
    # delele data 
    buf_data = [i for i in buf_data if( len(i[1]) > 150 and len(i[0]) > 10)]
    
    return(buf_data)


def main():
    normal_data = data_preprocessing(['cna_ok.json','cts_ok.json','pts_ok.json','tvbs_ok.json'])
    farm_data = data_preprocessing(['ck101_ok.json'])

    # Generate X & y
    X = normal_data + farm_data
    y = [0]*(len(normal_data)) + [1]*(len(farm_data))

    # split two
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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
    
if __name__ == "__main__":
    assert os.path.exists('../真實新聞資料/'), "真實新聞資料 不在上一層目錄"
    
    main()