from itertools import permutations

def score(S):
    S0 = [' '] + S + [' ']
    score = 0
    s = [0]*len(S0)
    for i in range(1, len(S)+1):
        c = S0[i]
        if c == 'L':
            s[i] += 1 if S0[i-1] == 'L' else 0
        else:
            s[i] += 1 if S0[i+1] == 'R' else 0
    return sum(s)

def main2():
    N, K = map(int, input().split())
    S = list(input().strip())
    m = score(S)
    
    print(min(m + 2 * K, N-1))

def main():
    N, K = map(int, input().split())
    S = list(input().strip())
    print(S, score(S), "initial")
    m = score(S)
    for ps in permutations([(i, j) for i in range(N) for j in range(i, N)], K):
        S_ = list(S)
        for p in ps:
            apply(S_, p)
        s = score(S_) 
        if m < s:
            mp = ps
            m = s
    S_ = list(S)
    for p in mp:
        apply(S_, p)
        print(S_, score(S_), p)
    print(m, mp)

def apply(S, lr):
    l, r = lr
    for i in range(r-l+1):
        if l+i > r-i:
            break
        S[l+i], S[r-i] = S[r-i], S[l+i]
        S[l+i] = 'R' if S[l+i] == 'L' else 'L'
        if l+i != r-i:
            S[r-i] = 'R' if S[r-i] == 'L' else 'L'

if 1==0:
    S = list("LLLLL")
    apply(S, (0, 4))
    print(S)

main2()
