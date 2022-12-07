#로또를 생성하세요(1~45 숫자중에서 중복없이 6개 가져오기)
import random

a = 0
x = []

for i in range(7):
    a = random.randint(1,45)
    if a not in x:
        x.append(a)
        x.sort()
print(x)