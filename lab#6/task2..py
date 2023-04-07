class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next

class LinkedList:
    def __init__(self,arr):
        self.head = Node(arr[0],None)
        tail = self.head
        i = 1
        while i<len(arr):
            n = Node(arr[i],None)
            tail.next = n
            tail = n
            i +=1



def add(head):
    if head == None:
        return 0
    else:
        return head.element + add(head.next)
def printReverse(head):
    if head == None:
        return
    else:
        printReverse(head.next)
        print(head.element)

arr = [10,20,30] 
p = LinkedList(arr)
print(add(p.head))
printReverse(p.head)


def pattern(n):
    if n == 0:
        return
    else:
        pattern(n-1)
        printNum(n)
        print()


def printNum(n):
    if n == 0:
        return
    else:
        printNum(n-1)
        print(n,end="")

pattern(5)


def print_pattern(n, m=1):
    if n == 0:
        return
    else:
        m +=1
        print_pattern(n-1, m)
        print(" "*(m-1), end="")
        print_numbers(1, n)
        print()

def print_numbers(start, end):
    if start <= end:
        print(start, end="")
        print_numbers(start+1, end)

print_pattern(5)


class FinalQ:
    def print_profit(self, array, idx):
        if idx < len(array):
            profit = self.calc_profit(array[idx])
            print(f"Investment: {array[idx]}; Profit: {profit}")
            self.print_profit(array, idx+1)

    def calc_profit(self, investment):
        if investment <= 100000:
            return (investment - 25000) * 0.045
        else:
            profit1 = (investment-100000) * 0.08
            return profit1 + self.calc_profit(100000)

       



array = [25000, 100000, 250000, 350000]
f = FinalQ()
f.print_profit(array, 0)


