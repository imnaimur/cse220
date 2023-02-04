# #left shift k cells

# source=[10,20,30,40,50,60]
# n = len(source)
# k = int(input())

# def shiftLeft(lst,k):
#     for j in range(k):
#         for i in range(n-1):
#             lst[i] = lst[i+1]
#         lst[n-j-1] = 0
#         return(lst)

# prothom = (source,k)
# print(prothom)

# # roate left k cells

# source=[10,20,30,40,50,60]
# n = len(source)
# k = int(input())

# def rotateLeft(lst,k):
#     for j in range(k):
#         temp_storage = lst[0]
#         for i in range(n-1):
#             lst[i] = lst[i+1]
#         lst[n-1]= temp_storage
#         return lst

# ditio = rotateLeft(source,k)
# print(ditio)

# #right shift k cells

# source=[10,20,30,40,50,60]
# n = len(source)
# k = int (input())

# def shiftRight(lst,k):
#     for j in range(k):
#         for i in range(1,n):
#             lst[n-i] = lst[n-1-i]
#         lst[j] = 0
#     return lst

# tritio = shiftRight(source,k)
# print(tritio)


# #right rotate k cells

# source=[10,20,30,40,50,60]
# n = len(source)
# k = int(input())

# def rotateRight(lst,k):
#     for j in range(k):
#         temp_storage= lst[n-1]
#         for i in range(1,n):
#             lst[n-i] = lst[n-1-i]
#         lst[0] = temp_storage
#         return lst

# choturto = rotateRight(source,k)
# print(choturto)


# def remove(lst,idx):
#     edt_arr = []
#     for i in range(n):
#         if i != idx:
#             edt_arr +=[lst[i]]
#     edt_arr += [0]
#     return edt_arr


# source=[10,20,30,40,50,0,0]
# n = len(source)
# idx = int(input())
# ponchom = remove(source,2)
# print(ponchom)

# def removeAll(lst,k):
#     arr = []
#     for i in lst:
#         if i != k:
#             arr +=[i]
#     return arr

# shostho = removeAll(source,idx)

# problem 7

"""Suppose the elements of an array A containing positive integers, denote the weights in kilograms. And we have a beam balance. We want to put the weights on both pans of the balance in such a way that for some index 0 < i < A.length - 1, all values starting from A[0], A[1], upto A[ i - 1], should be on the left pan. And all values starting from A[ i ] upto A[ A.length - 1] should be on the right pan and the left and right pan should be balanced. If such i exists, return true. Else, return false."""

# lst = [10, 3, 1, 2, 10]
# n = len(lst)

# def balance(lst):
#     left_pan = 0
#     right_pan = 0
#     for i in range(1,n):
#         left_pan += lst[i-1]
#         right_pan += lst[n-i]
#     if left_pan == right_pan:
#             return True
#     return False

# shoptom = balance(lst)
# print(shoptom)

def lagestBunch(lst):
    count = 1
    max_elem = []
    n = len(lst)
    for i in range(n-1):
        if lst[i] == lst[i+1]:
            count += 1
        else:
            max_elem +=[count]
            count = 1
    max_elem += [count]
    for i in range(len(max_elem)-1):
        if max_elem[i] > max_elem[i+1]:
            largest = max_elem[i]
        else:
            largest = max_elem[i+1]
    return largest

source = [1, 2, 2, 3, 4, 4, 4]
oshoptom = lagestBunch(source)
print(oshoptom)