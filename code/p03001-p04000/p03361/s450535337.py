from sys import stderr
from functools import reduce
from operator import add
def f(): return [int(i) for i in input().split()]
def yes(n): print("Yes" if n else "No")
def debug(*x, sep=" ", end="\n"):
    for item in x:
        stderr.write(str(item))
        stderr.write(sep)
    stderr.write(end)

h, w = f()
target =  ['.'*(w+2)]
for _ in range(h):
    a = '.'
    a += input()
    a += '.'
    target.append(a)
target.append('.'*(w+2))
flag = True

for i in range(1, h+1):
    for j in range(1, w+1):
        if target[i][j] == '#':
            if '#' not in [target[i-1][j], target[i+1][j], target[i][j-1], target[i][j+1]]:
                flag = False
yes(flag)