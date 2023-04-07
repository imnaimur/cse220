class KeyIndex:
    def __init__(self,arr) -> None:
        self.max = arr[0]
        self.min = arr[0]
        
        for i in arr:
            if i>self.max:
                self.max = i
            if i< self.min:
                self.min = i
        print("self.min:",self.min)
        print("self.max:",self.max)
        if self.min < 0:
            n = self.max - self.min + 1
            self.k = [0] * n
            for i in arr:
                self.k[i-self.min] +=1
            print(self.k)
        else:
            n = self.max + 1
            self.k = [0] * n
            for i in arr:
                self.k[i] += 1
            print(self.k)

    def search(self,n):
        if n > len(self.k):
            return False
        elif(n < self.min):
            return False
        else:
            if self.k[n] != 0:
                return True
            else:
                return False
            
    def sort(self):
        sortedArrary = []
        n = len(self.k)
        
        if self.min < 0:
            for i in range(n):
                if self.k[i] != 0:
                    sortedArrary += [i+self.min] * self.k[i]
        else:
            for i in range(n):
                if self.k[i] != 0:
                    sortedArrary += [i] * self.k[i]
        return sortedArrary


arr = [3,2,5,2,2,-3]
p = KeyIndex(arr)
print(p.search(-4))
print(p.search(100))
print(p.sort())

