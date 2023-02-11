class List:
    def __init__(self,x,y=None,z=None) -> None:
        self.item = x
        self.next = y
        self.prev = z
head = List(5)
i = 0
while i < 5:
    elem = int(input())
    n = List(elem)
    head.next = n
    n.prev = head
    n = head
    i += 1
