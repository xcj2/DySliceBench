import sys
input = sys.stdin.readline

mod = 10**9+7

def cmb(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
NN = 4*10**5 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

Child = [1]*N
Score = [1]*N

def dfs1(s):
    stack = [s]
    Ind = [0]*N
    while stack:
        p = stack[-1]
        #print(p)
        #print(Score)
        #print(Child)
        if Ind[p] == len(graph[p]):
            stack.pop()
            par = -1
            if len(stack) > 0:
                par = stack[-1]
            P = []
            for ch in graph[p]:
                if ch == par: continue
                Child[p] += Child[ch]
                P.append([Score[ch], Child[ch]])
            tmp = Child[p]-1
            for s, c in P:
                Score[p] = (Score[p] * s * cmb(tmp, c)) % mod
                tmp -= c
        elif len(stack) > 1 and stack[-2] == graph[p][Ind[p]]:
            Ind[p] += 1
        else:
            stack.append(graph[p][Ind[p]])
            Ind[p] += 1

ans = [-1]*N

def dfs2(s):
    stack = [s]
    ans[s] = Score[s]
    Ind = [0]*N
    while stack:
        p = stack[-1]
        #print(p)
        #print(Score)
        #print(Child)
        if Ind[p] == len(graph[p]):
            stack.pop()
            if len(stack) > 0:
                par = stack[-1]
                kiyo = Score[par] * cmb(Child[p]-1, Child[par])
                Score[p] = Score[p] * pow(kiyo, mod-2, mod) % mod
                Child[p] -= Child[par]
                Child[par] += Child[p]
                Score[par] = (Score[par] * Score[p] * cmb(Child[par]-1, Child[p])) % mod
        elif len(stack) > 1 and stack[-2] == graph[p][Ind[p]]:
            Ind[p] += 1
        else:
            ch = graph[p][Ind[p]]
            kiyo = Score[ch] * cmb(Child[p]-1, Child[ch])
            Score[p] = Score[p] * pow(kiyo, mod-2, mod) % mod
            Child[p] -= Child[ch]
            Child[ch] += Child[p]
            Score[ch] = (Score[ch] * Score[p] * cmb(Child[ch]-1, Child[p])) % mod
            ans[ch] = Score[ch]
            stack.append(ch)
            Ind[p] += 1

def main():
    dfs1(0)
    dfs2(0)
    print(*ans, sep="\n")

if __name__ == "__main__":
    main()