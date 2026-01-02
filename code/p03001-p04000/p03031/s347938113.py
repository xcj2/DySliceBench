# Technique often used
# enumerate: for i, a in enumerate(a_list):
# Functional Programming: filter, map, reduce

# naming conventions
# if [s_1, s_2, s_3, ..., s_k] then I name this list sk
# if [[s_11, s_12, ..., s_1k], ..,[s_j1, s_j2, ..., s_jk] then I name this list sjk
# if something strange in list then I add _ to list's name (ex:sjk_)

# visual studio code shortcut https://qiita.com/TakahiRoyte/items/cdab6fca64da386a690b
# delete line: Ctrl+Shift+k
# choose same words: Ctrl+Shift+l

from itertools import combinations # https://docs.python.org/ja/3/library/itertools.html#itertools.combinations
from itertools import permutations # https://docs.python.org/ja/3/library/itertools.html#itertools.permutations
from collections import deque # https://docs.python.org/ja/3/library/collections.html#collections.deque
def gcd(a,b):
    if b==0:return a
    return gcd(b,a%b)
def gcds(a):
    if len(a)==1:
        return a[0]
    else:
        element = gcd(a[0], a[1])
        if len(a)==2:return(element)
        else:
            for i in range(2,n):
                element=gcd(element,a[i])
            return(element)
def debug_print(word,a,is_test=False):
    if is_test and not word:
        print("")
    elif is_test:
        print(word,a)
    else:
        pass

is_test = False
if is_test:
    n,m = [2, 2]
    smk_ = [[2, 1, 2],[1, 2]]
    pm = [0, 1]
else:        
    n,m = map(int,input().split())
    smk_ = [[int(i) for i in input().split()] for j in range(m)]
    pm = [int(i) for i in input().split()]

subsets=[]
# exclude empty set (think about it later)
for i in range(n):
    for c in combinations(range(n), i+1):
        subsets.append(c)
debug_print("subsets",subsets,is_test)

ans = 0
for subset in subsets:
    for i_m, sk_ in enumerate(smk_):
        counter = 0
        for sub in subset:
            debug_print("sub",sub,is_test)
            debug_print("sk_[1:]",sk_[1:],is_test)
            debug_print("pm[i_m]",pm[i_m],is_test)
            if sub + 1 in sk_[1:]:
                counter += 1
                debug_print("counter",counter,is_test)
            debug_print("","",is_test)
        if counter % 2 != pm[i_m]:
            debug_print("break: i_m=",i_m,is_test)
            break
    else:
        ans += 1

# think about empty set (if all switches are off)
if not(any(pm)):
    ans += 1

print(ans)