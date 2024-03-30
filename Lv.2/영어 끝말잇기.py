def solution(n, words):
    answer = [0, 0]
    checks = set()
    
    for i, word in enumerate(words):
        if i != 0 and (word in checks or words[i - 1][-1] != word[0]):
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break
        checks.add(word)
    
    return answer