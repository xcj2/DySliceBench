import heapq

def main():
    n, k, q = map(int, input().split())
    a = tuple(map(int, input().split()))

    m = float('inf')
    for y in sorted(set(a)):
        x = find_x(a, y, k, q)
        if x is None:
            break
        m = min(m, x - y)
    
    print(m)

def find_x(a, y, k, q):
    gs = groups(a, y, k)
    xs = []

    for g in gs:
        xs.extend(heapq.nsmallest(len(g) - k + 1, g))
    
    xss = heapq.nsmallest(q, xs)
    if len(xss) < q:
        return None
    
    return xss[-1]

def groups(a, m, k):
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