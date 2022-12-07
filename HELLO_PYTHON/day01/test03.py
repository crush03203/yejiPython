import random
 # 홀/짝을 넣으세요 홀
 # 나 : 홀
 # 컴 : 짝
 # 결과ㅣ 졌음

print("홀/짝을 입력하세요")
a = input("나 : ")
b = random.randint(0,1)
com = ""
if b == 0 :
    com = "홀"
elif b == 1 :
    com = "짝"
print("컴퓨터: " + com)

result = ""
if com == a :
    print("결과 : 이김 ")
else :
    print("결과 : 짐 ")
