#left shift k cells

source=[10,20,30,40,50,60]
n = len(source)
k = int(input())
for j in range(k):
    for i in range(n-1):
        source[i] = source[i+1]
    source[n-j-1] = 0
print(source)

# roate left k cells

source=[10,20,30,40,50,60]

for j in range(k):
    temp_storage = source[0]
    for i in range(n-1):
        source[i] = source[i+1]
    source[n-1]= temp_storage

print(source)
