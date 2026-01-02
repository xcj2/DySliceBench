#! /usr/bin/env python3

n, m = map(int, input().split())
p = [int(i) for i in input().split()]
pairs = [[int(i) for i in input().split()] for _ in range(m)]

parents = [i for i in range(n + 1)]

def ufRoot(a):
    global parents
    if parents[a] == a:
        return(a)
    else:
        parents[a] = ufRoot(parents[a])
        return parents[a]

def ufFind(a, b):
    return ufRoot(a) == ufRoot(b)

def ufUnite(a, b):
    global parents
    a = ufRoot(a)
    b = ufRoot(b)
    if (a == b):
        return
    parents[a] = b

for pp in pairs:
    if ufFind(pp[0], pp[1]) == False:
        ufUnite(pp[0], pp[1])

for i in range(len(parents)):
    parents[i] = ufRoot(parents[i])


uniques = list(set(parents))
dict_ids = {}
dict_values = {}

for u in uniques:
    dict_ids[u] = []
    dict_values[u] = []

for i in range(n):
    dict_ids[parents[i + 1]].append(i + 1)
    dict_values[parents[i + 1]].append(p[i])

res = 0
for u in uniques:
    sets = set(dict_ids[u]).intersection(dict_values[u])
    res += len(sets)

print(res)
