import sys, math
def input(): return sys.stdin.readline().strip()


def func(R, G, B, lR, lG, lB):
    pG = lG - 1
    pB = lB - 1
    sumR = 0
    sumG = 0

    for i in range(lR - 1, -1, -1):
        while pG >= 0 and R[i] < G[pG]:
            while pB >= 0 and G[pG] < B[pB]:
                pB -= 1
            sumG += (lB - pB - 1)
            pG -= 1
        sumR += sumG
    return sumR


def main():
    N = int(input())
    S = input()
    
    R = []
    G = []
    B = []
    lR = 0
    lG = 0
    lB = 0
    for i in range(N):
        if S[i] == "R":
            R.append(i)
            lR += 1
        elif S[i] == "G":
            G.append(i)
            lG += 1
        else:
            B.append(i)
            lB += 1
    
    ans = 0
    ans += func(R, G, B, lR, lG, lB)
    #print("RGB->{}".format(func(R, G, B, lR, lG, lB)))
    ans += func(R, B ,G, lR, lB, lG)
    #print("RBG->{}".format(func(R, B ,G, lR, lB, lG)))
    ans += func(G, R, B, lG, lR, lB)
    #print("GRB->{}".format(func(G, R, B, lG, lR, lB)))
    ans += func(G, B, R, lG, lB, lR)
    #print("GBR->{}".format(func(G, B, R, lG, lB, lR)))
    ans += func(B, R, G, lB, lR, lG)
    #print("BRG->{}".format(func(B, R, G, lB, lR, lG)))
    ans += func(B, G, R, lB, lG, lR)
    #print("BGR->{}".format(func(B, G, R, lB, lG, lR)))

    subtract = 0
    for i in range(N):
        for j in range(i + 1, N):
            k = j * 2 - i
            if k < N and (S[i] != S[j] and S[j] != S[k] and S[k] != S[i]):
                subtract += 1

    print(ans - subtract)
    


if __name__ == "__main__":
    main()
