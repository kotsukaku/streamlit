#!/usr/bin/env python
# coding: utf-8

# In[3]:
import streamlit as st
import numpy
import pandas

st.title('Welcome to my first app')


# shop_car = []#用来存放购买的商品
goods = {
    1:['iPhone',2500],
    2:['パソコン',3500],
    3:['自転車',4500],
    4:['BMW',20000]
}#商品列表
while True:
    salary = input("お金はどれくらい持っていますか？") # 输入有多少钱
    if salary.isdigit(): # 判断是否为整数
        salary = int(salary) # 将字符串转化为整数
        print("何かを買うか買わないか：")
        flag1 = input("Y      N:")
        if flag1.upper() == 'N': # 将字符串大写
            exit("ありがとうございました!") # 退出程序并输出“ありがとうございました!”
        elif flag1.upper() == 'Y':
            break                # 终止循环
        elif flag1.upper() == 'Q':
            exit("ありがとうございました!")
    elif salary.upper() == 'Q':
        exit("ありがとうございました!")
while True:
        print("AMAZON".center(30,'-')) # 输出以-----amazon------
        for i in goods: # 循环输出
            print(i,goods[i])
        print("AMAZON".center(30, '-'))
        choice_good = input("商品の番号を入れてください")#接受一个字符串
        if choice_good.isdigit() :
            choice_good = int(choice_good)
            if choice_good >= 1 and choice_good <= 4:
                if salary >= goods[choice_good][1]:
                    shop_car.append(goods[choice_good][0]) # 给字典中添加元素
                    salary = salary - goods[choice_good][1]
                    print("ご購入いただいた商品は：", goods[choice_good][0])
                    print("残額：", salary)
                    print("続けますか")
                    contin = input("Y    N")
                    if contin.upper() == 'N':
                        break
                    elif contin.upper() == 'Q':
                        break
                else:
                    print('お金は足りないんです')
                    print("続けますか：")
                    contin = input("Y    N")
                    if contin.upper() == 'N':
                        break
                    elif contin.upper() == 'Q':
                        break
            else :
                print("番号なしです")
                continue # 暂停本次循环
        elif choice_good.upper() == "Q" :
            break
        else:
            print("意味不明")
print("買うものは",end =' ')
for i in shop_car:
    print(i,end=' ')
print()
print("残額：",salary)
print("ありがとうございました!")


# In[ ]:




