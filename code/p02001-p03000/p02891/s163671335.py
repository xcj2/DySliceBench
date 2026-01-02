import sys

def solveA(S):
    N = len(S)
    count = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            S[i+1] = "_"
            count += 1
    return count

def solve(S, K):
    S0 = S[:]
    N = len(S)
    if N == 1:
        return (K-(K%2))//2
    if K < 10:
        return solveA(S*K)
    #actual=(solveA(S*K))
    S1 = S0*1
    S2 = S0*2
    c1 = solveA(S1)
    c2 = solveA(S2)
    if c1 * 2 == c2:
        return c1 * K
    if S2[0] != S2[-1]:
        return c2 * (K//2) + (K%2) * c1
    else:
        a =  c2 * (K//2) + (K%2)*c1 + (K//2)-(1-K%2)
            #if a != solveA(S0*K):
            #print(c1, c2, S2[0]!=S2[-1])
            #print("c2 * (K//2) +(K%2)*c1=", c2 * (K//2)+(K%2)*c1)
        return a


def main():
    S = list(input().rstrip()) # len(S) <= 100
    K = int(input())    # K <= 10**9

    print(solve(S, K))
def test():
    import random

    for i in range(2000):
        n = random.randint(1,100)
        S = random.choices("aaaaaabcedbdddddklkjlkjdsfaak", k=n)
        S0 = S[:]
        K = random.randint(2, 30)
        SK = S*K
        a, a0 = solve(S, K), solveA(SK)
        if a != a0:
            print("".join(S0))
            print(K)
            print("actual=",a, ",expected=",a0)
            print("BAD\n")
            return
#test()
main()
