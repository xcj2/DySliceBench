def getN():
    return int(input())


def getNM():
    return map(int, input().split())


def getList():
    return list(map(int, input().split()))

def gcd(n,m):
    if n > m:
        n,m = m,n
    while (m % n != 0):
        temp = n;
        n = m % n;
        m = temp;
    return n;

def lcm(m,n):
    return int(m*n/gcd(m,n))

N,M = getNM()

s = input()
t = input()

lcm = lcm(N,M)
ks, kt = lcm//N, lcm//M
order = {}
flag = 1
i = 0
for alp in s:
    order[ks*i+1] = alp
    i += 1

j= 0
for alp in t:
    num = kt*j+1
    try:
        if order[num] != alp:
            flag = 0
    except:
        pass
    j += 1

if flag:
    print(lcm)
else:
    print("-1")

