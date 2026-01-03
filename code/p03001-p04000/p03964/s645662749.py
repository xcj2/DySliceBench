from collections import namedtuple

Report = namedtuple('Report', ['a', 'b'])

def main():
    n = int(input())
    reports = []
    for _ in range(n):
        a, b = map(int, input().split())
        reports.append(Report(a, b))
    
    print(solve(reports))

def solve(reports):
    x, y = reports[0].a, reports[0].b

    for a, b in reports[1:]:
        c = ceil(x, a)
        d = ceil(y, b)
        if d // b * a > c:
            x = d // b * a
            y = d
        else:
            x = c
            y = c // a * b
    
    return x + y

def ceil(x, y):
    r = x % y
    if r == 0:
        return x
    else:
        return x + y - r

main()
