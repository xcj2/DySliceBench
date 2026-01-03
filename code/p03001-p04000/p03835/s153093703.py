k=0
s=0
combi = 0

def nyu():
    num1,num2 = input().split()
    k = int(num1)
    s = int(num2)
    return k,s

def calc(l_k,l_s):
    l_combi = 0
    for x in range(l_k):
#        check_tmp =0
#        check_tmp =check1(x,l_s,l_k)
#        if check_tmp == 1:
#            break
#        elif check_tmp  == 2:
#            continue
        for y in range(l_k):
#            check_tmp =check2(x,y,l_s,l_k)
#            if check_tmp == 1:
#                break
#            elif check_tmp  == 2:
#                continue2
#            sum = x+y+l_k 
            sum = l_s- x-y 
            if 0<=sum and sum <= k:
#                print("x=",x,"y="   ,y) 
                l_combi +=1
    return l_combi

def check1(x,s,k):
    if s<x:
        return 1
    if x+(k-1)*2 < s:
        return 2
    return 0

def check2(x,y,s,k):
    sum = x+y
    if s<sum:
        return 1
    if x+y+k-1 < s:
       return 2
    return 0

def check3(x,y,z,s):
    sum = x+y+z
    if s<sum:
        return 1
    return 0    

def check_ini(k,s):
    if k*3 < s:
        return True
    return False


k,s=nyu()
if check_ini == True:
    print("0")
else :
    print(calc(k+1,s))







