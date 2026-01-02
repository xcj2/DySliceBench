#! /usr/bin/env python3
#! /usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def bit_search(n):
    res = []
    for i in range(2**n):
        st = set()
        for j in range(n): 
            if ((i >> j) & 1):
                st.add(j)
        res.append(st)
    return res

def main():
    H,W,K=mi()
    
    G = []
    for i in range(H):
        G.append(list(input()))
    
    v = [[0] * W for _ in range(H+1)]
    for w in range(W):
        for h in range(H):
            white_choc = G[h][w] == "1"
            v[h+1][w] = v[h][w] + white_choc
    
    ans = INF
    for borders in bit_search(H):
        counts = [[0] for _ in range(20)]
        k_fact = 1
        W_borders = []

        failed = False
        from_zero = True
        w = 0
        while w < W:
            pre = 0
            over_K = False

            max_diff = 0
            for i,border in enumerate(borders):
                if border == 0: continue
                count = v[border][w] - v[pre][w]
                if not from_zero:
                    count += counts[i][-1]
                else:
                    if count > K:
                        failed = True
                        break
                
                if count > K:
                    over_K = True
                

                counts[i].append(count)
                pre = border
            
            count = v[H][w] - v[pre][w]
            if not from_zero:
                count += counts[i+1][-1]
            else:
                if count > K:
                    failed = True
                    break

    
            if count > K:
                over_K = True


            counts[i+1].append(count)
            if over_K:
                W_borders.append(w-1)
                from_zero = True

                for c in counts:
                    if len(c) == 0: continue
                    c.pop() # 直前のカウント履歴を消す
            else:
                from_zero = False
                w += 1

            
            if failed:
                break

        # print(counts)
        if not failed:
            # print(borders)
            # print(W_borders)
            # print(counts)
            # # # print(v[2])
            # # exit()
            count_of_ope = len(borders) + len(W_borders)
            ans = min(count_of_ope,ans)


    print(ans)




if __name__ == "__main__":
    main()
