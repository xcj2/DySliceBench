import sys
stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)
import numpy as np

def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
# 入力全てを整数に変換したものの配列を受け取る
def LI(): return list(map(int, sys.stdin.readline().split()))
# 入力全てを整数に変換して1引いたものの配列を受け取る
def LLI(rows_number): return [LI() for _ in range(rows_number)]

k = int(input())
m = []
flatten = lambda x: [str(z) for y in x for z in (flatten(y) if hasattr(y, '__iter__') and not isinstance(y, str) else (y,))]

ll = [str(i) for i in range(1,10)]
o = []
for s in ll:
    l = []
    l.append(s)
    for i in range(10):
        p = []
        for j in l[-1]:
            t = []
            if str(j[-1])=='0':
                t.append(j+'0')
                t.append(j+'1')
            elif str(j[-1])=='9':
                t.append(j+'8')
                t.append(j+'9')
            else:
                t.append(j+str(int(j[-1])-1))
                t.append(j+str(int(j[-1])))
                t.append(j+str(int(j[-1])+1))
            p.append(t)
        l.append(flatten(p))
    o.append(l)

flatten = lambda x: [int(z) for y in x for z in (flatten(y) if hasattr(y, '__iter__') and not isinstance(y, str) else (y,))]

#print(sorted(set(flatten(o))))
print(sorted(set(flatten(o)))[k-1])
