class HashTable:
    def hashCal(self,string):
        vowel = ['A','E','I','O','U']
        cons = 0
        digit = 0
    
        for i in string:
            if i not in vowel:
                if 65<ord(i)<97:
                    cons += 1
                else:
                        digit += int(i)
        idx = (cons*24 + digit ) % 9
        return idx
    def linearProbing(self,arr):
        self.k = [0] * len(arr)
        for i in arr:
            idx = self.hashCal(i)
            x = self.index(idx) #funtion
            self.k[x] = i
        return self.k 
    
    #function for index detecting
    def index(self,idx):
        if idx > len(self.k)-1:
            idx = 0
        if self.k[idx] == 0:
            return idx
        else:
            idx += 1
            return self.index(idx)

        
        

    
arr_text = ["ABWR3561","LKGO14522","SDHG14563","ABGO14564","ABNF6JDN65","NDA103216","P3N3MA3C7","7D8A8Q8I8","ABEW04659"]
p = HashTable()
print(p.hashCal(arr_text[0]))
print(p.linearProbing(arr_text))



     