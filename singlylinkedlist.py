class Student:
    def __init__(self, fn, ln, dob, s_id):
        self.__fn=fn
        self.__ln=ln
        self.__dob=dob
        self.__s_id=s_id
        
class Node:
    def __init__(self, item):
        self.ref=item
        self.nextn=None




class Sll:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__count=0
    
    def getCount(self):
        return self.count
        
    def isEmpty(Self):
        if self.head==None:
            ans=True
        else:
            ans=False
        return ans
    
    def insertAtHead(self, item):
        pass
        
    def insertAtTail(self, item):
        node = Node(item)
        last_node=self.__tail
        last_node.nextn=node
        self.__tail=node
        self.__count+=1
        
    def insert(self, s_id, item):
        new_node=Node(item)
        node = self.__head
        while node.ref.s_id != s_id and node.nextn != None:
            node = node.nextn
        if node.nextn !+ None:
            # attach the new node after node
            new_node.nextn = node.nextn
            node.nextn = new_node
            self.__count+=1
            success = True
        
        
    def removeHead(self):
        pass
        
    def removeTail(self):
        pass

class 



