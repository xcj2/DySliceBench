from sys import stderr, setrecursionlimit
from functools import reduce
from operator import add
from collections import Counter
from collections import Counter
setrecursionlimit(2147483647)
def f(): return [int(i) for i in input().split()]
def yes(n): print("Yes" if n else "No")
def debug(*x, sep=" ", end="\n"):
    for item in x:
        stderr.write(str(item))
        stderr.write(sep)
    stderr.write(end)


n = int(input())
v = f()
debug(v)
ans = 0
even = Counter(v[0::2])
odd = Counter(v[1::2])

most_even = even.most_common(2)
most_odd = odd.most_common(2)

# 数字は2種類じゃないとダメ
if most_even[0][0] == most_odd[0][0]:
    if most_even[0][1] == most_odd[0][1]:
        # 2つ目が多い方を2つ目に  
        if len(most_even) != 1 and len(most_even) != 1:
            if most_even[1][1] < most_odd[1][1]:
                ans = (n//2 - most_even[0][1]) +  (n//2 - most_odd[1][1])
            else:
                ans = (n//2 - most_odd[0][1]) +  (n//2 - most_even[1][1])
        elif len(most_even) == 1 and len(most_odd) != 1:
            # most_evenの2番目は'0'
            ans = (n//2 - most_even[0][1]) + (n//2 - most_odd[1][1])
        elif len(most_even) != 1 and len(most_odd) == 1:
            # most_oddの2番目は'0'
            ans = (n//2 - most_even[1][1]) +  (n//2 - most_odd[0][1])
        else:
            ans = (n//2 - most_even[0][1]) + (n//2)
    # 総合結果から判断
    else:
        if len(most_even) != 1 and len(most_odd) != 1:
            # そのまま計算
            if most_even[0][1] + most_odd[1][1] < most_even[1][1] + most_odd[0][1]:
                ans = (n//2 - most_even[1][1]) +  (n//2 - most_odd[0][1])
            else:
                ans = (n//2 - most_even[0][1]) +  (n//2 - most_odd[1][1])
        elif len(most_even) == 1 and len(most_odd) != 1:
            # most_evenの2番目は"0"
            if most_even[0][1] + most_odd[1][1] < (n//2 - most_even[0][1]) + most_odd[0][1]:
                ans = most_even[0][1] + (n//2 - most_odd[0][1])
            else:
                ans = (n//2 - most_even[0][1]) + (n//2 - most_odd[1][1])
        elif len(most_even) != 1 and len(most_odd) == 1:
            # most_oddの2番目は"0"
            if most_even[0][1] + (n//2 - most_odd[0][1]) < most_even[1][1] + most_odd[0][1]:
                ans = (n//2 - most_even[1][1]) + (n//2 - most_odd[0][1])
            else:
                ans = (n//2 - most_odd[0][1]) + most_even[0][1]
        else:
            # どっちも2番目は"0"
            if most_even[0][1] < most_odd[0][1]:
                ans = (n//2 - most_odd[0][1]) + n//2
            else:
                ans = n//2 + (n//2 - most_even[0][1])
else:
    ans = n - most_even[0][1] - most_odd[0][1]

print(ans)
