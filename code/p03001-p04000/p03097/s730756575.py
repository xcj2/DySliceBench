#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# AtCoder Grand Contest 031
# Problem C: Differ by 1 Bit

N, A, B = [int(t) for t in input().split()]

def grayCode(n):
    """nビットGrayコードの生成器"""
    for v in range(2 ** n):
        yield v ^ (v >> 1)

def grayCodeEnding(b, n):
    """0で始まりbで終わるnビットGrayコードの生成器"""
    code = list(grayCode(n))
    l = len(code)
    p = code.index(b)  # bの出現位置
    assert p % 2 == 1  # bの重みは奇数なので奇数番目に現れる

    # 両端から交互にyield
    q = 0
    while q != p:
        yield code[q]
        if q % 2 == 0:
            q = l - 1 - q
        else:
            q += 1 if q < p else -1

    # 残りを線形にyield
    q = l - 1 - q
    d = 1 if q < p else -1
    for i in range(q + d, p + d, d):
        yield code[i]

def weight(v):
    """vをNビット2進表記したときの1の個数"""
    return sum(1 for k in range(N) if (v & (1 << k)) != 0)

# 0 からB ^ A への系列を求めるのと本質的に同じ.
B ^= A

# Bの重みが偶数なら, 長さ 2 ** N の系列は存在しない.
if weight(B) % 2 == 0:
    print('NO')
    exit()

print('YES')
code = [A ^ c for c in grayCodeEnding(B, N)]
print(' '.join(str(c) for c in code))