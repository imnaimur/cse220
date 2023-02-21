a = [10,20,30,40,50]
class Node:
    def __init__(self,x,n):
        self.elem = x
        self.next = n

class LinkedList:
    def __init__(self,a):
        self.head = Node(None,None)
        tail = self.head
        i = 0
        while i < len(a):
            n = Node(a[i],None)
            tail.next = n
            tail = n
            i +=1

            

    def traverse(self):
        tail = self.head
        s = ""
        while tail.next != None:
            if tail.elem != None:
                s += str(tail.elem) + " "
            tail = tail.next
        return s
    def countNode(self):
        i = 0
        tail = self.head
        while tail.next != None:
            tail = tail.next
            i +=1
        return i-1
    def insert(self,elem,idx):
        count = self.countNode()
        tail = self.head
        i = 0
        n = Node(elem,None)
        print(n.elem)
        if 0<=idx< count:
            while i < idx:
                tail = tail.next
                i +=1
            n.next = tail.next
            tail.next = n
            return self.traverse()
        else:
            while i < idx:
                tail = tail.next
                i +=1
            tail.next = n
            print("run")
            return self.traverse()

        # else:
        #     return ("Invalid Index")
h1 = LinkedList(a)
trv = h1.traverse()
count = h1.countNode()
print(trv)
ins = h1.insert(50,3)
print(ins)
ins2=h1.insert(60,6)
print(ins2)