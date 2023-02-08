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

        # so that if later i change stating idx it should reamin change
        st1 = top_idx
        st2 = bottom_idx
        string_top = ""
        string_bottom = ""
        i = 0
        controler = 0
        if controler > n1:
            controler = 0



        while True:

            press = input("Enter q to quite or any key to continue: ")
            if press == "q" or press == "Q":
                break


            else:
                i = 0
                while i < n1:
                    string_top += arr[0][st1]
                    st1 -=1
                    if st1 < 0:
                        st1 = n1-1
                    print(string_top[i],end="")
                    i +=1
                print()
      
                i = 0
                while i < n1:
                    string_bottom += arr[1][st2]
                    st2+=1
                    if st2 >n2-1:
                        st2 = 0
                    print(string_bottom[i],end="")
                    i += 1
                print()
                





# txt1 = input()
# txt2 = input()
txt1 = "giRtfel2th"
txt2 = "rightLeft2"
t = Billboard(txt1,txt2)