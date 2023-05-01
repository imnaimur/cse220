A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26



class Node:
    def __init__(self,name,next) -> None:
        self.name = name
        self.next = next

def hashTable(arr):
    newArr = [0]*(len(arr))
    for i in arr:
        sum = 0
        for j in i:
            sum += j
        newArr[sum] += [i]
    return newArr

arr = ["CSE","EEE","PHY","ECO"]
# cse = ["tmd",'ssb','rak']
# eee = ['rks','msd','twa']
# phy = ['msb','mit']
# eco = ['shbm','dzk']
# dept = [cse,eee,phy,eco]
d = hashTable(arr)
print(d)
