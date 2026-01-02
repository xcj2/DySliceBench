import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    S2 = list(input())
    T = list(input())
    N = len(S2)
    unable = "UNRESTORABLE"


    window_size = len(T)
    X = [] # 合致したwindow
    for i in range(N):
        window = S2[i:i+window_size]
        f = True

        if len(window) != window_size: continue
        for j in range(window_size):
            if not (window[j] == T[j] or window[j] == "?"):
                f = False
                break
        
        if f:
            X.append((i,i+window_size))
    
    if len(X) == 0:
        print(unable)
        exit()
    

    i,j = X[-1]
    S2[i:j] = T

    S = []
    for s in S2:
        if s == "?":
            S.append("a")
        else:
            S.append(s)
    
    print("".join(S))



if __name__ == "__main__":
    main()