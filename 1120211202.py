# 例3-1
# total=0
# for inum in range(1,10001):
#     total+=inum
# print("1~10000的总和为"+str(total))

# 例3-2
# total=0
# for inum in range(2,10001,2):
#     total+=inum
# print("1~10000的总和为"+str(total))

# 例3-3
# word="山羊上山山碰山羊角"
# sum=0
# for letter in word:
#     if letter =="山":
#         sum+=1
# print(sum)

# 例3-4
# plaincode=input("请输入明文：")
# for p in plaincode:
#     if ord("a")<=ord(p)<=ord("z"):
#         print(chr(ord("a")+(ord(p)-ord("a")+3)%26),end="")
#     else:
#         print(p,end="")

# 例3-5
# for inum in ['A','B','C','D']:
#     if(inum!='A')+(inum!='B')+(inum!='C')+(inum!='D')==3:
#         print(inum,"做了好事")

# 例3-6
# time=8
# while time<12:
#     print("time={},有效次数内".format(time))
#     time+=1
# else:
#     print("计次已满")

# 例3-7
# import math
# n=1
# t=1
# total=0
# flag=1
# count=0
# while math.fabs(t)>=1e-6:
#     total+=t
#     flag=-flag
#     n+=2
#     t=flag*1.0/n
#     count+=1
#     print("count:{},Π={}".format(count,total*4))

# 例3-8
# for i in range(1,10):
#     for j in range(1,10):
#         print("{}*{}={}".format(i,j,i*j),end="\t")
#     print("\n")

# 例3-9
# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         print("*",end=" ")
#     print()

# 例3-10
# import random
# games=10
# for i in range(games):
#     print("进行第{}场游戏".format(i+1))
#     result=random.randint(0,1)
#     if result==1:
#         print("朋友圈炫耀战绩")
#     else:
#         print("沉默...")
#     print("*"*20)

# 例3-11
# import random
# games = 10
# for i in range(games):
#     print("进行第{}场游戏".format(i+1))
#     #增加游戏过程中的感觉
#     feeling = random.randint(0,10) #0:开心，1:不爽，2:愤怒
#     if 5<= feeling <= 9:
#         print("中断本次游戏，开始下一局")
#         continue
#     elif feeling == 10:
#         print("中断游戏，不玩了")
#         break
#     else:
#         print("玩得很开心")
#     #随机产生游戏结果
#     result = random.randint(0,1) #0:失败，1:胜利
#     if result == 1:#获胜
#         print("朋友圈炫耀战绩")
#     else: #result ==0,失败
#         print("沉默...")
#     print("*"*20)

# 例3-15
# import random
# point=random.randint(1,6)
# count=1
# while count<=3:
#     guess=int(input("请输入您的猜测:"))
#     if guess>point:
#         print("您的猜测偏大")
#     elif guess<point:
#         print("您的猜测偏小")
#     else:
#         print("恭喜您猜对了")
#         break
#     count=count+1
# else:
#     print("很遗憾，三次全猜错了! ")

# 例3-16
# sentence=input("请输入一段文字:")
# for word in sentence:
#     if word=="密":
#         continue
#     print(word,end="")

# 例3-17
# while 1:
#     password=input("请输入密码:")
#     if len(password)<6:
#         print("长度为6位，请重试! ")
#         continue
#     if password=="123456":
#         print("恭喜您，密码正确!")
#         break
#     else:
#         print("密码有误，请重试! ")



#上机作业1
# # 编写程序，从键盘输入数字n，通过循环计算1~n的乘积
# n=input("输入数字n，计算机1~n的乘积：")
# n=int(n)
# i=1
# result=1
# while i<=n:
#     result=i*result
#     i+=1
# print(result)

# 上机作业2
# 编写程序，通过循环计算全部水仙花数，并依次输出。水仙花数是一个三位数字，该数字等于组成该三位数的各位数字的立方和。例如1^3+5^3+3^3=153
# for a in range(1,10):
#     for b in range(1,10):
#         for c in range(1,10):
#             d=a*100+b*10+c
#             if a*a*a+b*b*b+c*c*c==d:
#                 print(d)


# 上机作业3
# 编写程序，判断一个整数是否为素数（判断整数x是否为素数，最简单的方法就是用2~x-1之间的所有整数逐一去除x，若x能被其中任意一个数整除，则x就不是素数，否则就为素数）
# flag=1
# num=eval(input("输入一个整数："))
# if (num==1)or(num==2):
#     print("yes")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             flag=0
#
# if flag==0:
#     print("不是素数")
# else:
#     print("是素数")

# 上机作业4
# 编写程序，开发一个循环5次计算的小游戏，每次随机产生两个100以内的数字，让用户计算两个数字之和并输入结果，如果计算结果正确则加一分，如果计算结果错误则不加分。如果正确率大于等于80%，则闯关成功
# import random
# flag=0
# for i in range(5):
#     x=random.randint(1,100)
#     y=random.randint(1,100)
#     z=x+y
#     x=str(x)
#     y=str(y)
#     result=eval(input("请计算"+x+"+"+y+"的结果："))
#     if z==result:
#         flag+=1
#         print("正确"+str(flag))
#     else:
#         print("错误"+str(flag))
# if flag>=4:
#     print("闯关成功")
# else:
#     print("下次一定")


