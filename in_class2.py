class Person:
    
    __fname=""
    __lname=""
    __dob=""
    print("Person created")
    def set_person(self):
        self.__fname=input(" ")
        self.__lname=input(" ")
        self.__dob=input(" ")
    
    def print(self):
        print(self.__fname)
        print(self.__lname)
        print(self.__dob)
    
    def set_fname(self):
        self.__fname=input(" ")
    
    def set_lname(self):
        self.__lname=input(" ")
    
    def set_dob(self):
        self.__dob=input(" ")


    


p1=Person()
p1.set_person()
p1.print()