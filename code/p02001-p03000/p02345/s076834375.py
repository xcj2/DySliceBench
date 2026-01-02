import math
import sys

def make_tree(a: list, default: int, op):
    real_size = len(a)
    elem_size = 1 << math.ceil(math.log2(real_size))
    tree = [default] * elem_size + a + [default] * (elem_size - real_size)

    for i in range(elem_size-1, 0, -1):
        left, right = tree[i << 1], tree[(i << 1) + 1]
        tree[i] = op(left, right)

    return tree

def get_min(tree: list, x: int, y: int):
    result, elem_size = float("inf"), len(tree)//2
    l, r = x + elem_size, y + elem_size

    while l < r:
        if l & 1:
            result = tree[l] if tree[l] < result else result
            l += 1
        if r & 1:
            r -= 1
            result = tree[r] if tree[r] < result else result
        l, r = l >> 1, r >> 1

    return result

def set_value(tree: list, i: int, value: int, op):
    k = len(tree)//2 + i
    tree[k] = value

    while k > 1:
        k >>= 1
        left, right = tree[k << 1], tree[(k << 1) + 1]
        tree[k] = op(left, right)

if __name__ == "__main__":
    n, q = map(int, input().split())
    tree = make_tree([2**31-1]*n, 2**31-1, min)
    ans = []
    append = ans.append
    for com, x, y in (map(int, l.split()) for l in sys.stdin.readlines()):
        if com == 0:
            set_value(tree, x, y, min)
        else:
            append(get_min(tree, x, y+1))
    print(*ans, sep="\n")
