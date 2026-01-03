# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
s = input()[:-1]
ans = [1]*(N+2)


def print_ans(l: list):
    """
    T,Fからなる配列を受け取る
    T->S
    F->Wに変えて出力する
    """
    ret = ""
    for a in l[1:-1]:
        ret += "S" if a else "W"
    print(ret)


def next(ind: int, isSame: bool, isSheep: bool)->bool:
    """
    ind+1の動物を決める
    """
    if isSame:
        if isSheep:
            return ans[ind-1]
        else:
            return not ans[ind-1]
    else:
        if isSheep:
            return not ans[ind-1]
        else:
            return ans[ind-1]


def check(first: bool, last: bool)->list:
    """
    Lは動物の並び
    True;羊
    False:狼
    L=[L[-1],L[0],...]として、sの情報に従って隣を決めていく。
    最後まで行ったときに、最後の値がlastと一致するならok
    番兵的な
    """
    ans[0] = last
    ans[1] = first
    for i in range(1, N+1):
        ans[i+1] = next(i, s[i-1] == "o", ans[i])

    return ans[0] == ans[N] and ans[1] == ans[N+1]


for first in [True, False]:
    for last in [True, False]:
        if check(first, last):
            print_ans(ans)
            exit()
print("-1")
