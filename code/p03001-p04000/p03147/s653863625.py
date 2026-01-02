import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    H=list(mi())

    for h in H:
        if h != 0:break
    else:
        print(0)
        exit()
    
    ans = 0
    while True:
        i = 0
        while i < N and H[i] == 0:
            i += 1
            
        while i < N:
            # print(i)
            for j in range(i,N):
                if H[j] == 0: break
                H[j] -= 1
            while j < N and H[j] == 0:
                j += 1
            # print(H)
            if j == N-1 and H[j] != 0:
                i = N
            else:
                i = j
            ans += 1
        
        count = 0
        for j in range(N):
            count += H[j] == 0
        
        if count == N:
            break
        


    print(ans)
    



        





if __name__ == "__main__":
    main()