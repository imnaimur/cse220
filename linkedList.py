class Node:
    def __init__(self,elem) -> None:
        self.elem = elem
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self,arr) -> None:
        self.head = Node(arr[0])
        tail = self.head
        for i in range(1,len(arr)):
            n = Node(arr[i])
            tail.next = n
            n.prev = tail
            tail = n
    def traverseList(self):
        tail = self.head
        s = ""
        while tail.next != None:
            if tail.next != None:
                s += str(tail.elem) + " "
            else:
                s += str(tail.elem)
            tail = tail.next
        s += str(tail.elem)
        print(s)


    def countNode(self):
        tail = self.head
        count = 1
        while tail.next != None:
            count +=1
            tail = tail.next
        print(count)

    def backward(self):
        s = ''
        tail = self.head
        while tail.prev != self.head:

a = [10,20,30,40,50]
h1 = LinkedList(a)
h1.traverseList()
h1.countNode()