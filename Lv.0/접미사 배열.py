def solution(my_string):
    arr = []
    for i in range(len(my_string)):
        arr.append(my_string[i:])
        answer = sorted(arr)
    
    return answer