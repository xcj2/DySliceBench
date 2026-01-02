import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    H,W,M=mi()

    H_count = [0] * (H+1)
    W_count = [0] * (W+1)
    G = set()
    seenH = set()
    seenW = set()
    for i in range(M):
        h,w=mi()
        H_count[h] += 1
        W_count[w] += 1

        seenH.add(h)
        seenW.add(w)
        G.add((h,w))
    
    Hs = []
    Ws = []
    for i in range(max(H,W)+1):
        if i < len(H_count):
            count = H_count[i]
            if count > 0:
                Hs.append((count,i))

        if i < len(W_count):
            count = W_count[i]
            if count > 0:
                Ws.append((count,i))


    Hs.sort(reverse=True)
    Ws.sort(reverse=True)

    # print(Hs)
    # print(Ws)

    h_count,h = Hs[0]
    w_count,w = Ws[0]

    original = h_count + w_count
    ans = original
    if (h,w) in G:
        # print("a")
        ans -= 1

        i = 1
        sameH = []
        while i < len(Hs) and Hs[i][0] == h_count:
            # print("h")
            h = Hs[i][1]
            i += 1
            sameH.append(h)
        
        i = 1
        sameW = []    
        while i < len(Ws) and Ws[i][0] == w_count:
            w = Ws[i][1]
            i += 1
            sameW.append(w)
           
        max_mass = (len(sameH)+1) * (len(sameW)+1)

        # print(max_mass)
        on_bom_count = 0
        for h,w in G:
            count = H_count[h] + W_count[w]
            if count == original:
                on_bom_count += 1
        
        if max_mass - on_bom_count > 0:
            ans += 1

                
    print(ans)


        
    



if __name__ == "__main__":
    main()