import random
print("欢迎游玩")
player = eval(input("请输入 点数 1 点数 2 点数 3 点数 4"))
computer = random.randint(1,4)
print("你输入的为 %d 电脑输入为 %d" %(player,computer))
if ((player == 2 and computer == 1 )
        or (player == 3 and computer == 1)
        or (player == 3 and computer == 2)
        or (player == 4 and computer == 1)
        or (player == 4 and computer == 3)
        or (player == 4 and computer == 2)):



    print("恭喜获胜")
elif(player == computer):

    print("平手")
else:

    i = 1
    while i <= 5:
        print("电脑都打不过")
        i += 1
    print("数字 %d" % i)
















