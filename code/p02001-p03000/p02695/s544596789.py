#import numpy as np
import math
#from fractions import gcd

def check_Q(current_list,Qset):

    sum_d = 0
    for i in range(len(Qset)):
        current_Qset = Qset[i]
        #print(current_Qset)
        #print(current_list)
        #print(sum_d)
        if (current_list[current_Qset[1]-1]-current_list[current_Qset[0]-1])==current_Qset[2]:
            sum_d = sum_d+current_Qset[3]

    return sum_d

def check_N(preget_list,zan_pre,M,nokori_N,Qset):

    if nokori_N==1:
        sum_list = []
        for i in range(zan_pre,M+1):
            current_list = preget_list+[i]
            sum_list.append(check_Q(current_list,Qset))

        return sum_list
    else:
        sum_list = []
        for i in range(zan_pre,M+1):
            current_list = preget_list+[i]
            sum_list = sum_list + check_N(current_list,i,M,nokori_N-1,Qset)

        return sum_list

def main():

    ##get int
    first_input = list(map(lambda x:int(x), input().split(" ")))
    #second_input = list(map(lambda x:int(x), input().split(" ")))

    ##get float
    #first_input = list(map(lambda x:float(x), input().split(" ")))
    #second_input = list(map(lambda x:float(x), input().split(" ")))

    ##get string
    #first_input = input().split(" ")

    N = first_input[0]
    M = first_input[1]
    Q = first_input[2]

    Qset = []
    for i in range(Q):
        secondkara_input = list(map(lambda x:int(x), input().split(" ")))
        Qset.append(secondkara_input)

    #print(check_N([],1,M,N,Qset))
    print(max(check_N([],1,M,N,Qset)))

if __name__ == '__main__':
    main()
