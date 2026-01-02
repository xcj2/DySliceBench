import numpy as np

def main():
    temp = input().split()
    N = int(temp[0])
    M = int(temp[1])
    k = [] #tukawanai
    s = []
    for m in range(M):
        temp = input().split()
        k.append(int(temp[0]))
        s.append([])
        for x in temp[1:]:
            s[m].append(int(x)-1)
    p = []
    temp = input().split()
    for x in temp:
        p.append(int(x))
    res = 0
    for i in range(2**N):
        suitti = ret_suitti(i,N)
        if(hantei(suitti, s, p)):
            res += 1
    print(res)

def ret_suitti(i,N):
    suitti = []
    shou = i
    for n in range(N):
        amari = shou % 2
        shou = shou // 2
        if(amari == 0):
            suitti.append(0)
        else:
            suitti.append(1)
    return suitti

def hantei(suitti, s, p):
    M = len(p)
    flag = 1
    for m in range(M):
        on_suitti = 0
        for x in s[m]:
            if(suitti[x] == 1):
                on_suitti += 1
        if(on_suitti % 2 != p[m]):
            flag = 0
    if(flag == 1):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
