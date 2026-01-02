#%%
import sys
INPUT = sys.stdin.readline

def SINGLE_INT(): return int(INPUT())
def MULTIPLE_INT_LIST(): return list(map(int, INPUT().split()))
def MULTIPLE_INT_MAP(): return map(int, INPUT().split())
def SINGLE_STRING(): return INPUT()
def MULTIPLE_STRING(): return INPUT().split()

#%%

N, A, B, C = MULTIPLE_INT_MAP()
materials = [int(input()) for _ in range(N)]
INF = 10 ** 9

#%%

def dfs(cursor, a, b, c):  # cursor:カーソル a,b,c:現在の竹の長さ
    if cursor == N:  # cursorが最後まで行ったら終了する。
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) != 0 else INF
    # なぜ30を減じているのかというと、
    # dfs(0,0,0,0)で始まる以上、最初に選ばれるa,b,cを決定する際にもコストが10増加してしまうからである。

    # a,b,cのいずれかに1本も竹を利用していない場合は不適であるため、三項演算子を利用してその場合のコストをINFとする。

    # 再帰(4**N)
    # カーソルの当たっている竹に対して、(A or B or Cに合成する) or (合成しない)の場合に分ける
    no_compound = dfs(cursor+1, a, b, c)
    compound_to_a = dfs(cursor+1, a + materials[cursor], b, c) + 10
    compound_to_b = dfs(cursor+1, a, b + materials[cursor], c) + 10
    compound_to_c = dfs(cursor+1, a, b, c + materials[cursor]) + 10

    return min(no_compound, compound_to_a, compound_to_b, compound_to_c)

print(dfs(0, 0, 0, 0))