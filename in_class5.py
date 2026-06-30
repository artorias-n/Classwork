class Person:
    
    def __init__(self,fname,lname):
        self.__hungry=False
        self.__thirsty=False
        self.__tired=False
        self.__drunk=False
        self.__ms="S"
        self.__partner=""
        self.fname=fname
        self.lname=lname
    
    def ishungry(self):
        return self.__hungry
        
    
    def eat(self):
        self.__hungry=False
    
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
  
    def isdrunk(self):
        return self.__drunk
    
    #def __del__(self):
     #   print(self.fname+" "+self.lname+" was taken out back")
    
    def __add__(self,other):
        if self.__ms=="S" and other.__ms=="S":
            self.__ms="M"
            other.__ms="M"
            self.__partner=other.fname+" "+other.lname
            other.__partner=self.fname+" "+self.lname
            return self.lname+other.lname
        elif self.__ms=="M" and other.__ms=="M":
            print(self.fname+" is already married to "+self.__partner)
            print(other.fname+" is already married to "+other.__partner)
        elif self.__ms=="M":
            print(self.fname+" is already married to "+self.__partner)
        elif other.__ms=="M":
            print(other.fname+" is already married to "+other.__partner)
    
    def ismarried(self):
        if self.__ms=="M":
            print(self.fname+" is married to "+self.__partner)
        else:
            print(self.fname+" is not married")

p1=Person("Peter","Parker")
p2=Person("Mary","Jane")
p1.ismarried()
p2.ismarried()
hh=p1+p2
print(hh)
p1.ismarried()
p2.ismarried()