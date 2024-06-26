#2023/8/9
#用於計算盲注經過的時間，單位是秒

from pip._vendor import requests
import time

wordnumber_ = 0
path1_ = "time_dictionary.txt"  #參數字典
path2_ = "time_result.txt"  #輸出檔

file1_ = open(path1_,'r',encoding='utf-8')  #讀取
file2_ = open(path2_,'w',encoding='utf-8')  #寫入(覆蓋之前內容)

http_ =""

print('\033[0m' ,end='')
theinput_ = input('\033[32m輸入url: \033[0m')  #綠色字
print("")

if len(theinput_) == 0:
    exit("輸入不能是空")

if "$$$" not in theinput_:
    exit("url內要有'$$$'")

if theinput_.count('$') >3:
    exit("只能是連續三個'$'")


for word_ in file1_:
    wordnumber_ = wordnumber_+1
    word_ = word_.strip()  #去掉參數的頭尾空白
    http_ = theinput_.replace('$$$', word_)  #構建http請求

    start_ = time.time()  #開始計時
    request_ = requests.get(http_)  #http

    if request_.status_code != 200:
        # print("WRONG", "  |  ", word_)
        wrongoutput_ = "WRONG"+"   |   "+word_
        file2_.write(wrongoutput_ +'\n')
        print(f'\033[31m{"WRONG"} \033[0m  |   {word_}')  #將WRONG轉成紅色 其他正常
        continue

    end_ = time.time()    #結束計時
    timespend_ = (end_ - start_)
    timespend_ = str(timespend_)  #轉成字串
    
    dot_ = '.'
    dotseat_ = timespend_.find(dot_)  #小數點出現位置
    timespend_ = timespend_[0:dotseat_ + 4]  #擷取至小數點後3位

    if dotseat_ <= 1:                       #判斷位數是否在1以下
        output_ = timespend_+ "   |   "+ word_
        file2_.write(output_ +'\n')  #輸出時間與參數到time_result.txt
        print(output_) #輸出時間與參數
    if dotseat_ > 1:                        #判斷位數是否在1以上
        output_ = timespend_+ "  |   "+ word_  #因為是二位數所以少一個空格
        file2_.write(output_ +'\n')  #輸出時間與參數到time_result.txt
        print(output_)  #輸出時間與參數

print("")
print("字典: " + path1_)
print("字典總行數: " + str(wordnumber_))
print("輸出: " + path2_)

dot_ = '.'
dotnumber_ = timespend_.find(dot_)

file1_.close()
file2_.close()
