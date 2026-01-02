import sys
def I(): return int(sys.stdin.readline())
def LI(): return [int(x) for x in sys.stdin.readline().split()]

def calc(a,b,n):
    ret = 0
    if a==b and a<=n:
        ret += 1
    if a*10+b <= n:
        ret += 1
    for i in range(2,7):
        if a*(10**i)+b>n:
            break
        if a*(10**i)+(10**i)-10+b<=n:
            ret += 10**(i-1)
            continue
        tmp = n
        while(tmp%10!=b):
            tmp -= 1
        tmp -= a*(10**i)
        tmp //= 10
        tmp += 1
        ret += tmp
    return ret

def main():
    N = I()
    ans = 0
    for A in range(1,10):
        for B in range(1,10):
            ans += calc(A,B,N) * calc(B,A,N)
    print(ans)

if __name__ == "__main__":
    main()
