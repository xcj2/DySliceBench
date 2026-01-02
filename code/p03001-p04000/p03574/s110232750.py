import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    H,W=mi()
    G = [[] for _ in range(H)]
    for i in range(H):
        S = input()
        G[i] = list(S)
    
    # print(G)
    for h in range(H):
        for w in range(W):
            if G[h][w] == "#": continue
            res = 0
            for dh in [-1,0,1]:
                for dw in [-1,0,1]:
                    if dh == dw == 0: continue
                    if 0 <= h+dh < H and 0<= w+dw < W:
                        if G[h+dh][w+dw] == "#":
                            res += 1
            
            G[h][w] = str(res)

    # print(G)
    for h in range(H):
        print("".join(G[h]))



if __name__ == "__main__":
    main()