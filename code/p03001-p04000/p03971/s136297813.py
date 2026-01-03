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
    n,a,b = MI()
    s = LS()
    for i in range(n):
        if s[i] == 'c':
            print('No')
            continue
        if s[i] == 'a':
            if a > 0:
                a-=1
                print('Yes')
            elif b > 0:
                b-=1
                print('Yes')
            else:
                print('No')
            continue
        if s[i] == 'b':
            if a+b > 0 and b > 0:
                b-=1
                print('Yes')
            else:
                print('No')
            continue

if __name__ == '__main__':
    main()
