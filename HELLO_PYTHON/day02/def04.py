def addminmuldiv(a,b):
    return a + b ,a - b , a*b, a/b 

sum, min, mul, div = addminmuldiv(5,4)


print("sum",sum)
print("min",min)
print("mul",mul)
print("div",div)

#2,3개 만 있으면 안뜨지만 오히려 한개만 있으면 뜸
#약간 배열같은 느낌이다
#배열같은 배열아닌

def addminmuldiv1(a,b):
    return a + b ,a - b , a*b, a/b 

sum = addminmuldiv1(5,4)

print("sum",sum[0])

