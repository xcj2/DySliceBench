
IN = list(map(int, input().split()))
N, K = IN[0], IN[1]
P = [None] + list(map(int, input().split()))
C = [None] + list(map(int, input().split()))
MAX_N = 45000
#N = 1000
#K = 10**7
#P = [None] + [random.choice(list(itertools.chain(range(1,i), range(i+1,N)))) for i in range(1, N+1)]
#C = [None] + random.choices(range(-10**9, 10**9), k=N)

verbose = False

def cumsum(a):
    tmp = [0]*(len(a)+1)
    for i in range(1, len(a)+1): tmp[i] = a[i-1] + tmp[i-1]
    return tmp[1:]

def find_cycle(p, pos):
    cnt = 0
    steps = [0] * (MAX_N+1)
    path = [False] * (MAX_N+1)
    while True:
        steps[cnt] = pos
        path[pos] = True
        cnt += 1
        pos = p[pos]
        if path[pos]: break # found closure
    st = steps.index(pos) # start of closure
    return [steps[:st], steps[st:cnt]]


def score(steps, c):
    ret = [0]*len(steps)
    for i in range(len(steps)): ret[i] = c[steps[i]]
    return ret

maxsc = -10**9-1
done = [False] * (N+1)
for i in range(1, N+1):
    if verbose: print('entering', i)
    if done[i]: continue
    [preclosure_path, closure_path] = find_cycle(P, i)
    if verbose: print('closure found:', closure_path)
    closure_scores = score(closure_path, C)
    preclosure_scores = score(preclosure_path, C)
    closure_score = sum(closure_scores)
    preclosure_len, closure_len = len(preclosure_path), len(closure_path)

    cycles = (K-preclosure_len)//closure_len
    resid = (K-preclosure_len)%closure_len
    if cycles>=1: cycles -= 1
    abbrev = closure_score * cycles
   
    trail = preclosure_scores + closure_scores * 3
    path = preclosure_path + closure_path*3
    if verbose: print('score trail:', trail)
    if verbose: print('path:', preclosure_path + closure_path*3)
    if verbose: print('mark:', mark)
    mark = min(K, len(preclosure_path+closure_path)+resid)
    localmax = max(cumsum(trail[0:mark])) + max(0, closure_score*cycles)
    if verbose: print('localmax:', localmax, 'cycles:', cycles)
    maxsc = max(localmax, maxsc)

    if verbose: print('going greedy')
    for j in range(1, closure_len):
        if K<=mark+j: break
        target = path[j]
        if done[target]: continue
        localmax = max(cumsum(trail[j:mark+j])) + max(0, closure_score*cycles)
        maxsc = max(localmax, maxsc)
        done[target] = True
        if verbose: print('done:', target, 'with', localmax)

print(maxsc)
