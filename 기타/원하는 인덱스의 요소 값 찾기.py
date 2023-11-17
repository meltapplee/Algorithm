list_n = []
number = 1
for i in range(1000):
  list_n.append(number)
  number += 2
n = input("몇번 째 요소의 값을 원하십니까? ")
n = int(n)
num = 1
tmp = 0
cnt = 0
while n > 0:
  tmp = n
  n -= num
  cnt += num
  num += 1
print(f"Group: {num - 2}의, index: {tmp-1}번째 인덱스, 값은 value: {list_n[tmp - 1]} 입니다")