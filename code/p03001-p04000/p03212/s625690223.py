def next(n):
    # nの次に小さい、3と7と5しか出てこない数
    s = str(n)
    if s[-1] == "3":
        return int(s[:-1] + "5")
    if s[-1] == "5":
        return int(s[:-1] + "7")
    # s[-1] == "7"
    if len(s) == 1:
        return 33
    else:
        s = str(next(s[:-1]))
        return int(s + "3")

def is_753(n):
    # 3, 7, 5 がすべて表れているかを判定
    s = str(n)
    if "3" in s and "5" in s and "7" in s:
        return True
    return False

def next_753(n):
    # 次の753数を返す
    while True:
        n = next(n)
        if is_753(n):
            return n

N = int(input())
ans = 0
n = 357
while n <= N:
    ans += 1
    n = next_753(n)
print(ans)