class Queue:
    def __init__(self):
        self.__storage=list()
    
    def isempty(self):
        if len(self.__storage)==0:
            ans=True
        else:
            ans=False
        return ans
    
    def getcount(self):
        return len(self.__storage)
        
    def enqueue(self,x):
        self.__storage.append(x)
        
    def dequeue(self):
            item=self.__storage.pop(0)
            return item
            
test=Queue()
print(test.isempty())
test.enqueue(0)
test.enqueue(1)
test.enqueue(2)
test.enqueue(3)
test.enqueue(4)
test.enqueue(5)
print(test.getcount())
print(test.dequeue())
print(test.getcount())