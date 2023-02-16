# List er mother
class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n

#prepare by me

# To you coding in this cell
class LinkedList:
  
  def __init__(self, a):
  #  Design the constructor based on data type of a. If 'a' is built in python list then
  #  Creates a linked list using the values from the given array. head will refer
  #  to the Node that contains the element from a[0]
  #  Else Sets the value of head. head will refer
  #  to the given LinkedList
  # Hint: Use the type() function to determine the data type of a
    self.head = None
    self.head = Node(a[0],None)
    tail = self.head
    i = 1
    while i < len(a):
        n = Node(a[i],None)
        tail.next = n
        tail = n
        i+=1
    
  
  # Traverse elements in the list.
  # This method is done for you. Do not change this method.
  def traverseList(self):
    s = ''
    temp = self.head
    while temp != None:
      if temp.next != None:
        s += str(temp.element) + " "
      else:
        s += str(temp.element)
      temp = temp.next
    return s
  
  # Count the number of nodes in the list and return the total number
  def countNode(self):
    h = self.head
    count = 0
    i = 0
    while h.next != None:
        n = h.next
        h = n
        count +=1
        i +=1
    return count + 1
  
  # returns the reference of the Node at the given index. For invalid index return None.
  def nodeAt(self, idx):
    i = 0
    count = self.countNode()
    tail = self.head
    if 0<=idx<= count: 
        while i < idx:
            tail = tail.next
            i +=1
        return tail
    else:
        return None
    
    
  
  # returns the element of the Node at the given index. For invalid idx return None.
  def get(self, idx):
    i = 0
    count = self.countNode()
    tail = self.head
    if 0<=idx<= count: 
        while i < idx:
            tail = tail.next
            i +=1
        return tail.element
    else:
        return None
  
  # updates the element of the Node at the given index. 
  # Returns the old element that was replaced. For invalid index return None.
  # parameter: index, element
  def set(self, idx, elem):
    i = 0
    count = self.countNode()
    tail = self.head
    if 0<=idx<= count: 
        while i < idx:
            tail = tail.next
            prev = tail.element
            i +=1
        tail.element = elem
        return prev
    else:
        return None

  # returns the index of the Node containing the given element.
  # if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    # a = self.traverseList()

        i = 0
        count = self.countNode()
        tail = self.head
        while i < count+1:
            if elem == tail.element:
                return i
            n = tail.next
            tail = n
            i +=1
        return -1
  
  # returns true if the element exists in the List, return false otherwise.
  def contains(self, elem):
    i = 0
    count = self.countNode()
    tail = self.head
    while i < count+1:
        if tail.element == elem:
            return True
        tail = tail.next
       
        i += 1
    return False

  # Makes a duplicate copy of the given List. Returns the reference of the duplicate list.
  def copyList(self):
    count = self.countNode()
    tail = self.head
    dupliacte = []
    i = 0
    while i < count:
        dupliacte += [tail.element]
        tail = tail.next
        i += 1
    return dupliacte

  # Makes a reversed copy of the given List. Returns the head reference of the reversed list.
  def reverseList(self):
    reverse = []
    count = self.countNode()
    j = 0
    while j < count:
        i = 0
        tail = self.head
        while i < count-1-j:
            tail = tail.next
            i +=1
        reverse += [tail.element]
        j +=1
    return reverse
  
  # inserts Node containing the given element at the given index
  # Check validity of index. If invalid then print "Invalid Index"
  def insert(self, elem, idx):
    tail = self.head
    i = 0
    count = self.countNode()
    if idx<0 or idx>count:
        print("Invalid Index")
    else:
        if idx == 0:
            n = Node(elem,None)
            n.next = self.head
            self.head = n
        elif idx == count-1:
            while i < idx-1:
                tail = tail.next
                i +=1
            n = Node(elem,None)
            tail.next = n
        else:
            while i < idx-1:
                tail = tail.next
                i +=1
            n = Node(elem,None)
            n.next = tail.next
            tail.next = n
            

                
  # removes Node at the given index. returns element of the removed node.
  # Check validity of index. return None if index is invalid.
  def remove(self, idx):
    count = self.countNode()
    i = 0
    if 0 <= idx <= count-1:
        if idx == 0:
            rem = self.head.element
            self.head = self.head.next
        elif idx == count -1:
            tail = self.head
            while i < idx:
                tail = tail.next
                i +=1
            rem = tail.element
            i = 0
            tail = self.head
            while i < idx-1:
                tail = tail.next
                i+=1
            tail.next = None
        else:
            tail1 = self.head
            tail2 = self.head
            while i <idx-1:
                tail1 = tail1.next
                i +=1
            i = 0
            while i< idx:
                tail2 = tail2.next
                i+=1
            rem = tail2.element
            tail1.next = tail2.next
        return rem

    else:
        return None
        
  
  # Rotates the list to the left by 1 position.
  def rotateLeft(self):
    count = self.countNode()
    i = 0
    tail = self.head
    while i < count-1:
        tail = tail.next
        i +=1
    tail.next = self.head
    self.head = self.head.next
    tail = self.head
    i = 0
    while i < count-1:
        tail = tail.next
        i +=1
    tail.next = None
  # Rotates the list to the right by 1 position.
  def rotateRight(self):
    count = self.countNode()
    i = 0
    tail = self.head
    while i < count-1:
        tail = tail.next
        i +=1
    tail.next = self.head
    self.head = tail
    tail = self.head
    i = 0
    while i < count-1:
        tail = tail.next
        i +=1
    tail.next = None


    # Do not modify this cell. Run this for test your written code.
