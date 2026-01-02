import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,m=map(int, input().split())
    def make_divisors(n):
             divisors = []
             for i in range(1, int(n**0.5)+1):
                 if n % i == 0:
                     # 約数の片割れをリストに
                     divisors.append(i)
                     # 平方数じゃなければ片割れの相方をリストに
                     if i != n // i:
                         divisors.append(n//i)
             divisors.sort(reverse=True) # sort必要なかったらコメントアウト
             return divisors
    for i in make_divisors(m):
        if i*n<=m:
            print(i)
            break

resolve()