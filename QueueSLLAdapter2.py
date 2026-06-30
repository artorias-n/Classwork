class Student:
   def __init__(self, fn, ln, dob, s_id):
      self._fn = fn
      self._ln = ln
      self._dob = dob
      self._s_id = s_id

class Node:
   def __init__(self, item):
      self.ref = item
      self.nextn = None

class Sll:
   def __init__(self):
      self.__head = None
      self.__tail = None
      self.__count = 0

   def getCount(self):
      return self.__count

   def isEmpty(self):
      if self.__head == None:
         ans = True
      else:
         ans = False
      return ans
   
   def insertAtHead(self, node):
   # Insert a node at the head of the linked list
      if self.__head == None:
         self.__head = node
         self.__tail = node
         node.nextn = None
      else:
         first_node = self.__head
         node.nextn = first_node
         self.__head = node      
      self.__count += 1
   
   def insertAtTail(self, node):
      #node = Node(item)
      if self.__tail == None:
         self.insertAtHead(node)
      else:
          last_node = self.__tail
          last_node.nextn = node
          self.__tail = node
      self.__count += 1

   def insert(self, prev_node, node):
   # If prev_node is not found in the LL, node is inserted
   # return success as false
      success = False
      
      node_var = self.__head
      while node_var != prev_node and node_var.nextn != None:
         node = node.nextn
      if node_var == prev_node:
         # attach the new node after node
         node.nextn = node_var.nextn
         node_var.nextn = node
         self.__count += 1
         success = True

      return success
      
   def removeHead(self):
      pass

   def removeTail(self):
      pass

   def remove(self):
      pass



QueueSllAdapt:
   def __init__(self):
      self.storage = Sll()



# Main program
s1 = Student("John", "Wayne", "2000-01-01", 12343456)
n1 = Node(s1)
s2 = Student("John", "Wayne", "2000-01-01", 12343456)
n2 = Node(s2)
s3 = Student("John", "Wayne", "2000-01-01", 12343456)
n3 = Node(s3)
s4 = Student("John", "Wayne", "2000-01-01", 12343456)
n4 = Node(s4)
s5 = Student("John", "Wayne", "2000-01-01", 12343456)
n5 = Node(s5)
s6 = Student("John", "Wayne", "2000-01-01", 12343456)
n6 = Node(s6)

sll = Sll()
sll(
