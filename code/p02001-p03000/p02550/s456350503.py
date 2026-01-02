#create date: 2020-09-19 21:14

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n, x, m = na()
    ans = x
    l = [x]
    a = x
    for i in range(n-1):
        a = a**2
        a %= m
        if a == 0:
            ans += a
            print(ans)
            quit()
        if a in l:
            #print(a, l)
            j = l.index(a)
            r = i - j + 1
            res = sum(l[j:])
            k = ((n-i-1)%r)
            #print(k, n-i-1, r, l[j:(j+k)])
            ans += (n-i-1)//r * res + sum(l[j:(j+k)])
            break
        l.append(a)
        ans += a
    print(ans)

if __name__ == "__main__":
    main()