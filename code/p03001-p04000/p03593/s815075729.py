mod = 10 ** 9 + 7
mod2 = 2 ** 61 + 1
from collections import deque
import heapq
from bisect import bisect_left, insort_left, bisect_right

_NUMINT_ALL = list(range(10))


def main():
    ans = solve()

    if ans in [True, False]:
        YesNo(ans)
    elif ans is not None:
        print(ans)


def solve():
    H, W = iip(False)

    A = []
    for i in range(H):
        A.extend([i for i in input()])

    d = count_elements(A)

    a = 0
    b = 0
    for i in d.values():
        if i % 4 == 1:
            a += 1
        elif i % 4 == 2:
            b += 1
        elif i % 4 == 3:
            a += 1
            b += 1

    ans = True

    h = H % 2 == 0
    w = W % 2 == 0

    #print(a, b)

    if h and w:
        if a == 0 and b == 0:
            return True
        else:
            return False

    elif w:
        if b <= W/2 and a == 0:
            return True
        else:
            return False

    elif h:
        if b <= H/2 and a == 0:
            return True
        else:
            return False

    else:
        if b <= (H+W)/2 -1 and a <= 1:
            return True
        else:
            return False


#####################################################ライブラリ集ここから

def iip(listed=True, num_only=True):  # 数字のinputをlistで受け取る
    if num_only:
        ret = [int(i) for i in input().split()]
    else:
        ret = [int(i) if i in _NUMINT_ALL else i for i in input().split()]

    if len(ret) == 1 and not listed:
        return ret[0]
    return ret


def saidai_kouyakusuu(A):  # 最大公約数
    l = len(A)
    while True:
        m = min(A)
        mx = max(A)
        if m == mx:
            return m

        for i in range(l):
            if A[i] % m == 0:
                A[i] = m
            else:
                A[i] %= m


def sort_tuples(l, index):  # タプルのリストを特定のインデックスでソートする
    if isinstance(l, list):
        l.sort(key=lambda x: x[index])
        return l
    else:
        l = list(l)
        return sorted(l, key=lambda x: x[index])


def count_elements(l):  # リストの中身の個数を種類分けして辞書で返す
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def safeget(l, index, default="exception"):  # listの中身を取り出す時、listからはみ出たり
    if index >= len(l):                      # マイナスインデックスになったりするのを防ぐ
        if default == "exception":
            raise Exception("".join(["safegetに不正な値 ", index, "が渡されました。配列の長さは", len(l), "です"]))
        else:
            return default
    elif index < 0:
        if default == "exception":
            raise Exception("".join(["safegetに不正な値 ", index, "が渡されました。負の値は許可されていません"]))
        else:
            return default
    else:
        return l[index]


def iipt(l, listed=False, num_only=True):  # 縦向きに並んでいるデータをリストに落とし込む(iip利用)
    ret = []
    for i in range(l):
        ret.append(iip(listed=listed, num_only=num_only))
    return ret


def sortstr(s):  # 文字列をソートする
    return "".join(sorted(s))


def iip_ord(startcode="a"):  # 文字列を数字の列に変換する(数字と文字は1:1対応)
    if isinstance(startcode, str):
        startcode = ord(startcode)
    return [ord(i) - startcode for i in input()]


def YesNo(s):  # TrueFalseや1, 0をYesNoに変換する
    if s:
        print("Yes")
    else:
        print("No")


def fprint(s):  # リストを平たくしてprintする(二次元リストを見やすくしたりとか)
    for i in s:
        print(i)


def bitall(N):  # ビット全探索用のインデックスを出力
    ret = []
    for i in range(2 ** N):
        a = []
        for j in range(N):
            a.append(i % 2)
            i //= 2
        ret.append(a)
    return ret

def split_print_space(s):  # リストの中身をスペース区切りで出力する
    print(" ".join([str(i) for i in s]))


def split_print_enter(s):  # リストの中身を改行区切りで出力する
    print("\n".join([str(i) for i in s]))


def soinsuu_bunkai(n):  # 素因数分解
    ret = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
            ret.append(i)
        if i > n:
            break
    if n != 1:
        ret.append(n)
    return ret


def conbination(n, r, mod, test=False):  # nCrをmodを使って計算する
    if n <= 0:
        return 0
    if r == 0:
        return 1
    if r < 0:
        return 0
    if r == 1:
        return n
    ret = 1
    for i in range(n - r + 1, n + 1):
        ret *= i
        ret = ret % mod

    bunbo = 1
    for i in range(1, r + 1):
        bunbo *= i
        bunbo = bunbo % mod

    ret = (ret * inv(bunbo, mod)) % mod
    if test:
        # print(f"{n}C{r} = {ret}")
        pass
    return ret


def inv(n, mod):  #  modnにおける逆元を計算
    return power(n, mod - 2)


def power(n, p, mod_=mod):  # 繰り返し二乗法でn**p % modを計算
    if p == 0:
        return 1
    if p % 2 == 0:
        return (power(n, p // 2, mod_) ** 2) % mod_
    if p % 2 == 1:
        return (n * power(n, p - 1, mod_)) % mod_


if __name__ == "__main__":
    main()
