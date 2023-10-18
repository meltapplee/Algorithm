from random import *

cnt = 0
luckyNum = set({8, 11, 15, 18, 21, 30})
numli = set()
money = 10000
setn = money // 1000

print(luckyNum, "1등 당첨 번호")
for i in range(setn):
    for j in range(12):
        numli.add(randint(1, 45))
        if len(numli) == 6: break
    for k in range(6):
        cnt = len(luckyNum & numli)
    if cnt == 0:
        print(numli, "0개 일치! ", "낙첨")
    else:
        print(numli, cnt, "개 일치! ", 7-cnt, "등")
    cnt = 0
    numli.clear()