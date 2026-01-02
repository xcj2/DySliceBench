import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def main():

    n,x,MOD = get_nums_l()

    ans = x
    now = x

    known = {x}
    history = [x]

    for i in range(1, n):
        y = now**2 % MOD
        if y in known:
            # ループ長と合計を検出する
            last_known = i-1
            loop_sum = y
            while history[last_known] != y:
                loop_sum += history[last_known]
                last_known -= 1
            loop_len = i - last_known

            ans += (n-i) // loop_len * loop_sum

            # log(loop_len, loop_sum)

            for j in range((n-i) % loop_len):
                if (last_known + j) < len(history):
                    ans += history[last_known + j]
            break

        known.add(y)
        history.append(y)
        ans += y
        now = y
    
    print(ans)


main()