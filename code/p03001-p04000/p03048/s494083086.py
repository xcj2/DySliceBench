def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

r,g,b,n = get_nums_l()

ans = 0
for ra in range(n//r + 1):
    for ga in range(n//g + 1):
        now = r * ra + g * ga
        nokori = n - now
        if nokori >= 0 and nokori % b == 0:
            ans += 1

print(ans)