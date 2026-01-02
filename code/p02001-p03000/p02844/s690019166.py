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

    ans = 0
    for i in range(1000):
        pin = str(i)
        if len(pin) == 1:
            pin = "00"+pin
        elif len(pin) == 2:
            pin = "0"+pin
        
        waiti = 0
        for j in range(N):
            if S[j] == pin[waiti]:
                waiti += 1
                if waiti == 3:
                    break
                    
        if waiti == 3:
            ans += 1

    print(ans)
            
            





if __name__ == "__main__":
    main()