#left shift k cells

source=[10,20,30,40,50,60]
n = len(source)
k = int(input())

def shiftLeft(lst,k):
    for j in range(k):
        for i in range(n-1):
            lst[i] = lst[i+1]
        lst[n-j-1] = 0
        return(lst)

prothom = (source,k)
print(prothom)

# roate left k cells

source=[10,20,30,40,50,60]
n = len(source)
k = int(input())

def rotateLeft(lst,k):
    for j in range(k):
        temp_storage = lst[0]
        for i in range(n-1):
            lst[i] = lst[i+1]
        lst[n-1]= temp_storage
        return lst

ditio = rotateLeft(source,k)
print(ditio)

#right shift k cells

source=[10,20,30,40,50,60]
n = len(source)
k = int (input())

def shiftRight(lst,k):
    for j in range(k):
        for i in range(1,n):
            lst[n-i] = lst[n-1-i]
        lst[j] = 0
    return lst

tritio = shiftRight(source,k)
print(tritio)


#right rotate k cells

source=[10,20,30,40,50,60]
n = len(source)
k = int(input())

def rotateRight(lst,k):
    for j in range(k):
        temp_storage= lst[n-1]
        for i in range(1,n):
            lst[n-i] = lst[n-1-i]
        lst[0] = temp_storage
        return lst

choturto = rotateRight(source,k)
print(choturto)


def remove(lst,idx):
    edt_arr = []
    for i in range(n):
        if i != idx:
            edt_arr +=[lst[i]]
    edt_arr += [0]
    return edt_arr


source=[10,20,30,40,50,0,0]
n = len(source)
idx = int(input())
ponchom = remove(source,2)
print(ponchom)

def removeAll(lst,k):
    arr = []
    for i in lst:
        if i != k:
            arr +=[i]
    return arr

shostho = removeAll(source,idx)

