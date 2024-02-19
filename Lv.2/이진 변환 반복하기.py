def solution(s):
    n, m = 0, 0
    while s != '1':
        n += 1
        num = s.count('1')
        m += len(s) - num
        s = bin(num)[2:]
    return [n, m]