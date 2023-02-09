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
            if  "A" <= txt1[i] <= "Z":
                top_char = txt1[i]
                top_idx = i
        for i in range (n2):
            arr[1][i] = txt2[i]
            if  "A" <= txt2[i] <= "Z":
                bottom_char = txt2[i]
                bottom_idx = i
        print("Top Board Start Character: ",top_char)
        print("Top Board Start Index:",top_idx)
        print("Bottom Board Start Character:",bottom_char)
        print("Bottom Board Start Character:",bottom_idx)

    #----------Variable desk for rearranging string---------#


        st1 = top_idx
        st2 = bottom_idx
        string_top = []
        string_bottom = []
        i = 0
        controler = 0


    #-----------------start infinite loop------------#
    
        while True:

            press = input("Enter q/Q to quite or any key to continue: ")
            if press == "q" or press == "Q":
                break


            else:

    #-----------------Top String Work-----------------#

                i = 0
                if controler ==0:
                    while i < n1:
                        string_top += [arr[0][st1]]
                        st1 -=1
                        if st1 < 0:
                            st1 = n1-1
                        print(string_top[i],end="")
                        i += 1
                        
                else:
                    i = 0
                    while i < n1-1:
                        string_top[i] = string_top[i+1]
                        string_top[n1-1] = temp
                        print(string_top[i],end="")
                        
                        i +=1
                print()
                temp=string_top[0]


    #-----------------Bottom String Work--------------#

                if controler == 0:
                    i = 0
                    while i < n1:
                        string_bottom += [arr[1][st2]]
                        st2+=1
                        if st2 >n2-1:
                            st2 = 0
                        print(string_bottom[i],end="")
                        i += 1
                else:
                    i = 0
                    while i < n2-1:
                        string_bottom[i] = string_bottom[i+1]
                        string_bottom[n1-1] = temp1
                        print(string_bottom[i],end="") 
                        i +=1            
                print()
                temp1 = string_bottom[0]


                controler = 1
                






txt1 = input("enter top text: ")
txt2 = input("Enter bottom text: ")
t = Billboard(txt1,txt2)