import random
 # 가위바위보를 넣으세요 가위
 # 나 : 가위
 # 컴 : 가위
 # 결과 : 졌음
mine = input("가위/바위/보를 입력하세요")
b = random.random()
 
com = ""
if b > 0.66 :
     com = "가위"
elif b > 0.33 : 
     com = "바위"
else:
     com = "보"
     
result = ""
if mine == "주먹" and com =="가위" or mine == "가위" and com =="보" or mine == "보" and com =="주먹" :
   result = "이김"
elif mine == com :
    result = "비김"
else :
    result = "짐" 

# if com == "가위" and mine == "가위" : result = "비김"
# if com == "가위" and mine == "주먹" : result = "이김"
# if com == "가위" and mine == "보" : result = "짐"

# if com == "주먹" and mine == "주먹" : result = "비김"
# if com == "주먹" and mine == "보" : result = "이김"
# if com == "주먹" and mine == "가위" : result = "짐"

# if com == "보" and mine == "보" : result = "비김"
## if com == "보" and mine == "가위" : result = "이김"
# if com == "보" and mine == "주먹" : result = "짐"


print("mine : ",mine)  
print("com : " ,com)    
print("결과 : " ,result)
    