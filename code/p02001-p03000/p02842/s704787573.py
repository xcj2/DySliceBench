def II(): return int(input())
def MI(): return map(int,input().split())
def LMI(): return list(map(int,input().split()))
def LIIN(n): return list(int(input()) for _ in range(n))
def LMIN(n): return [list(map(int, input().split())) for _ in range(n)]
def IS(): return input()
def LS(): return list(input())
def MS(): return map(str,input().split())
def LMS(): return list(map(str,input().split()))
def LMS(): return list(map(str,input().split()))
def LISN(n): return list(input() for _ in range(n))
def LMSN(n): return [input().split() for _ in range(n)]
MOD = 10**9+7
INF = 10**18

def main():
    n = II()
    tmp = (n * 100 + 108 - 1) // 108
    if tmp * 108 //100 != n:
        print(':(')
    else:
        print(tmp)

if __name__ == '__main__':
    main()
