import sys

sys.setrecursionlimit(10000)

from collections import Counter
 
def parse_line(line, type=int):
    return [type(x) for x in line.split(' ')]
 
 
#              1, 2, 3, 4, 5, 6, 7, 8, 9
weight = ['x', 2, 5, 5, 4, 5, 6, 3, 7, 6]
 

def run(k, weight_to_num, cache):
    if k not in cache:
        if k <= 1:
            res = 0
        else:
            res = 0
            for w, num in weight_to_num.items():
                res = max(res, run(k - w, weight_to_num, cache))
            if res > 0:
                res += 1
            if k in weight_to_num:
                res = max(1, res)
        cache[k] = res
    return cache[k]
 
 
def main():
    n, m = parse_line(input())
    numbers = set(parse_line(input()))
    #numbers = [6, 8, 9]
 
    #for n in range(2, 60):
 
    if 6 in numbers and 9 in numbers:
        numbers.remove(6)
    if 2 in numbers and 3 in numbers:
        numbers.remove(2)
    if 2 in numbers and 5 in numbers:
        numbers.remove(2)
    if 3 in numbers and 5 in numbers:
        numbers.remove(3)
 
    weight_to_num = {weight[v]: v for v in numbers}
    cache = {}
    run(n, weight_to_num, cache)
    #print(cache)
    #return
 
    ws = list(weight_to_num.keys())
    ws.sort(reverse=True, key=lambda w: weight_to_num[w])
    res = []
    cache = {k:v for k,v in cache.items() if v > 0}
    cache[0] = 0
 
    if n not in cache:
        return
 
    l = cache[n]
    while l:
        for w in ws:
            if cache.get(n - w, 'False') == l - 1:
                res.append(weight_to_num[w])
                n = n - w
                l -= 1
                break
    print(''.join((str(x) for x in res)))
 
 
if __name__ == '__main__':
    main()

# 20 4
# 3 7 8 4