def perm(n, r):
    rtn = 1
    for i in range(r):
        rtn *= n-i
    return rtn

def cmb(n, r):
    return perm(n, r) // perm(r, r)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnts = [0]*(2*10**5 + 1)
    for v in a:
        cnts[v] += 1
    buf = 0
    for i in range(2*10**5 + 1):
        if cnts[i] > 0:
            buf += cmb(cnts[i], 2)
    for i in range(n):
        x = a[i]
        if cnts[x] <= 1:
            print(buf)
        else:
            ans = buf
            ans -= cmb(cnts[x], 2)
            print(ans + cmb(cnts[x]-1, 2))

if __name__ == "__main__":
    main()