#coding=utf-8
import os
import pandas as pd
import glob
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def hebing():
    csv_list = glob.glob('*.csv')
    print(u'共发现%s个CSV文件'% len(csv_list))
    print(u'正在处理............')
    for i in csv_list:
        fr = open(i,'r').read()
        with open('haha.csv','a') as f:
            f.write(fr)
    print(u'合并完毕！')

def quchong(file):
    df = pd.read_csv(file,header=0)
    datalist = df.drop_duplicates()
    datalist.to_csv(file)

if __name__ == '__main__':
    hebing()
    quchong("haha.csv")