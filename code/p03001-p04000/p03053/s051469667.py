#!/usr/bin python3
# -*- coding: utf-8 -*-

from collections import deque

H, W = map(int,input().split())

INF = -1
Gmap = [list(input()) for _ in range(H)]
next_q = deque([])

def dfs_settings():
    #複数
    for h in range(H):
        for w in range(W):
            if Gmap[h][w]=='#':
                next_q.append([h,w])
                Gmap[h][w]=0

def dfs():
    ret = 0
    while len(next_q)!=0:
        #スタック取り出し(先頭)幅優先
        h,w = next_q.popleft()
        lv=Gmap[h][w]+1
        hs, ws = h + 0 , w + 1
        if ws<W and Gmap[hs][ws]=='.':
            next_q.append([hs,ws])
            Gmap[hs][ws] = lv
            ret = max(ret, Gmap[hs][ws])
        hs, ws = h + 1 , w + 0
        if hs<H and Gmap[hs][ws]=='.':
            next_q.append([hs,ws])
            Gmap[hs][ws] = lv
            ret = max(ret, Gmap[hs][ws])
        hs, ws = h + 0 , w - 1
        if ws>=0 and Gmap[hs][ws]=='.':
            next_q.append([hs,ws])
            Gmap[hs][ws] = lv
            ret = max(ret, Gmap[hs][ws])
        hs, ws = h - 1 , w + 0
        if hs>=0 and Gmap[hs][ws]=='.':
            next_q.append([hs,ws])
            Gmap[hs][ws] = lv
            ret = max(ret, Gmap[hs][ws])
    return ret

def main():
    dfs_settings()
    ret = dfs()
    print(ret)

if __name__ == '__main__':
    main()
