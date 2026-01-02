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

from itertools import combinations, permutations # https://docs.python.org/ja/3/library/itertools.html#itertools.combinations
# https://docs.python.org/ja/3/library/itertools.html#itertools.permutations
from collections import deque, Counter # https://docs.python.org/ja/3/library/collections.html#collections.deque
from heapq import heapify, heappop, heappush, heappushpop, heapreplace # https://docs.python.org/ja/3/library/heapq.html
from copy import deepcopy, copy # https://docs.python.org/ja/3/library/copy.html
import heapq
import copy
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

is_test = False
def debug_print(a,comments="",is_test=is_test):
    # debug_print([]) => []
    # debug_print("") => 
    # debug_print(a, "a is") => "a is:" print(a)
    if not is_test:
        pass
    elif not comments and a is None:
        print("")
    elif not comments:
        print(a)
    else:
        print(comments,":",a)

# setting the inputs
if is_test:
    n,k = [6, 8]
    vn = [-6, -100, 50, -2, -5, -3]
    # vn = [-10, 8, 2, 1, 2, 6]
else:        
    n,k = map(int,input().split())
    vn = [int(i) for i in input().split()]

hp = []
ans = 0
for i in range(min(k,n)+1):
    if i == 0:
        pass
    else:
        heapq.heappush(hp,vn[i-1])
    hpj = copy.deepcopy(hp)
    for j in range(min(k,n)-i+1):
        if j == 0:
            pass
        else:
            heapq.heappush(hpj,vn[n-j])
        hpjj = copy.deepcopy(hpj)
        debug_print(hpjj)
        counter = 0
        if i==0 and j==0:
            pass
        else:            
            while hpjj[0] < 0 and counter < k-i-j:
                counter += 1
                heapq.heappop(hpjj)
                if len(hpjj)==0:
                    break
        ans = max(ans, sum(hpjj))

print(ans)
