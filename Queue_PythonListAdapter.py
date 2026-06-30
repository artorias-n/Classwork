# Queue adapter based on Python Lists (objects)
class QueueAdapter:
   def __init__(self):
      self.__storage = list()
   
   def isEmpty(self):
      if len(self.__storage) == 0:
         ans = True
      else:
         ans = False
      return ans
   
   def getCount(self):
      return len(self.__storage)
      
   def enqueue(self, item):
      self.__storage.append(item)
      
   def dequeue(self):
      item = self.__storage.pop(0)
      return item

   def showQueue(self):
      print(self.__storage)

   def __repr__(self):
      print("Queue: ")
      for item in self.__storage:
         print(item, end=", ")

myqueue = QueueAdapter()
myqueue.enqueue("Tyler")
myqueue.enqueue("Mohammed")
myqueue.enqueue("Logan")
myqueue.enqueue("Noah")
myqueue.enqueue("Jason")
myqueue.enqueue("Brandon")
myqueue.enqueue("Ariane")
myqueue.enqueue("Ryan")

myqueue.showQueue()
print(myqueue)

