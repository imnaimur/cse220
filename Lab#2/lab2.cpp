#include<bits/stdc++.h>
using namespace std;
// giRtfel2th
// rightLeft2
int main(){
    string txt1,txt2;
    cin >> txt1 >> txt2;

    //length and loop i
    int n1 = txt1.length(),n2 = txt2.length(),i=0;

    // array main
    string arr1[n1],arr2[n2]; 

    // information about billboard    
    int top_idx,bottom_idx;
    char top_char,bottom_char;
    
    while(i < n1)
    {
        arr1[i] += txt1[i];
        if ('A'<=txt1[i] &&  txt1[i]<= 'Z')
        {
            top_char = txt1[i];
            top_idx = i;
        }
        i++;
    }
    i = 0;
    while (i< n2)
    {
        arr2[i] += txt2[i];
        if ('A'<=txt2[i] &&  txt2[i]<= 'Z')
        {
            bottom_char = txt2[i];
            bottom_idx = i;
        }
        i++;
    }


    // some variable for rearranging string
    int st1 = top_idx,st2 = bottom_idx,controller = 0;
    string r_arr1[n1],r_arr2[n2];

    // checking length
    if (n1>10 || n2>10)
        cout<< "Invalid Input Size" << endl ;
    else
    {
        cout << endl;
        cout<< "Top Board Start Character: "<<top_char << endl;
        cout<< "Top Board Start Index: " <<top_idx << endl;
        cout<< "Bottom Board Start Character: " <<bottom_char << endl;
        cout<< "Bottom Board Start Character: " <<bottom_idx << endl;


        //  Infinite loop start
        while (true)
        {
            char press;
            cout << "Press q/Q to quite or any key to continue: ";
            cin >> press;
            if (press == 'Q' || press == 'q')
            {
                break;
            }else
            {

                // Top String Work
                if (controller == 0)
                {
                    i = 0;
                    while(i < n1)
                    {
                        r_arr1[i] += arr1[st1];
                        st1 --;
                        if (st1<0)
                        {
                            st1 = n1-1;
                        }
                        cout<< r_arr1[i];
                        i++;
                    }
                }else
                {
                    i = 0;
                    string temp = r_arr1[0];
                    while(i<n1)
                    {
                        if (i == n1-1)
                        {
                            r_arr1[n1-1] = temp;
                            cout << r_arr1[n1-1];
                            break;

                        }
                        r_arr1[i] = r_arr1[i+1];
                        cout << r_arr1[i];
                        i ++;
                    }
                    // cout<< r_arr1[n1-1];
                }
                cout << endl;


                // Bottom String Work
                if (controller == 0)
                {
                    i = 0;
                    while(i < n2)
                    {
                        r_arr2[i] += arr2[st2];
                        st2 ++;
                        if (st2== n2)
                        {
                            st2 = 0;
                        }
                        cout<< r_arr2[i];
                        i++;
                    }
                }else
                {
                    i = 0;
                    string temp2 = r_arr2[0];
                    while(i<n2)
                    {
                        if (i == n2-1)
                        {
                            r_arr2[n2-1] = temp2;
                            cout << r_arr2[n2-1];
                            break;
                        }
                        r_arr2[i] = r_arr2[i+1];
                        cout << r_arr2[i];
                        i ++;
                    }
                }
                cout << endl;

            }

            controller = 1;
        }
    }
}