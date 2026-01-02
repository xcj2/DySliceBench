import itertools
import bisect
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))


INF=10**20
def main():
    N=ii()
    S=list(input())

    R,G,B=[],[],[]
    Rset,Gset,Bset = set(),set(),set()
    
    for i in range(N):
        s = S[i]
        if s == "R":
            R.append(i)
            Rset.add(i)

        elif s == "G":
            G.append(i)
            Gset.add(i)
        
        else:
            B.append(i)
            Bset.add(i)

    ans = 0
    dic = {"R":(R,Rset),"G":(G,Gset),"B":(B,Bset)}
    for comb in itertools.permutations(["R","G","B"]):
        X,Y,Z = dic[comb[0]][0], dic[comb[1]][0], dic[comb[2]][0]
        Xset,Yset,Zset = dic[comb[0]][1], dic[comb[1]][1], dic[comb[2]][1]

        # print(X,Y,Z)
        for x in X:
            for y in Y:
                if not x < y: continue
                ignore_z = 2*y - x
                has_ignore_target = ignore_z in Zset

                iz = bisect.bisect_left(Z,y+1)
                if not 0<=iz<len(Z): continue
                z_count = len(Z)-iz

                if has_ignore_target:
                    z_count -= 1
                
                assert z_count >= 0
                ans += z_count
                # print(ans)


    print(ans)





if __name__ == "__main__":
    main()