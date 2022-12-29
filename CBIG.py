# age = eval(input("请输入年龄"))
# if age >= 18 and age <= 60:
#     print("你好")
# else:
#     print("滚")








# has_ticket = True
# knife_long = 10
# if has_ticket:
#     print("检票成功")
#     print("欢迎乘车")
#     if knife_long > 20:
#         print("到太长了 %d 长" % knife_long)
#     else:
#         print("案件通过")
#
#
#
#
#
# else:
#     print("请买票")













# holiday_name = "平安夜"
# if holiday_name == "情人节":
#     print("买美国")
# elif holiday_name == "平安夜":
#     print("吃你妈")
# elif holiday_name == "傻逼节":
#     print("大哈比")
# else:
#     print("滚")





#



# python_score = 70
# if python_score >= 0 and python_score <= 60:
#     print("抱歉")
# else:
#     print("考试通过")






# is_yuangong = True
# if not is_yuangong:
#     print("禁止入内")
# else:
#     print("你好")





# age = 120
# if age >= 0 and age <= 100:
#     print("年龄正确")
# else:
#     print("年龄不争")





# age = 18
# if age >= 18:
#     print("欢迎进入网吧")
# else:
#     print("滚回去写作业")









#第一次
# name_number = 114514
# print("我的学号是 %06d" % name_number)




# # 第二次演练
# price = 10.34
# weight = 20.52
# money = price * weight
# print("苹果单价 %.2f 重量为 %.2f 总金额为 %.2f" % (price,weight,money))
#
#
# #第三次演练
# scale = 0.25
# print("数据比例是 %.2f%% " % (scale * 100))









# age =eval(input("请输入年龄"))
# if age >= 60:
#     print("恭喜，你可以退休了")






# price = eval(input("输入单价"))
# weight = eval(input("输入重量"))
# money = price * weight
# print(money)













# import random
#
# player = eval(input("请输入 石头 1 剪刀 2 布 3"))
# computer = random.randint(1,3)
# print("玩家出拳的是 %d - 电脑出的拳是 %d "% (player, computer))
# if ((player == 1 and computer== 2)
#         or (player == 2 and computer == 3)
#         or (player == 3 and computer == 1)):
#
#      print("恭喜玩家获胜")
# elif (player == computer):
#      print("平手")
# else:
#      print("玩家输了")






#
# i = 0
# while i < 5:
#      print("Hello")
#      i += 1
# print("数字 %d" % i)





# result = 0
# i = 0
# while i <= 100:
#      print(i)
#      result += i
#      i += 1
# print("数字和 %d" % result)




# result = 0
# i = 0
# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#         result += i
#     i += 1
# print("狮子王 %d" % result)





# result = 0
# i = 0
# while i <= 100:
#     if i % 2 != 0:
#         print(i)
#         result += i
#     i += 1
# print("狮子王 %d" % result)





# i = 0
# while i < 10:
#     if i == 3:
#         break
#     print(i)
#     i += 1






# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#
#     print(i)
#     i += 1



# row = 1
# while row <= 5:
#     print("*" * row)
#     row += 1



# print("*",end= "")
# print("*")


row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*",end="")
        col += 1
    print("")
    row += 1







































