#로또를 생성하세요(1~45 숫자중에서 중복없이 6개 가져오기)
#제일 기본적인 방법이다
#파이썬은 가장 기본적인 코드로 짤 수 있어야한다
from random import random

arr6 = [1,2,3,4,5,6]

for i in range(1000):
    rnd = int(random()*6)
    
    a = arr6[0]
    b = arr6[rnd]
    arr6[0] = b
    arr6[rnd] = a

print(arr6[0],arr6[1],arr6[2])