print("////// Test 01 //////")
a1 = [10, 20, 30, 40]
h1 = LinkedList(a1) # Creates a linked list using the values from the array
# head will refer to the Node that contains the element from a[0]
# print(h1.element)

returned_value = h1.traverseList() # This should return: 10 20 30 40
print(returned_value)
# unittest.output_test(returned_value, '10 20 30 40')
print('------------------------------')
retured_value = h1.countNode() # This should return: 4
# unittest.output_test(retured_value, 4)

print("////// Test 02 //////")
# returns the reference of the Node at the given index. For invalid idx return None.
myNode = h1.nodeAt(1)
retured_value = myNode.element # This should return: 20. In case of invalid index This will generate an Error.
# unittest.output_test(retured_value, 20)
    
print("////// Test 03 //////")
# returns the element of the Node at the given index. For invalid idx return None.
val = h1.get(2)  # This should return: 30. In case of invalid index This will print None.
# unittest.output_test(val, 30)
    
    
print("////// Test 04 //////")
    
# updates the element of the Node at the given index. 
# Returns the old element that was replaced. For invalid index return None.
# parameter: index, element
         
replaced_value = h1.set(1,85) # This should return: 20
# unittest.output_test(replaced_value, 20)
print('------------------------------')
returned_value = h1.traverseList() # This should return: 10 85 30 40
# unittest.output_test(returned_value, '10 85 30 40')
print('------------------------------')
replaced_value = h1.set(15,85) # This should return: None
# unittest.output_test(replaced_value, None)
print('------------------------------')
returned_value = h1.traverseList() # This should return: 10 85 30 40
# unittest.output_test(returned_value, '10 85 30 40')
    
print("////// Test 05 //////")
# returns the index of the Node containing the given element.
# if the element does not exist in the List, return -1.
index = h1.indexOf(40) # This should return: 3. In case of element that doesn't exists in the list this will print -1.
# unittest.output_test(index, 3)
    
print("////// Test 06 //////")
# returns true if the element exists in the List, return false otherwise.
ask = h1.contains(40)  # This should return: True.
# unittest.output_test(ask, True)
    
    
print("////// Test 07 //////")
a2 = [10,20,30,40,50,60,70]
h2 = LinkedList(a2) # uses theconstructor where a is an built in list
returned_value = h2.traverseList() # This should return: 10 20 30 40 50 60 70  
# unittest.output_test(returned_value, '10 20 30 40 50 60 70')
print('------------------------------')
# Makes a duplicate copy of the given List. Returns the head reference of the duplicate list.
copyH=h2.copyList() # Head node reference of the duplicate list
h3 = LinkedList(copyH) # uses the constructor where a is head of a linkedlist 
returned_value = h3.traverseList() # This should return: 10 20 30 40 50 60 70  
# unittest.output_test(returned_value, '10 20 30 40 50 60 70')
    
