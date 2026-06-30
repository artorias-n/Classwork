class Person:
    
    def __init__(self):
        self.__hungry=True
        self.__thirsty=True
        self.__tired=True
        self.__drunk=False
        self.name="John doe"
    
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
    
    def __del__(self):
        print(self.name+" was taken out back")

class Student(Person):
    def __init__(self,gradyear,sid,major,athlete,degree):
        super(Student, self).__init__()
        self.__gradyear=gradyear
        self.__sid=sid
        self.__major=major
        self.__athlete=athlete
        self.__degree=degree
    
    def study(self):
        print("Under development")
    
    def go_to_class(self):
        print("Under development")
    
    def eat(self):
        print("Under development")
    
    def do_hw(self):
        print("Under development")
    
    def sleep(self):
        print("Under development")
    
def df():
    p1=Student(2026,120270,"Comp. Science",False,"Bachelor's")
    print("Function Terminating")

df()
