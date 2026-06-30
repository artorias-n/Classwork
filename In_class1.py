class Person:
    def __init__(self, fn, ln, dob, addrr, ssn, hungry, thirsty, tired, ms):
        self.fname=fn
        self.lname=ln
        self.dob=dob
        self.addrr=addrr
        self.ssn=ssn
        self.__hungry=hungry
        self.__thirsty=thirsty
        self.__tired=tired
        self.__ms=ms
    
    def ishungry(self):
        if self.__hungry==False:
            print(self.fname+ " is not hungry")
        if self.__hungry==True:
            print(self.fname+ " is hungry")
    
    def eat(self):
        self.__hungry=False
    
    def faminished(self):
        self.__hungry=True
    
    def isthirsty(self):
        if self.__thirsty==False:
            print(self.fname+ " is not thirsty")
        if self.__thirsty==True:
            print(self.fname+ " is thirsty")
    
    def drink(self):
        self.__thirsty=False
    
    def dehydrate(self):
        self.__thirsty=True
        
    def istired(self):
        if self.__tired==False:
            print(self.fname+ " is not tired")
        if self.__tired==True:
            print(self.fname+ " is tired")
    
    def sleep(self):
        self.__tired=False
    
    def exhausted(self):
        self.__tired=True
    
    def viewssn(self):
        print(self.ssn)
    


p1=Person("Loki", "Odinson",0o07122003,"adrian",88888888, False,False,False, "single")
print(p1.fname)
print(p1.lname)
p1.ishungry()
p1.faminished()
p1.ishungry()
p1.eat()
p1.ishungry()
p1.viewssn()
p1.istired()
p1.exhausted()
p1.istired()
p1.sleep()
p1.istired()
p1.isthirsty()
p1.dehydrate()
p1.isthirsty()
p1.drink()
p1.isthirsty()
