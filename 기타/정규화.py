import pickle as pk
import re

##__는 영문자로 취급됨
strtxt = '''f F____ F---- beautiful 
Fly
Hello world!! This is python calss.
Python class is fun fun !!
Python is storm!!
Friday is always tired
'''
##f로 시작하는 단어 찾기

pt = re.compile(r"\sf\w*", re.IGNORECASE)
words = pt.findall(' ' + strtxt)
words = [a.strip() for a in words]
##strip 괄호 안에 아무것도 없으면 문자열 앞뒤의 공백을 제거
print(words)

a = " abcd"
b=a.strip()
print(b, a)
print(words, len(words))