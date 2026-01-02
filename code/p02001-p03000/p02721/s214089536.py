import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,K,C=mi()
    S=list(input())
    ok,ng = "o","x"

    OK = []
    for i in range(N):
        if S[i] == ok:
            OK.append(i+1) # 1-index
    
    greeds = [OK[0]]
    for i in range(1,len(OK)):
        x = OK[i]
        if x - greeds[-1] > C:
            greeds.append(x)
            if len(greeds) > K:
                break

    inv_greeds = [OK[-1]]
    inv_OK = OK[::-1]
    for i in range(1,len(OK)):
        x = inv_OK[i]
        if -x + inv_greeds[-1] > C:
            inv_greeds.append(x)
            if len(inv_greeds) > K:
                break
    
    if len(greeds) < K or len(inv_greeds) < K:
        exit()

    greeds = greeds[:K]
    inv_greeds = inv_greeds[:K][::-1]

    # print(greeds,inv_greeds)
    for i in range(len(greeds)):
        if greeds[i] == inv_greeds[i]:
            print(greeds[i])



    
if __name__ == "__main__":
    main()