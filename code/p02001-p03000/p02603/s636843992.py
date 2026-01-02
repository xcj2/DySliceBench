import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    _A=list(mi())
    A = []

    for a in _A:
        if len(A) > 0 and A[-1] == a: continue
        A.append(a)
    
    N = len(A)
    bottoms = []
    
    if N < 2:
        print(1000)
        exit()

    if A[0] < A[1]:
        bottoms.append(0)

    for i in range(N-1):
        if not i+2 < len(A): continue
        # print(A[i], A[i+1], A[i+2])
        if A[i] > A[i+1] and A[i+1] < A[i+2]:
            bottoms.append(i+1)
    
    money = 1000
    kabu = 0
    # print(bottoms)
    for bi in bottoms:
        bottom = A[bi]
        i = bi
        while i < N-1 and A[i] < A[i+1]:
            i += 1
        
        top = A[i]

        # print(bi,i)
        # print(bottom,top)
        kabu += money//bottom
        money -= money//bottom * bottom
        
        money += kabu * top
        kabu = 0
        # print("money",money)
    
    print(money)

    

if __name__ == "__main__":
    main()
