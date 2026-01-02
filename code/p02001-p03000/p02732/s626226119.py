GI = lambda: int(input()); GIS = lambda: map(int, input().split()); LGIS = lambda: list(GIS())

def count_unique_pairs(n):
    return n * (n - 1) // 2

def main():
    GI()
    arr = LGIS()

    d = {}
    for x in arr:
        d[x] = d.get(x, 0) + 1

    tot = sum(count_unique_pairs(v) for v in d.values())
    
    for x in arr:
        print(tot - count_unique_pairs(d[x]) + count_unique_pairs(d[x]-1))

def main():
    GI()
    arr = LGIS()

    d = {}
    for x in arr:
        d[x] = d.get(x, 0) + 1

    tot = sum(count_unique_pairs(v) for v in d.values())
    
    for x in arr:
        print(tot - d[x] + 1)

main()
