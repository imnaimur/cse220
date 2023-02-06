
def printReverse(lst,st,size):
    n = len(lst)
    last = (st+size-1)%n
    i = 0
    while i<size:
        if last == 0:
            last = n-1
        print(lst[last-i])
        i +=1



arr = [3,4,5,0,1,2]
t = printReverse(arr,2,5)