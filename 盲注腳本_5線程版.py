#2023/7/9
#字典分5區
#輸入的url要包含'$$$'，且只能是連續三個'$'
#將url的'$$$'替換成字典參數並發送http請求，根據返回的http狀態碼處理結果
#導致服務器返回非200的參數就算是有效的payload (effective payload)
#返回200的則算是無效的payload (invalid payload)

from pip._vendor import requests
import time
import linecache
import threading


#\033[31m 紅色字
#\033[32m 綠色字
#\033[0m 重製屬性變一般字

print('\033[0m' ,end='')
thestring_ = input('\033[32m輸入url: \033[0m')  #綠色字
print("")

if len(thestring_) == 0:
    exit("輸入不能是空")

if "$$$" not in thestring_:
    exit("url內要有'$$$'")

if thestring_.count('$') >3:
    exit("只能是連續三個'$'")


#thestring_ = "http://localhost/test3.php?Send=send&userinput=user1&passwordinput=$$$"

filelen_ = 0
chunklen_ = 0


total_ = 0  #已執行行數
num1_ = 0  #有效payload數量
num2_ = 0  #無效payload數量

chunk1 =  []
chunk2 =  []
chunk3 =  []
chunk4 =  []
chunk5 =  []

path1_ = 'test.txt'
path2_ = 'effective_result.txt'
path3_ = 'invalid_result.txt'

file1_ = open(path1_,'r')  #讀取
file2_ = open(path2_,'w')  #寫入(覆蓋之前內容)
file3_ = open(path3_,'w')  #寫入(覆蓋之前內容)

filelen_ = len(file1_.readlines())  #行數
chunklen_ = filelen_ // 5
chunklen_ = chunklen_ + 1

chunk1 = linecache.getlines(path1_)[0 : chunklen_ * 1]
chunk2 = linecache.getlines(path1_)[chunklen_ * 1  : chunklen_ * 2]
chunk3 = linecache.getlines(path1_)[chunklen_ * 2  : chunklen_ * 3]
chunk4 = linecache.getlines(path1_)[chunklen_ * 3  : chunklen_ * 4]
chunk5 = linecache.getlines(path1_)[chunklen_ * 4  : filelen_ ]




def function1_():
    for c1 in chunk1:
        #print(c1, end='')
        c1 = c1.strip()  #去掉變數頭尾空白
        newurl1_ = thestring_.replace('$$$',c1)
        request1_ = requests.get(newurl1_)
        #print(request1_.status_code)
        #print(newurl1_)
        if request1_.status_code == 200:
            print(request1_.status_code, " | ",c1)
            global num2_
            num2_ = num2_ + 1
            print(c1,file = file3_)  #將無效payload寫入invalid_result.txt並換行
        else:
            print(f'\033[31m{request1_.status_code} \033[0m |  {c1}')  #將非200狀態碼變紅色，其他字串正常
            global num1_
            num1_ = num1_ + 1
            print(c1,file = file2_)  #將有效payload寫入effective_result.txt並換行
        global total_
        total_ = total_ + 1




def function2_():
    for c2 in chunk2:
        #print(c2, end='')
        c2 = c2.strip()
        newurl2_ = thestring_.replace('$$$',c2)
        request2_ = requests.get(newurl2_)
        #print(request1_.status_code)
        #print(newurl2_)
        if request2_.status_code == 200:
            print(request2_.status_code, " | ",c2)
            global num2_
            num2_ = num2_ + 1
            print(c2,file = file3_)  #將無效payload寫入invalid_result.txt並換行
        else:
            print(f'\033[31m{request2_.status_code} \033[0m |  {c2}')  #將非200狀態碼變紅色，其他字串正常
            global num1_
            num1_ = num1_ + 1
            print(c2,file = file2_)  #將有效payload寫入effective_result.txt並換行
        global total_
        total_ = total_ + 1





def function3_():
    for c3 in chunk3:
        #print(c3, end='')
        c3 = c3.strip()
        newurl3_ = thestring_.replace('$$$',c3)
        request3_ = requests.get(newurl3_)
        #print(request1_.status_code)
        #print(newurl3_)
        if request3_.status_code == 200:
            print(request3_.status_code, " | ",c3)
            global num2_
            num2_ = num2_ + 1
            print(c3,file = file3_)  #將無效payload寫入invalid_result.txt並換行
        else:
            print(f'\033[31m{request3_.status_code} \033[0m |  {c3}')  #將非200狀態碼變紅色，其他字串正常
            global num1_
            num1_ = num1_ + 1
            print(c3,file = file2_)  #將有效payload寫入effective_result.txt並換行
        global total_
        total_ = total_ + 1



def function4_():
    for c4 in chunk4:
        #print(c4, end='')
        c4 = c4.strip()
        newurl4_ = thestring_.replace('$$$',c4)
        request4_ = requests.get(newurl4_)
        #print(request1_.status_code)
        #print(newurl4_)
        if request4_.status_code == 200:
            print(request4_.status_code, " | ",c4)
            global num2_
            num2_ = num2_ + 1
            print(c4,file = file3_)  #將無效payload寫入invalid_result.txt並換行
        else:
            print(f'\033[31m{request4_.status_code} \033[0m |  {c4}')  #將非200狀態碼變紅色，其他字串正常
            global num1_
            num1_ = num1_ + 1
            print(c4,file = file2_)  #將有效payload寫入effective_result.txt並換行
        global total_
        total_ = total_ + 1


def function5_():
    for c5 in chunk5:
        #print(c5, end='')
        c5 = c5.strip()
        newurl5_ = thestring_.replace('$$$',c5)
        request5_ = requests.get(newurl5_)
        #print(request1_.status_code)
        #print(newurl5_)
        if request5_.status_code == 200:
            print(request5_.status_code, " | ",c5)
            global num2_
            num2_ = num2_ + 1
            print(c5,file = file3_)  #將無效payload寫入invalid_result.txt並換行
        else:
            print(f'\033[31m{request5_.status_code} \033[0m |  {c5}')  #將非200狀態碼變紅色，其他字串正常
            global num1_
            num1_ = num1_ + 1
            print(c5,file = file2_)  #將有效payload寫入effective_result.txt並換行
        global total_
        total_ = total_ + 1
      


    



#將多個程序放入線程池
threads_ = []  #創建池

t1_ = threading.Thread(target=function1_, args=())
threads_.append(t1_)  #放入池

t2_ = threading.Thread(target=function2_, args=())
threads_.append(t2_)

t3_ = threading.Thread(target=function3_, args=())
threads_.append(t3_)

t4_ = threading.Thread(target=function4_, args=())
threads_.append(t4_)

t5_ = threading.Thread(target=function5_, args=())
threads_.append(t5_)


start_ = time.time()
for i in threads_:
    i.start()

for i in threads_:
    i.join()
end_ = time.time()
time_ = end_ - start_
time_ = round(time_, 3)  #取到小數點後三位

file1_.close()
file2_.close()
file3_.close()


linecache.clearcache()  #清除文件緩存

print("字典總行數: " + str(filelen_))
print("每一區塊行數: " + str(chunklen_))
print("已執行行數: " + str(total_))
print("有效payload的數量: " + str(num1_))
print("無效payload的數量: " + str(num2_))
print("運行時間: " + str(time_) + "秒")


