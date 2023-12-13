import random as rnd

data = [rnd.randint(1, 1000) for _ in range(10)]
data = sorted(data)
print(data)
su3 = [a for a in data if a%3 == 0]
n3 = len(su3)

su5 = [a for a in data if a%5 == 0]
n5 = len(su5)

su15 = [a for a in su5 if a in su3]
n15 = len(su15)

print("3의 배수: ", su3)
print("5의 배수: ", su5)
print("15의 배수: ", su15)
print(n3+n5-n15) ##3또는 5의 배수의 개수