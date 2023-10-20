def solution(arr):
    an = []
    for item in arr:
        if an[-1:] == [item]: continue
        an.append(item)
    return an