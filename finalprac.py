
#--------Key Index Search ----------#

# class KeyIndex:
#     def __init__(self,arr) -> None:
#         self.max = arr[0]
#         self.min = arr[0]
#         for i in arr:
#             if i > self.max:
#                 self.max = i
#             if i < self.min:
#                 self.min = i
#         if self.min < 0:
#             n = self.max - self.min + 1
#             self.k = [0] * n
#             for i in arr:
#                 self.k[i - self.min] += 1
#         else:
#             n = self.max + 1
#             self.k = [0] * n
#             for i in arr:
#                 self.k[i] += 1
#         # print(self.min,"\n",self.max,"\n",self.k)


#     def search(self,n):
#         if n < self.min or n > len(self.k):
#             return False
#         else:
#             if self.min < 0:
#                 if (n - self.min< len(self.k)):
#                     if self.k[n-self.min] != 0:
#                         return True
#                 else:
#                     return False
#             elif self.k[n] != 0:
#                 return True
#             else:
#                 return False
#     def sorting(self):
#         sortedArrary = []
#         n = len(self.k)
        
#         if self.min < 0:
#             for i in range(n):
#                 if self.k[i] != 0:
#                     sortedArrary += [i+self.min] * self.k[i]
#         else:
#             for i in range(n):
#                 if self.k[i] != 0:
#                     sortedArrary += [i] * self.k[i]
#         return sortedArrary
            

# arr = [3,2,5,2,2,-3]
# test = KeyIndex(arr)
# print(test.search(7))
# print(test.sorting())


#----------------- Recursion -----------------#


class Node:
    def __init__(self,elem,next) -> None:
        self.next = next
        self.elem = elem


def buildList(arr,i=0):
    if i == len(arr):
        return
    root = Node(arr[i],None)
    i +=1
    root.next = buildList(arr,i)
    return root

arr = [10,20,30]
p = buildList(arr)
while p != None:
    print(p.elem)
    p = p.next


z = buildList(arr)
def printRev(root):
    if root == None:
        return
    printRev(root.next)
    print(root.elem)

printRev(z)