def memoize(f):  
    cache = {}  
    def helper(x):  
        if x not in cache:              
            cache[x] = f(x)  
        return cache[x]  
    return helper 

def split_rc(rc):
    for i in range(1, len(rc)):
        yield rc[:i], rc[i:]

@memoize
def cost(rc):
    if len(rc) == 1:
        return 0
    return min(calc_cost(first, second) for first, second in split_rc(rc))

def calc_cost(first, second):
    return cost(first) + cost(second) + first[0][0] * first[-1][1] * second[-1][1]

n = int(input())
rc = tuple(tuple(map(int, input().split())) for _ in range(n))
print(cost(rc))