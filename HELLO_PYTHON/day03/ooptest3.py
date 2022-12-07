from astropy.modeling.tests.test_model_sets import xx
class Xi :
    def __init__(self):
        self.index_look = 10
    
    def corona(self): 
        self.index_look -= 1
        
class Trump :
    def __init__(self):
        self.money = 2
    def youfire(self):
        self.money += 1
        
class Kim :
    def __init__(self):
        self.nucler = 20
    def  aoji(self):
        self.nucler += 2
        
        
class ParkInSoo(Xi,Trump,Kim):
    
    def __init__(self):
        Xi.__init__(self)
        Trump.__init__(self)
        Kim.__init__(self)
    
if __name__ == '__main__':
    pis = ParkInSoo()
    print("index_look",pis.index_look)
    print("money",pis.money)
    print("nucler",pis.nucler)
        
    pis.corona()
    pis.youfire()
    pis.aoji()
    
    print("index_look",pis.index_look)
    print("money",pis.money)
    print("nucler",pis.nucler)
        