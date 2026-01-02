import math

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

n = int(input())

if n == 1 or n == 2:
    print(0)
    exit()

root_n = int(math.sqrt(n))

ans = 0
for mod in range(1, root_n+1):
    if (n - mod) % mod == 0:
        a = (n - mod) // mod
        #if a != 1 and a < n:
        if n % a == mod:
            #print(a)
            ans += a

print(ans)
