#!/usr/bin/env python3
import sys
def read(): return sys.stdin.readline() # 標準入力
def fbit(i, j=-1): return format(i, 'b').zfill(j) # bit 表示
def popcount(x): # ビットカウント
    x=x-((x>>1)&0x5555555555555555)
    x=(x&0x3333333333333333)+((x>>2)&0x3333333333333333)
    x=(x+(x>>4))&0x0f0f0f0f0f0f0f0f;x=x+(x>>8);x=x+(x>>16);x=x+(x>>32)
    return x&0x0000007f


def solv(N:int, M: int, k:list, s: list, p: list):
    ans = 0
    for bits in range(1<<N): # スイッチの状態を全て列挙(bit全探査)
        # ビットの数をカウント
        # count = popcount(bits)
        flag = True
        for i in range(M): # 点灯条件 M[i]でpopcount%2=p[i]
            # マスクビット用のmaskを作成
            mask = 0
            # 各電球の利用可能スイッチをマスクで取得 => 1,2 なら　0b11とか
            for j in s[i]:
                mask = mask|1<<(j-1)
            # print(fbit(mask))
            # ビットカウント => 条件分岐
            if not popcount(bits&mask)%2==p[i]: flag = False
        if flag: ans += 1
    print(ans)

def main():
    [N, M] = list(map(int, read().rsplit()))
    k = []; s = []
    for i in range(M):
        _tmp = list(map(int, read().rsplit()))
        k.append(_tmp.pop(0))
        s.append(_tmp)

    p = list(map(int, read().rsplit()))
    solv(N, M, k, s, p)


if __name__ == '__main__':
    main()



2&3
