import math

def factor(n):
    r = []
    tmp = n
    for i in range(2, int(math.sqrt(n)) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            r.append((i, cnt))
    if tmp != 1:
        r.append((tmp, 1))
    if not r:
        r.append((n, 1))
    return r

def all_pat(l):
    k = [0] * len(l) 
    t = [tuple(k)]
    while True:
        k[0] += 1
        for i in range(len(l)):
            if k[i] <= l[i][1]:
                break
            k[i] = 0
            if i == len(l) - 1:
                return t
            k[i + 1] += 1
        t.append(tuple(k))
    

def main():
    a = int(input())
    l = factor(a)
    p = all_pat(l)
    t = []
    for i in p:
        m = 1
        for j in range(len(l)):
            m *= l[j][0] ** i[j]
        t.append(m + (a // m))
    print(min(t) - 2)
            


if __name__ == '__main__':
    main()
