# add a an element in index no 4 right shift


# b = [8,9,2,4,5,1,2,3]
# elem = 6
# idx = 4
# i = 1
# n = len(b)
# while i < n - idx:
#     b[n-i] = b[n-i-1]
#     i+=1
# b[idx] = elem
# print(b)

#left shifting append

b = [8,9,2,4,5,1,2,3]
elem = 10
idx = 6
i = 0
n = len(b)
while i < idx:
    b[i] = b[i+1]
    i += 1
b[idx] = elem
print(b)
