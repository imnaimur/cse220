# left rotate and an elem at idx 3
b = [11,12,13,14,15,16,17,28]
n = len(b)
idx = 3
for j in range(1):
    temp = b[j]
    for i in range(idx):
        b[i] = b[i+1]
    b[idx] = temp
print(b)

# right shift append
# # a = []
# for i in b:
#     a += [i]
# now put a number at index 3
# a += [0]
# for i in range(n + 1 - idx):
#     a[n-i] = a[n-i-1]
# a[idx] = 0
# print(a)

#left shift append
elem = 100
a = [0]
for i in b:
    a += [i]
for i in range(idx):
    a[i] = a[i + 1]
a[idx] = elem
b = a
print(b)