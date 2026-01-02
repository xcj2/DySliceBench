import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N = ii()
    ac,wa,tle,re = 0,0,0,0
    for i in range(N):
        t = input()
        if t == "AC":
            ac+= 1
        elif t == "WA":
            wa += 1
        elif t == "TLE":
            tle+= 1
        else:
            re += 1

    print("AC x {}".format(ac))
    print("WA x {}".format(wa))
    print("TLE x {}".format(tle))
    print("RE x {}".format(re))



if __name__ == "__main__":
    main()