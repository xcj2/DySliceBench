def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


def getnum(n):
    ret = 1
    _sum = 1
    while True:
        if _sum > n:
            return ret-1
        ret += 1
        _sum += ret

def main():
    n = int(input())
    aa = factorization(n)
    ret = 0
    for a in aa:
        if a[0] == 1:
            continue
        ret += getnum(a[1])
    print(ret)

if __name__=="__main__":
    main()
