import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

MOD = 1000000007

def smax(a,b):
    if a>b:
        return a
    else:
        return b

def smin(a,b):
    if a<b:
        return a
    else:
        return b


def main():
    N = int(readline())
    S = readline().rstrip().decode()
    rn = 0
    gn = 0
    bn = 0
    R = [0]
    G = [0]
    B = [0]

    for i in range(N):
        if S[i]=="R":
            rn+=1
        if S[i]=="G":
            gn+=1
        if S[i]=="B":
            bn+=1
        R.append(rn)
        G.append(gn)
        B.append(bn)
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            if S[i]!=S[j]:
                if "R"!=S[i] and "R"!=S[j]:
                    ans += R[N]-R[j]
                    if j+(j-i) < N:
                        if S[j+(j-i)]=="R":
                            ans-=1
                elif "G"!=S[i] and "G"!=S[j]:
                    ans += G[N]-G[j]
                    if j+(j-i) < N:
                        if S[j+(j-i)]=="G":
                            ans-=1
                elif "B"!=S[i] and "B"!=S[j]:
                    ans += B[N]-B[j]
                    if j+(j-i) < N:
                        if S[j+(j-i)]=="B":
                            ans-=1
        
    print(ans)


if __name__ == '__main__':
    main()