import math
A,B=[int(item) for item in input().split()]

def gdc(A,B):
    if A < B:
        A,B = B,A
    if B==0:
        return A
    else:
        A,B=B,A%B
        return gdc(A,B)

def chk_pn(num):
    flag=True
    if num <= 3:
        pass
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num % i ==0:
                flag = False
                break
    return flag
def mk_factor(num):
    max_divisor = int(math.sqrt(num))+1
    divisor =2
    factor_list=[1]

    while divisor <= max_divisor:
        if num % divisor ==0:
            factor_list.append(divisor)
            num /= divisor
        else:
            divisor += 1
    factor_list.append(num)
    return factor_list

GDC=gdc(A,B)
pn_factor = [i for i in mk_factor(GDC) if chk_pn(i) is True]
print(len(set(pn_factor)))
