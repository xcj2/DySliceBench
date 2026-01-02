
def debug(*args):
    if 1 == 1:
        print(*args)

def solve(N, S):
    R = [0]*N
    L = [0]*N
    c = 0
    for i in range(N):
        if S[i] == 'R':
            c += 1
        else: # 'L'
            if c > 0:
                q, r = divmod(c, 2)
                R[i-1] = q + r
                R[i] =  q
                c = 0
    c = 0
    for i in range(N)[::-1]:
        if S[i] == 'L':
            c += 1
        else: # 'R'
            if c > 0:
                q, r = divmod(c, 2)
                L[i] = q 
                L[i+1] =  q + r
                c = 0
    #debug("S:", *S)
    #debug("R:", *R, "R=",sum(R), sum(c == "R" for c in S))
    #debug("L:", *L, "L=",sum(L), sum(c == "L" for c in S))
    #debug("A:", *[x+y for x, y in zip(R, L)])
    #debug("S", sum(x+y for x, y in zip(R, L)), N)
    print(*[x+y for x, y in zip(R, L)])



def main():
    S = input()
    solve(len(S), S)

main()




