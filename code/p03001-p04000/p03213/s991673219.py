import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    P=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def prime_array(n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a



    N_p = {x:0 for x in P}
    for i in range(1,N+1):
        for p in prime_array(i):
            N_p[p] += 1
    
    # print(N_p)

    ans = 0
    for p in P:
        if N_p[p] >= 74: ans += 1
    
    for p1 in P:
        for p2 in P:
            if p1 == p2: continue
            if N_p[p1] >= 2 and N_p[p2] >= 24: ans += 1
            if N_p[p1] >= 4 and N_p[p2] >= 14: ans += 1
    
    seen = set()
    for p1 in P:
        for p2 in P:
            if p1 == p2: continue
            for p3 in P:
                if p2 == p3 or p1 == p3 or (p1,p2,p3) in seen: continue
                if N_p[p1] >= 2 and N_p[p2] >= 4 and N_p[p3] >= 4: ans += 1

                seen.add((p1,p2,p3))
                seen.add((p1,p3,p2))

    print(ans)




if __name__ == "__main__":
    main()