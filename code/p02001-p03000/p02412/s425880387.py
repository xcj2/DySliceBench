def mapt(fn, *args):
    return tuple(map(fn, *args))
    

# def sum_num_is_x(n, x):
#     seen = set()
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             for c in range(1, n+1):
#                 if a != b and a != c and b != c:
#                     if a + b + c == x:
#                         k = tuple(sorted([a,b,c]))
#                         seen.add(k)
#     return len(seen)

from itertools import combinations


def sum_num_is_x(n, x):
    return len([row for row in combinations(range(1, n+1), 3) if sum(row)==x])

def Input():
    while True:
        n, x = mapt(int, input().split(" "))
        if n == x == 0: break
        print(sum_num_is_x(n, x))

Input()

