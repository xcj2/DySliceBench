import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    def make_divisors(n):
             divisors = []
             for i in range(1, int(n**0.5)+1):
                 if n % i == 0:
                     # 約数の片割れをリストに
                     divisors.append(i)
                     # 平方数じゃなければ片割れの相方をリストに
                     if i != n // i:
                         divisors.append(n//i)
             # divisors.sort() # sort必要なかったらコメントアウト
             return len(divisors)
    ans=0
    for i in range(1,n+1,2):
        if make_divisors(i)==8:
            ans+=1
    print(ans)

resolve()