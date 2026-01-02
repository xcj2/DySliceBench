import numpy as np

"""
def divs(_n):
    n = _n
    r = int(np.sqrt(n))
    res = []
    
    for i in range(2, r+1, 1):
        buf = [0, 0]
        while n%i == 0:
            buf[0] = i
            buf[1] += 1
            n/=i
        if buf[0] != 0:
            res.append(buf)
    if len(res)==0:
        res.append([n, 1])
        
    return res


def has(lis, num, search_i):
    beki = -1
    index = -1
    for i in range(search_i, len(lis), 1):
        #print(type(i))
        if lis[i][0] == num:
            beki = lis[i][1]
            index = i
            break
    return (beki, index)


def common_divs(_a, _b):
    # len(a) <= len(b)
    if len(_a) > len(_b):
        a = _b
        b = _a
    else:
        a = _a
        b = _b

    common = []
    search_i = 0 # from this index, search e[0] in list b
    for e in a:
        beki, index = has(b, e[0], search_i)
        if beki > 0:
            common_e = [e[0], min(e[1], beki)]
            common.append(common_e)
            search_i = index + 1
    return common

def mult_all(c):
    res = 1
    for i in range(len(c)):
        res *= c[i][0]**c[i][1]
    return res


def main():
a, b, k = map(int, input().split())
    divA = divs(a)
    divB = divs(b)
    divC = common_divs(divA, divB)
    
    #print ( divA, '\n', divB, '\n', divC, '\n')
    cnt = 1
    i = 0
    ans = mult_all(divC) 
    while(True):
        if cnt + divC[i][1] <= k:
            ans /= divC[i][0]**divC[i][1]
            cnt += divC[i][1]
        else:
            ans /= divC[i][0]**(k-cnt)
            break
        i += 1
        
    print(int(ans))

def main2():
    
main()    
"""

def divs(n):
    res = np.zeros(int(n/2))
    cnt = 0
    for i in range(n, 1, -1):
        if n%i == 0:
            res[cnt] = i
            cnt += 1
    return res[np.where(res>0)]


def main():
    a, b, k = map(int, input().split())
    divA = divs(a)
    divB = divs(b)

    cnt = 0
    ans = 1
    flag = False
    for i in range(len(divA)):
        if flag == True:
            break
        else:
            for j in range(len(divB)):
                if flag==False and divA[i]==divB[j]:
                    cnt += 1
                    if cnt == k:
                        ans = divA[i]
                        flag = True

    print(int(ans))
               
    
main()
