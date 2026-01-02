# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 19:42:05 2019

@author: Yamazaki Kenichi
"""

N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

tree = [[-1,-1,-1] for i in range(N)]
for i in range(N):
    tree[A[i][0]][1],tree[A[i][0]][2] = A[i][1],A[i][2]
    if A[i][1] != -1:
        tree[A[i][1]][0] = A[i][0]
    if A[i][2] != -1:
        tree[A[i][2]][0] = A[i][0]

def parent(u):
    return tree[u][0]
def lchild(u):
    return tree[u][1]
def rchild(u):
    return tree[u][2]
def depth(u):
    res = 0
    while parent(u) != -1:
        res += 1
        u = parent(u)
    return res
H = [-1 for i in range(N)]
def h(u):
    hl = h(lchild(u)) +1 if lchild(u) != -1 else 0
    hr = h(rchild(u)) +1 if rchild(u) != -1 else 0
    H[u] = max(hl,hr)
    return max(hl,hr)

for i in range(N):
    if parent(i) == -1:
        k = i
ans_pre = []
def pre(u):
    if u != -1:
        ans_pre.append(u)
    if lchild(u) != -1:
        pre(lchild(u))
    if rchild(u) != -1:
        pre(rchild(u))
pre(k)
ans_ino = []
def ino(u):
    if lchild(u) != -1:
        ino(lchild(u))
    if u != -1:
        ans_ino.append(u)
    if rchild(u) != -1:
        ino(rchild(u))
ino(k)
ans_pos = []
def pos(u):
    if lchild(u) != -1:
        pos(lchild(u))
    if rchild(u) != -1:
        pos(rchild(u))
    if u != -1:
        ans_pos.append(u)
pos(k)
print('Preorder')
print(" "+" ".join(map(str,ans_pre)))
print('Inorder')
print(" "+" ".join(map(str,ans_ino)))
print('Postorder')
print(" "+" ".join(map(str,ans_pos)))


