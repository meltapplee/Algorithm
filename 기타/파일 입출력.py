import random as rnd

data = [[rnd.randint(0,100), ' '] for _ in range(5)]
print(data)
##a = [82, ' '] ##a의 점수 82, 등급을 어떻게 정하지?
for a in data:
    if a[0] >= 90: a[1] = 'A'
    elif a[0] >= 80: a[1] = 'B'
    elif a[0] >= 70: a[1] = 'C'
    elif a[0] >= 60: a[1] = 'D'
    else: a[1] = 'F'

print(data, type(data))

with open("filefile.txt", "wt") as fd:
    ##filefile.txt파일을 wt라는 이름으로 열겠다
    for a in data:
        fd.write(str(a)+'\n')

with open("filefile.txt", "rt") as fd: ##파일 생성
    ##파일_객체 = open(파일_이름, 파일_열기_모드) - r(읽기), w(쓰기), a(추가하기) + t(텍스트) or b(바이너리)
    data = fd.readline() ##line 별로 읽기
print(data, type(data)) 