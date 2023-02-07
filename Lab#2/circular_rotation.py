

def rotateLeft(txt,st):
    n = len(txt)
    i = 0
    arr = []
    while i < n:
        arr += txt[st]
        st -= 1
        if st < 0:
            st = n-1
        i += 1
    return arr
txt1 = rotateLeft("giRtfel2th",2)
print(txt1)
text2 = rotateLeft(txt1,0)
print(text2)
