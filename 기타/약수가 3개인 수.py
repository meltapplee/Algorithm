import random as rnd
import math as mt
##약수가 3개인 수 : 어떤 소수의 제곱수
def sosu(Max):
    su, rst = [a for a in range(2, Max+1)], []##관리할 데이터(2-100까지의 수
    while su[0]**2 <= Max:
        rst.append(su[0])
        su = [a for a in su if a%su[0]]
    
    return rst + su

Max = 100
ss = sosu(int(mt.sqrt(Max))) ##sqrt -> 루트 구하는 함수
gijun = [a*a for a in ss]
print(gijun)
data = [rnd.randint(1,Max) for _ in range(10)]
result = [a for a in data if a in gijun]

print(data)
print(result, len(result))