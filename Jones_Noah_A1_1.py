class Person:
    
    __hungry=True
    __thirsty=True
    __tired=True
    __fn="Bruce"
    __ln="Wayne"
    __dob="10-11-2003"
    __addr="adrian"
    __ssn=999999999
    __ms="single"
    

    def eat(self):
        self.__hungry=False
    
    def drink(self):
        self.__thirsty=False
        
    def sleep(self):
        self.__tired=False
    
    def work(self):
        self.__tired=True
        self.__thirsty=True
        self.__hungry=True
    
    def move(self):
        self.__addr=input("Where to: ")
        
    def  set_name(self):
        self.__fn=input("First Name: ")
        self.__ln=input("Last Name: ")
       
    def  set_dob(self):
        self.__dob=input("Date of birth: ")
        
    def  set_address(self):
        self.__addr=input("New address: ")
        
    def  set_ssn(self):
        self.__ssn=input("New SSN: ")
        
    def set_marital_status(self):
        self.__ms=input("Marital status: ")
    
    def get_info(self):
        print(self.__fn)
        print(self.__ln)
        print(self.__dob)
        print(self.__hungry)
        print(self.__thirsty)
        print(self.__tired)
        print(self.__addr)
        print(self.__ssn)
        print(self.__ms)
  
p1=Person()
p1.get_info()
p1.eat()
p1.drink()
p1.sleep()
p1.move()
p1.set_name()
p1.set_dob()
p1.set_ssn()
p1.set_marital_status()
p1.get_info()
p1.set_address()
p1.work()
p1.get_info()