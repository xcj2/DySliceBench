def burst(S,H,W):
    for i in range(H):
        S[i] += "d" #dummy
    S.append("d" * (W+1))
    tate_burst = [[] for _ in range(W)]
    yoko_burst = [[] for _ in range(H)]
    #tate_burst[j]:j列目の連続する"."の(左端,右端)
    #yoko_burst[i]:i行目の連続する"."の(上端,下端)

    for j in range(W):
        sp,ep = None,None
        for i in range(H):
            if S[i][j] == ".":
                if sp == None:
                    sp = i
                    if S[i+1][j] != ".":
                        ep = i
                        tate_burst[j].append((sp,ep))
                        sp,ep = None,None
                elif S[i+1][j] != ".":
                    ep = i
                    tate_burst[j].append((sp,ep))
                    sp,ep = None,None

    for i in range(H):
        sp,ep = None,None
        for j in range(W):
            if S[i][j] == ".":
                if sp == None:
                    sp = j
                    if S[i][j+1] != ".":
                        ep = j
                        yoko_burst[i].append((sp,ep))
                        sp,ep = None,None
                elif S[i][j+1] != ".":
                    ep = j
                    yoko_burst[i].append((sp,ep))
                    sp,ep = None,None

    return tate_burst,yoko_burst

def score(tate_burst,yoko_burst,H,W):
    T = [[-1 for _ in range(W)] for _ in range(H)]

    for j in range(W):
        for st,go in tate_burst[j]:
            for i in range(st,go+1):
                T[i][j] += (go-st+1)

    for i in range(H):
        for st,go in yoko_burst[i]:
            for j in range(st,go+1):
                T[i][j] += (go-st+1)

    return T

def max_score(T,H,W):
    output = 0
    for i in range(H):
        for j in range(W):
            output = max(output,T[i][j])

    return output

def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]

    B = burst(S,H,W)
    tate_burst,yoko_burst = B[0],B[1]
    T = score(B[0],B[1],H,W)
    ans = max_score(T,H,W)

    print(ans)

if __name__ == "__main__":
    main()
