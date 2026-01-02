import sys
def I(): return int(sys.stdin.readline())
def LI(): return [int(x) for x in sys.stdin.readline().split()]

def GCM(a,b):
    while(a%b!=0):
        a,b = b,a%b
    return b

def main():
    N,M = LI()
    A = LI()

    count_two = 0
    while(A[0]%2==0):
        A[0] //= 2
        count_two += 1
    pow_two = pow(2,count_two)

    for i in range(1,N):
        if A[i]%pow_two != 0:
            print(0)
            return
        A[i] //= pow_two
        if A[i]%2 == 0:
            print(0)
            return

    tmp = A[0]

    for i in range(1,N):
        tmp = tmp * A[i] // GCM(tmp,A[i])
        if tmp > M:
            print(0)
            return

    ans = M//(tmp*pow_two//2)
    if ans%2==0:
        ans -= 1
    ans -= ans//2
    print(ans)


if __name__ == "__main__":
    main()
