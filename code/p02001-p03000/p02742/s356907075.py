import sys
from collections import defaultdict
from collections import deque
def load(vtype=int):
    return vtype(input().strip())
def load_list(seplator=" ", vtype=int):
    return [vtype(v) for v in input().strip().split(seplator)]
def exit():
    import sys
    sys.exit(0)
def perm_sub(li, used):
    if len(li) == len(used):
        return [deque()]
    k = []
    for i in range(len(li)):
        if i in used:
            continue
        used.add(i)
        sub_list = perm_sub(li, used)
        for sub in sub_list:
            sub.appendleft(li[i])
        k.extend(sub_list)
        used.discard(i)
    return k
def perm_li(li):
    return perm_sub(li, set())
def perm_n(n):
    return perm_sub(list(range(n)), set())
def join_i(li, sep=""):
    return sep.join([str(e) for e in li])
def li2n(li):
    n, base = 0, 1
    for i in range(len(li)-1, -1, -1):
        n += li[i] * base
        base *= 10
    return n
def sli2ili(li):
    return [int(s) for s in li] 

h, w = load_list()
if h == 1 or w == 1:
    print(1)
    exit()
if h*w % 2 == 0:
    print(int(h*w/2))
else:
    print(int((h*w+1)/2))
