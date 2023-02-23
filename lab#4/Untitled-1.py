class Node:
  def __init__(self, e, n, p):
    self.element = e
    self.next = n
    self.prev = p

class DoublyList:
  
  def __init__(self, a):
  # Creates a Non Dummy Headed Circular Doubly Linked List using the values from the given array a.
    self.head = Node(a[0],None,None)
    tail = self.head
    i = 1
    while i < len(a):
        n = Node(a[i],None,tail)
        tail.next = n
        tail = tail.next
        i +=1
    tail.next = self.head
    self.head.prev = tail


    
    pass # Remove this line
  
  # Counts the number of Nodes in the list and return the number
  def countNode(self):
    tail = self.head
    i = 0
    while tail.next != self.head:
        tail = tail.next
        i +=1
    return i+1
  
  # prints the elements in the list
  def forwardprint(self):
    # To Do
    tail = self.head
    count = self.countNode()
    s = ""
    i = 0
    while tail.next != self.head:
        s += str(tail.element) + " "
        tail = tail.next
    s += str(tail.element)
    print(s)

  # prints the elements in the list backward
  def backwardprint(self):
    count = self.countNode()
    tail = self.head
    i = 0
    s = ""
    while i < count:
        tail = tail.prev
        s += str(tail.element) + " "
        i +=1
    print(s)

  # returns the reference of the at the given index. For invalid index return None.
  def nodeAt(self, idx):
    tail = self.head
    i = 0
    while i < idx:
        tail = tail.next
        i +=1
    return tail
  
  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    tail = self.head
    i = 0
    while True:
        if elem == tail.element:
            return i
        tail = tail.next
        i +=1
        return None

  # inserts containing the given element at the given index Check validity of index. 
  def insert(self, elem, idx):
    tail = self.head
    n = Node(elem,None,None)
    i = 0
    count = self.countNode()
    if idx<0 or idx>count:
        print("Invalid Index")
    else:
        if idx == 0:
            while tail.next != self.head:
                tail = tail.next
            tail.next = n
            n.next = self.head
            n.prev = tail
            self.head.prev = n
            self.head = n
            
        elif idx == count:
            while tail.next != self.head:
                tail= tail.next
            tail.next = n
            n.prev = tail
            self.head.prev = n
            n.next = self.head
        else:
            while i < idx-1:
                tail = tail.next
                i +=1
            tail2 = self.head
            i = 0
            while i < idx:
                tail2 = tail2.next
                i +=1
            tail.next = n
            n.prev= tail
            n.next = tail2
            tail2.prev = n
  # removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
  def remove(self, idx):
    count = self.countNode()
    tail = self.head
    tail2 = self.head
    i = 0
    if 0 <= idx <= count-1:
        if idx == 0:
            while tail.next != self.head:
                tail = tail.next
            tail.next = self.head.next
            rem = self.head.element
            self.head = self.head.next
            self.head.prev = tail
        elif idx == count -1:
            while i < idx-1:
                tail = tail.next
                i +=1
            rem = tail.next
            rem = rem.element
            tail.next = self.head
            self.head.prev = tail
        else:
            while i < idx-1:
                tail = tail.next
                i +=1
            i = 0
            while i < idx:
                tail2 = tail2.next
                i +=1
            rem = tail2.element
            tail2 = tail2.next
            tail.next = tail2
            tail2.prev = tail
            
            
        return str(rem)
    else:
        return None



print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array
h1.forwardprint() # This should print: 10,20,30,40. 
h1.backwardprint() # This should print: 40,30,20,10. 
print(h1.countNode()) # This should print: 4


print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"


print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index) # This should print: 3. In case of element that 
#doesn't exists in the list this will print -1.



print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40.  

# inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40. 
h2.backwardprint() # This should print: 40,30,20,10,85.

print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.  
h2.backwardprint() # This should print: 40,30,95,20,10,80.  

print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75. 
h2.backwardprint() # This should print: 75,40,30,95,20,10,85. 


print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70.  

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.  
h3.backwardprint() # This should print: 70,60,50,40,30,20.  
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.  
h3.backwardprint() # This should print: 70,60,40,30,20.  
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60. 
h3.backwardprint() # This should print: 60,40,30,20.