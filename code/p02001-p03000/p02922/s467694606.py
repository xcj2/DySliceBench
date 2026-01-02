def II(): return int(input())
def MI(): return map(int,input().split())
def LMI(): return list(map(int,input().split()))
def LIIN(n): return list(int(input()) for _ in range(n))
def LMIN(n): return [list(map(int, input().split())) for _ in range(n)]
def IS(): return input()
def MS(): return map(str,input().split())
def LMS(): return list(map(str,input().split()))
def LISN(n): return list(input() for _ in range(n))
def LMSN(n): return [input().split() for _ in range(n)]
MOD = 10**9+7
INF = 10**18

def main():
    a,b = MI()
    print(1+(b-a+(a-1)-1)//(a-1))

if __name__ == '__main__':
    main()
