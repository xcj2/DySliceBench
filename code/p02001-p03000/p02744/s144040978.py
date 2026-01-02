import itertools
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

# x1+x2+x3+...xN = X (x>=0) 
def nHk_list(N,X):
    if N == 0: return []
    elif N == 1: return [[X]]

    border = [i for i in range(X+1)]
    res = []
    for S in itertools.combinations_with_replacement(border, N-1):
        # print(S)
        pre = 0
        sub = []
        for s in S:
            sub.append(s-pre)
            pre = s
        sub.append(X-pre)
        res.append(sub)
    return res


INF=10**20
def main():
    N=ii()
    alphabet = ["a","b","c","d","e","f","g","h","i","j"]

    ans = []
    for c in range(1,N+1):
        # print("___\nc",c)
        for X in nHk_list(c,N-c):
            # print("X:",X,"c:",c,"N-c:",N-c)
            V = []
            for i in range(len(X)):
                x = X[i]
                V.append(list(itertools.product(alphabet[:i+1],repeat=x)))

            # print("V",V)
            U = itertools.product(*V)
            base = alphabet[:c]
            for u in U:
                char = ""
                for i in range(c):
                    char += alphabet[i] + "".join(list(u[i]))
        
                ans.append(char)
        
    
    ans.sort()
    # ans.append("".join(alphabet[:N]))
    print(*ans,sep='\n')

            
            

        

if __name__ == "__main__":
    main()