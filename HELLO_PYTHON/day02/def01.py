def add(a,b):
    return a + b 

def minus(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

sum = add(5,4)
min = minus(5,4)
mul = multiply(5,4)
div = divide(5,4)


print("sum",sum)
print("min",min)
print("mul",mul)
print("div",div)

#def divide(a,b):
#    return a/b 를 밑에다가 쓰면 안됨
#why ? 인터프리터 언어라서 위에서메모리 구성이 안되어있기 때문