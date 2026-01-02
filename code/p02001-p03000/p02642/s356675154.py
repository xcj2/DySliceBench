from math import sqrt
from random import randint
def Divisor_Set(n):
    s = set()
    for i in range(1, int(sqrt(n))+2):
        if n%i == 0:
            s.add(i)
            s.add(n//i)
    return s

def main1():
    n = int(input())
    a = list(map(int, input().split()))
    dic = {}
    for x in a:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    ans = 0
    a.sort()
    for i in range(n):
        v = a[i]
        if dic[v] > 1:
            continue
        lim = v//2 + 1
        f = True
        for j in range(i):
            if a[j] > lim:
                break
            if a[i] % a[j] == 0:
                f = False
                break
        if f:
            ans += 1
    print(ans)

def main2():
    n = int(input())
    a = list(map(int, input().split()))
    dic = {}
    for x in a:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    ans = 0
    for v in a:
        if dic[v] > 1:
            continue
        tmp = Divisor_Set(v)
        tmp.remove(v)
        f = True
        for x in tmp:
            if x in dic:
                f = False
                break
        if f:
            ans += 1
    print(ans)

if __name__ == "__main__":
    if randint(1, 2) == 1:
        main1()
    else:
        main2()
