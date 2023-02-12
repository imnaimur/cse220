class Node:
    def __init__(self,x,y=None,z=None) -> None:
        self.item = x
        self.next = y
        self.prev = z
head = Node(5)
i = 0
while i < 5:
    elem = int(input())
    n = Node(elem)
    head.next = n
    n.prev = head
    n = head
    i += 1
