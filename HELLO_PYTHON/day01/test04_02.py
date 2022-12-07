#로또를 생성하세요(1~45 숫자중에서 중복없이 6개 가져오기)
#제일 기본적인 방법이다
#파이썬은 가장 기본적인 코드로 짤 수 있어야한다
from random import random
arr45 = list(range(1,46))

for i in range(1000) :
    rnd = int(random()*45)
    
    a = arr45[0]
    b = arr45[rnd]
    arr45[0] = b
    arr45[rnd] = a

        
print(arr45[0],arr45[1],arr45[2],
      arr45[3],arr45[4],arr45[5])