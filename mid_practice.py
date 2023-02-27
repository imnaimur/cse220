class LinearArray:
    def __init__(self,arr,x) -> None:
        self.arr= arr
        self.n = len(arr)
        self.size = x
    
    def lefShift(self,k=1):
        for j in range(k):
            for i in range(len(self.arr)-1):
                self.arr[i] = self.arr[i +1]
            self.arr[self.n -1] = 0
        print(self.arr)


    def rightShift(self,k=1):
        for j in range(k):
            for i in range(1,self.n):
                self.arr[self.n-i] = self.arr[self.n -1 -i]
            self.arr[0] = 0
        print(self.arr)


    def leftRotatte(self,k=1):
        for j in range(k):
            temp = self.arr[0]
            for i in range(self.n-1):
                self.arr[i] = self.arr[i + 1]
            self.arr[self.n-1] = temp
        print(self.arr)

    def rightRotate(self,k = 1):
        for j in range(k):
            temp = self.arr[self.n-1]
            for i in range(1,self.n):
                self.arr[self.n-i] = self.arr[self.n -1 -i]
            self.arr[0] = temp
        print(self.arr)
    
    def resize(self,k=1):
        b = []
        for i in self.arr:
            b +=[i]
        for j in range(k):
            b += [0]
        self.arr = b
        self.size +=1
    def insert(self,itm,idx):
        if 0 in self.arr:
            pass
        else:
            self.resize()


        if idx == 0:
            self.rightShift()
            self.arr[0] = itm
        if idx == self.n-1:
                self.arr[idx]=[itm]
        else:
            for i in range(idx):
                if i == idx-1:
                    self.arr +=[itm]
        print(self.arr)
        
class CircularArray:
    def __init__(self) -> None:
        pass




arz = [1,2,3,4,5]
test = LinearArray(arz,5)
# test.lefShift()
# test.rightShift()
# test.leftRotatte(2)
# test.rightRotate(2)
test.insert(10,0)
