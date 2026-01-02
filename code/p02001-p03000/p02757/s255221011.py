def solve2(s):
    ans = 0
    for i, c in enumerate(s): #見る数字を右に広げていく
        if c in '02468':
            ans += i + 1 # 見ている数字のの一番右の桁が偶数ならその頭に乗っている数字の数だけ
                        # 答えに追加する
                        # 例 2254とし2→偶数、22→偶数（さらに先頭の2をどけても偶数）
                        # →225（奇数）→2254（偶数、上の3つをそれぞれどけても偶数）
    return ans


def solve5(s): # p==2のときと同じ原理
    ans = 0
    for i, c in enumerate(s):
        if c in '05':
            ans += i + 1
    return ans


def solve_other(s, p):
    ans = 0
    last_mod=0
    mods = [0]*p
    mods[0] = 1 #初期値として何も選んでない状態を1個加えとく
    digit = 1
    for i in range(n-1,-1,-1): # 一番右のけたから見る
        last_mod = (last_mod + int(s[i])*digit)%p # 最新のmodに新しく見ている桁*(10**x)を足してmod計算
        ans += mods[last_mod] # modリストに直前までのの値を答えに追加
        mods[last_mod] += 1 # modリスト更新
        digit=digit*10%p # 桁上げ
    return ans


n, p = list(map(int, input().split()))
s = input()
if p == 2:
    print(solve2(s))
elif p == 5:
    print(solve5(s))
else:
    print(solve_other(s, p))