print("////// Test 08 //////")
a4 = [10,20,30,40,50]
h4 = LinkedList(a4) # uses the constructor where a is an built in list
returned_value = h4.traverseList() # This should return: 10 20 30 40 50  
# unittest.output_test(returned_value, '10 20 30 40 50')
print('------------------------------')
# Makes a reversed copy of the given List. Returns the head reference of the reversed list.
revH=h4.reverseList() # Head node reference of the reversed list
h5 = LinkedList(revH) # uses the constructor where a is head of a linkedlist 
returned_value = h5.traverseList() # This should return: 50 40 30 20 10  
# unittest.output_test(returned_value, '50 40 30 20 10')
    
print("////// Test 09 //////")
a6 = [10,20,30,40]
h6 = LinkedList(a6) # uses theconstructor where a is an built in list
returned_value = h6.traverseList() # This should return: 10 20 30 40  
# unittest.output_test(returned_value, '10 20 30 40')
print('------------------------------')   
# inserts Node containing the given element at the given index. Check validity of index.
h6.insert(85,0)
returned_value = h6.traverseList() # This should return: 85 10 20 30 40  
# unittest.output_test(returned_value, '85 10 20 30 40')
print('------------------------------')
h6.insert(95,3)
returned_value = h6.traverseList() # This should return: 85 10 20 95 30 40  
# unittest.output_test(returned_value, '85 10 20 95 30 40')
print('------------------------------')
h6.insert(75,6)
returned_value = h6.traverseList() # This should return: 85 10 20 95 30 40 75
# unittest.output_test(returned_value, '85 10 20 95 30 40 75')
    
    
    
print("////// Test 10 //////")
a7 = [10,20,30,40,50,60,70]
h7 = LinkedList(a7) # uses theconstructor where a is an built in list
returned_value = h7.traverseList() # This should return: 10 20 30 40 50 60 70  
# unittest.output_test(returned_value, '10 20 30 40 50 60 70')
print('------------------------------')  
# removes Node at the given index. returns element of the removed node.
# Check validity of index. return None if index is invalid.
    
removed_element = h7.remove(0) # This should return: 10
# unittest.output_test(removed_element, '10')
print('------------------------------')
returned_value = h7.traverseList() # This should return: 20 30 40 50 60 70
# unittest.output_test(returned_value, '20 30 40 50 60 70')
print('------------------------------')
removed_element = h7.remove(3) # This should return: 50
# unittest.output_test(removed_element, '50')
print('------------------------------')
returned_value = h7.traverseList() # This should return: 20 30 40 60 70 
# unittest.output_test(returned_value, '20 30 40 60 70')
print('------------------------------')
removed_element = h7.remove(4) # This should return: 70
# unittest.output_test(removed_element, '70')
print('------------------------------')
returned_value = h7.traverseList() # This should return: 20 30 40 60 
# unittest.output_test(returned_value, '20 30 40 60')
    
    
print("////// Test 11 //////")
a8 = [10,20,30,40]
h8 = LinkedList(a8) # uses theconstructor where a is an built in list
returned_value = h8.traverseList() # This should return: 10 20 30 40  
# unittest.output_test(returned_value, '10 20 30 40')
print('------------------------------')    
# Rotates the list to the left by 1 position.
h8.rotateLeft()
returned_value = h8.traverseList() # This should return: 20 30 40 10  
# unittest.output_test(returned_value, '20 30 40 10')
      
print("////// Test 12 //////")
a9 = [10,20,30,40]
h9 = LinkedList(a9) # uses the constructor where a is an built in list
returned_value = h9.traverseList() # This should return: 10 20 30 40
# unittest.output_test(returned_value, '10 20 30 40')  
print('------------------------------')    
# Rotates the list to the right by 1 position.
h9.rotateRight()
returned_value = h9.traverseList() # This should return: 40 10 20 30
# unittest.output_test(returned_value, '40 10 20 30')