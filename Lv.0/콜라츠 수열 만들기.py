def solution(n):
    result = [n]

    while n != 1:
        if n%2:
            n = 3 * n + 1
        else:
            n //= 2
        
        result.append(n)

    return result