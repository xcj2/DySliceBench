import copy
def prime_decomposition(n, table):
  i = 2
  while i * i <= n:
    c = 0
    while n % i == 0:
      n /= i
      c+=1
    if c!=0:
        if i not in table:
            table[i] = c
        else:
            table[i] += c
    i += 1
  if n > 1:
    if int(n) not in table:
        table[int(n)] = 1
    else:
        table[int(n)] += 1
  return table

table = {}
for i in range(int(input().strip())):
    table = prime_decomposition(i+1, table)

def find_224(ns, ttt, depth, counter):
    n_ttt = copy.deepcopy(ttt)
    if ns[depth] == 4:
        ccc = 0
        for i in n_ttt:
            if n_ttt[i] >= 4:
                ccc += 1
        return (ccc * (ccc -1) )// 2

    counter = 0
    for i in ttt:
        if ttt[i] >= ns[depth]:
            tmp = n_ttt[i]
            del n_ttt[i]
            counter += find_224(ns, n_ttt, depth + 1, counter)
            n_ttt[i] = tmp
    return counter

def find_n(ns, ttt, depth, counter):
    n_ttt = copy.deepcopy(ttt)
    counter = 0
    for i in ttt:
        if ttt[i] >= ns[depth]:
            if len(ns) == depth + 1:
                counter += 1
            else:
                tmp = n_ttt[i]
                del n_ttt[i]
                counter += find_n(ns, n_ttt, depth + 1, counter)
                n_ttt[i] = tmp
    return counter

# 553
res = 0
res += find_224([2, 4], table, 0, 0)

res += find_n([14, 4], table, 0, 0)
res += find_n([24, 2], table, 0, 0)
res += find_n([74], table, 0, 0)
print(res)
