import sys
from collections import defaultdict

def load(vtype=int):
    return vtype(input().strip())

def load_list(seplator=" ", vtype=int):
    return [vtype(v) for v in input().strip().split(seplator)]

def exit():
    import sys
    sys.exit(0)

def kumiawase(li, used):
    if len(li) == len(used):
        return [[]]
    k = []
    for i in range(0, len(li)):
        if i in used:
            continue
        used.add(i)
        sub_list = kumiawase(li, used)
        for sub in sub_list:
            sub.append(li[i])
        k.extend(sub_list)
        used.discard(i)
    return k
        
n = load()
p = "".join(load_list(vtype=str))
q = "".join(load_list(vtype=str))

ks = kumiawase([i for i in range(n, 0, -1)], set())
ks = sorted(["".join([str(e) for e in k]) for k in ks])

a = ks.index(p) + 1
b = ks.index(q) + 1
print(abs(a-b))

