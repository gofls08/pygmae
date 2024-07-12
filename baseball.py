import random

num = random.sample(range(1,9),4)
#임의의 숫자 4개 선언, 중복x
print("숫자 4개를 맞추시면 됩니다.\n숫자와 자리까지 모두 맞추실 경우 strike, 숫자만 맞을 경우 ball로 나타납니다.\n기회는 총 10번입니다.\n띄어쓰기 없이 숫자를 입력해주세요")

i = 0

while True:
    list_user =[]
    str=0
    ball = 0
    i = i+1
    user = input("숫자 4개를 입력해주세요\n")
    for n in range(4):
        list_user.append(int(user[n]))
        n = n + 1
    print(list_user)
    for a in range(4):
        if num[a] == list_user[a]:
            str = str + 1
        for b in range(4):
            if num[a] == list_user[b]:
                ball = ball + 1
    if str == 4:
        print("Perfect\n",i,"번 만에 맞췄습니다")
        break
    else:
        print(str,"strike, ",ball-str,"ball, ",4-ball,"out")
    if i>= 10:
        print("game over")
        break
    