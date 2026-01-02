import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    H,W,K=mi()
    C = [[""]*H for _ in range(W)]
    for h in range(H):
        t = list(input())
        for w in range(W):
            C[w][h] = t[w]
    
    WL = []
    for i in range(2**W):
        w_l = set()
        for j in range(W): 
            if ((i >> j) & 1):
                w_l.add(j)
        WL.append(w_l)

    HL = []
    for i in range(2**H):
        h_l = set()
        for j in range(H): 
            if ((i >> j) & 1):
                h_l.add(j)
        HL.append(h_l)


    def count(graph):
        cnt = 0
        for h in range(H):
            for w in range(W):
                if graph[w][h] == "#":
                    cnt += 1

        return cnt

    def refill_and_count(wl,hl):
        newC = [[""]*H for _ in range(W)]
        for h in range(H):
            for w in range(W):
                if w in wl or h in hl:
                    newC[w][h] = "r"
                else:
                    newC[w][h] = C[w][h]

        # print(newC)
        return count(newC)

    ans = 0
    for wl in WL:
        for hl in HL:
            # print(wl,hl)
            black = refill_and_count(wl,hl)
            # print(black)
            if black == K:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()