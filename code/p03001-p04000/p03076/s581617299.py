import sys
import numpy as np
import math

def ReadInputNum():
    input_num=[]
    for i in range(5):
        input_num.append(int(input()))
    return tuple(input_num)

def CheckRangeInput(*argv):
    for num in argv:
        if 1<=num<=123 and isinstance(num,int):
            pass
        else:
            print("input"+ num +"is unexpected.")
            sys.exit()


def SumTotalTime(Tuple_Input):
    list_input=list(Tuple_Input)
    amari=[]
    # use numpy #                                                                                                                                                                        
    # list_tmp=np.array(list_input)                                                                                                                                                      
    # amari=(list_tmp-1)%10                                                                                                                                                              

    for i in list_input:
        amari.append((i-1) % 10)

    # amari=amari.tolist()                                                                                                                                                               
    last_one=min(amari)
    last_one=list_input.pop(amari.index(last_one))
    # print(last_one)                                                                                                                                                                    
    # print(list_input)                                                                                                                                                                  

    out_put=0
    for i in list_input:
        out_put += math.ceil(i/10)*10
    # print(out_put)                                                                                                                                                                     
    print(out_put+last_one)


# tuple_input= ReadInputNum()                                                                                                                                                            
# CheckRangeInput(tuple_input)                                                                                                                                                           
A,B,C,D,E = ReadInputNum()
CheckRangeInput(A,B,C,D,E)
tuple_input = (A,B,C,D,E)
SumTotalTime(tuple_input)
