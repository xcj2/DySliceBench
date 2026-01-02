import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N = ii()
    A = list(mi())

    A.sort()
    if A[0] == 1:
        print(1)
        exit()
    
    ini = A[0]
    while len(A) > 1:
        x = A[0]
        B = set([x])
        for a in A:
            b = a%x
            if b > 0:
                B.add(b)

        A = list(B)
        A.sort()

    if len(A) > 0:
        print(A[0])
    else:
        print(ini)
            

            
        



if __name__ == "__main__":
    main()