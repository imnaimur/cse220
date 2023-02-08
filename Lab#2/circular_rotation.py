
st = 2
def rotateLeft(txt):
    global st
    n = len(txt)
    i = 0
    arr = []
    while i < n:
        arr += txt[st]
        st -= 1
        if st < 0:
            st = n-1
        i += 1
    return 
txt1 = rotateLeft("giRtfel2th")
print(txt1)
text2 = rotateLeft(txt1)
print(text2)

j = 0
k = 2
while j < k :
    tem = arr[0][0]
    i = top_idx
    while i< n1-1:
        arr[i] = arr[0][i+1]
        i += 1
        # print(arr[i])
    arr[0][n-1] = tem
    j+=1
print(lst)
