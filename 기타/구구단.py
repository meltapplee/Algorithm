form = "{a} X {b} = {a*b}\t" ## = "%d X %2d = %d\t" 

part = 3 ##part = 한 문단에 몇개의 구구단이 나올 것 인지 2, 5, 8단에서 문단 변경
for g in range(2, 10, part):
    for b in range(2, 10, 2):
        for a in range(g, g+part):
           print(f"{a}X {b} = {a*b}\t", end=' ') ##{}괄호 안에서는 띄어놔도 값 표현에 변화X
           ##print(form % (a, b, a*b), end=' ')
        print()
    print()