import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    iS = input().rstrip()

    S = []
    for i in range(N-1):
        S.append(abs(int(iS[i])-int(iS[i+1])))
    N -= 1

    f = FactorialUtils(N)
    n1 = n2 = 0
    for i in range(N):
        t = f.choose(N-1,i)
        #print(t,S[i])
        if S[i] == 1: n1 += t
        elif S[i] == 2: n2 += t
    if n1&1 and n2&1: print(1)
    elif n1&1: print(1)
    elif n2&1 and n1==0: print(2)
    else: print(0)
    #print(n1,n2)

class FactorialUtils:
    def __init__(self, n):
        self.fac = [1] * (n+1)
        for i in range(2, n+1): self.fac[i] = self.fac[i-1] + (i&(-i)).bit_length()

    def choose(self, n, r):
        if r < 0 or r > n: return 0
        return 2 if (self.fac[n] - self.fac[n-r] - self.fac[r]) > 0 else 1

if __name__ == '__main__':
    main()
