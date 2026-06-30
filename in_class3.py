class Person:
    
    def __init__(self, thirsty, hungry, tired,drunk):
        self.__hungry=hungry
        self.__thirsty=thirsty
        self.__tired=tired
        self.__drunk=drunk
        
    
    def ishungry(self):
        return self.__hungry
        
    
    def eat(self):
        self.__prepare_food()
    
    def faminished(self):
        self.__hungry=True
    
    def isthirsty(self):
        return self.__thirsty
        
    def drink(self,*x):
        if len(x)>0:
            if x!="alcohol" and x!="Alcohol":
                self.__thirsty=False
        elif len(x)==0:
            self.__drunk=True
            
    
    def dehydrate(self):
        self.__thirsty=True
        
    def istired(self):
        return self.__tired
    
    def sleep(self):
        self.__tired=False
    
    def exhausted(self):
        self.__tired=True
    def __prepare_food(self):
            self.__serve()
        
    def __serve(self):
            self.__hungry=False
            
    def isdrunk(self):
            return self.__drunk


p1=Person(True,True,True,False)
print(p1.isthirsty())
print(p1.isdrunk())
p1.drink()
print(p1.isdrunk())
print(p1.isthirsty())
p1.drink("water")
print(p1.isthirsty())