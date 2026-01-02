import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    X=I()
    
    #nまでの素数を列挙(n loglogn)
    n = 2*(10**6)

    #is_prime[i]にはi+1が素数か否かを示すboolが入る，[0]に1の素数判定がある．
    is_prime = [True]*(n+1)
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i

    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    
    for i in table:
        if i>=X:
            print(i)
            exit()

main()
