def parentNode(k):
    return k // 2

def leftNode(k):
    return 2 * k 

def rightNode(k):
    return 2 * k + 1

H = int(input())
elems = [0] + [int(x) for x in input().split()]

for k in range(1, H+1):
    print(f'node {k}: ', end = '')
    print(f'key = {elems[k]}, ', end = '')
    if parentNode(k) >= 1:
        print(f'parent key = {elems[parentNode(k)]}, ', end = '')
    if leftNode(k) <= H:
        print(f'left key = {elems[leftNode(k)]}, ', end = '')
    if rightNode(k) <= H:
        print(f'right key = {elems[rightNode(k)]}, ', end = '')
    print()

