#첫번째수를 넣으세요 1
#두번째수를 넣으세요 10
#1에서 10까지 합은 55입니다

a = int(input("첫번째 수를 넣으세요 "))
b = int(input("두번째 수를 넣으세요 "))

sum = 0
for i in range(a,b+1):
    sum += i
print("{}에서 {}까지 합은 {}입니다.".format(a,b,sum))

#a = int(input("첫번째 수를 넣으세요 "))
#b = int(input("두번째 수를 넣으세요 "))
#aa = int(a)
#bb = int(b)
#print(aa,bb)

#sum = 0
#for i int range(aa, bb+1) :
#    sum += i
    
#print("{}에서 {}까지 합은 {}입니다".format(aa,bb,sum))