def Billboard(txt1,txt2):
    n1 = len(txt1)
    n2 = len(txt2)
    arr = [['0']*n1,['0']*n2]
    top_char = 'A'
    top_idx = 0
    bottom_char = 'A'
    bottom_idx = 0

    if n1>10 or n2>10:
        print("Invalid Input Size")
    else:
        for i in range (n1):
            arr[0][i] = txt1[i]
            if  65 <= ord(txt1[i]) <= 90:
                top_char = txt1[i]
                top_idx = i
        for i in range (n2):
            arr[1][i] = txt2[i]
            if  65 <= ord(txt2[i]) <= 90:
                bottom_char = txt2[i]
                bottom_idx = i
        print("Top Board Start Character: ",top_char)
        print("Top Board Start Index:",top_idx)
        print("Bottom Board Start Character:",bottom_char)
        print("Bottom Board Start Character:",bottom_idx)
        while True:
            press = input("Enter q to quite or any key to continue: ")
            if press == "q" or press == "Q":
                break
            else:
                print("run")
                i = 0
                j = 0
                st = top_idx
                while i < n1-1:
                    print(txt1[st],end="")
                    st -= 1
                    if st <0:
                        st = n1-1
                    i += 1
                print()
                st = 0






# txt1 = input()
# txt2 = input()
txt1 = "giRtfel2th"
txt2 = "rightLeft2"
t = Billboard(txt1,txt2)