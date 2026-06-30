class Person:
    
    def __init__(self,hungry,thirsty,tired,fn,ln,dob,addr,ssn,ms,intoxicated,partnerfn,partnerln):
        self.__hungry=hungry
        self.__thirsty=thirsty
        self.__tired=tired
        self.fn=fn
        self.ln=ln
        self.dob=dob
        self.__addr=addr
        self.ssn=ssn
        self.ms=ms
        self.__intoxicated=intoxicated
        self.partnerfn=partnerfn
        self.partnerln=partnerln
    
    def __del__(self):
        print(self.fn+" "+self.ln+" was taken out back")

    def eat(self):
        self.__hungry=False
    
    def drink(self,*x):
        if len(x)>0:
            if x!="alcohol" and x!="Alcohol":
                self.__thirsty=False
        elif len(x)==0:
            self.__intoxicated=True
        
    def sleep(self):
        self.__tired=False
    
    def work(self):
        self.__tired=True
        self.__thirsty=True
        self.__hungry=True
    
    def move(self):
        self.__addr=input("Where to: ")
        
    def  set_name(self):
        self.fn=input("First Name: ")
        self.ln=input("Last Name: ")
       
    def  set_dob(self):
        self.dob=input("Date of birth: ")
        
    def  set_address(self):
        self.__addr=input("New address: ")
        
    def  set_ssn(self):
        self.ssn=input("New SSN: ")
        
    def set_marital_status(self):
        self.ms=input("Marital status: ")
    
    def get_info(self):
        print(self.fn)
        print(self.ln)
        print(self.dob)
        print(self.__hungry)
        print(self.__thirsty)
        print(self.__tired)
        print(self.__addr)
        print(self.ssn)
        print(self.ms)
        print(self.__intoxicated)
        print(self.partnerfn)
        print(self.partnerln)

class Student(Person):
    def __init__(self,hungry,thirsty,tired,fn,ln,dob,addr,ssn,ms,intoxicated,partnerfn,partnerln,grad_year,s_id,major,athlete,degree,knowledge):
        super().__init__(hungry,thirsty,tired,fn,ln,dob,addr,ssn,ms,intoxicated,partnerfn,partnerln)
        self.grad_year=grad_year
        self.s_id=s_id
        self.major=major
        self.athlete=athlete
        self.degree=degree
        self.__knowledge=knowledge
    
    def study(self):
        self.__knowledge=self.__knowledge+5
    
    
    def eat(self):
        self.__richie_market_place()
    
    def __richie_market_place(self):
        print(self.fn+" has gone to Richie Market Place")
        super().eat()
    
    def drink(self,*x):
        self.__richie_Market_place(*x)
    
    def __richie_Market_place(self,*x):
        print(self.fn+" has gone to Richie Market Place")
        super().drink(*x)
    
    def sleep(self):
        self.__dorm()
    
    def __dorm(self):
        print(self.fn+" has gone to the dorms")
        super().sleep()
    
    def get_info(self):
        super().get_info()
        print(self.grad_year)
        print(self.s_id)
        print(self.major)
        print(self.athlete)
        print(self.degree)
        print(self.__knowledge)
  
p1=Person(True,True,True,"Abraham","lincoln","Jan 11 2003","Adrian",999999999,"Married",False,"Mary","Todd")
p1.get_info()
p1.eat()
p1.drink("Water")
p1.sleep()
p1.move()
p1.set_name()
p1.set_dob()
p1.set_ssn()
p1.set_marital_status()
p1.get_info()
p1.set_address()
p1.work()
p1.drink()
p1.get_info()
p2=Student(True,True,True,"John Paul","Jones","Dec 23 1997","Atlantic",888888888,"Married",False,"Freya","Campbell",2026,55555,"Computer Science",False,"Bachelor's",10)
p2.get_info()
p2.eat()
p2.drink("water")
p2.sleep
p2.study()
p2.get_info()