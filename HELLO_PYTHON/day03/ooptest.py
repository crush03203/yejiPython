class Animal :
    def __init__(self):
        print("생성자")
        self.age = 0
        
    def getOlder(self):
        self.age += 1
    
    def _del_(self):
        print("소멸자")
    
# ani = Animal()
# print("1",ani.age)
# ani.getOlder()
# print("1",ani.age)

class Human(Animal):
    def __init__(self):
      super().__init__()
      self.language = 0
    
    def monstouch(self,stroke): 
        self.language += stroke
        
        
#main    
if __name__ == '__main__':
    hum = Human()
    print(hum.language)
    print(hum.age)
    hum.getOlder()
    hum.monstouch(5)
    print(hum.language)
    print(hum.age)