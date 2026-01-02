import heapq

def main():
    _, k, q = map(int, input().split())
    a = tuple(map(int, input().split()))

    gs = [a]
    m = float('inf')
    for y in sorted(set(a)):
        gs = groups(gs, y, k)
        x = find_x(gs, y, k, q)
        if x is None:
            break
        m = min(m, x - y)
    
    print(m)

def find_x(gs, y, k, q):
    xs = []

    for g in gs:
        xs.extend(heapq.nsmallest(len(g) - k + 1, g))
    
    xss = heapq.nsmallest(q, xs)
    if len(xss) < q:
        return None
    
    return xss[-1]

def groups(gs, m, k):
    new_gs = []
    for g in gs:
        new_gs.extend(groups_1(g, m, k))
    return new_gs

def groups_1(a, m, k):
    g = []

    pos = 0
    while pos < len(a):
        i = pos
        while i < len(a) and a[i] < m:
            i += 1
        
        j = i
        while j < len(a) and a[j] >= m:
            j += 1
        
        if j - i >= k:
            g.append(a[i:j])
        
        pos = j
    
    return g

main()