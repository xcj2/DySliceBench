import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()

    city = []
    dic = {}
    for i in range(N):
        S,P=isp()
        P = int(P)
        if not S in city:
            city.append(S)
            dic[S] = [(P,i)]
        else:
            dic[S].append((P,i))
    
    city.sort()
    for S in city:
        Ps = dic[S]
        Ps.sort(reverse=True) 
        for p,i in Ps:
            print(i+1)
    


if __name__ == "__main__":
    main()