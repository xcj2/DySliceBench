#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 998244353


def set_depth(depth):
    global DEPTH, SEGTREE_SIZE, NONLEAF_SIZE
    DEPTH = depth
    SEGTREE_SIZE = 1 << DEPTH
    NONLEAF_SIZE = 1 << (DEPTH - 1)


def set_width(width):
    set_depth((width - 1).bit_length() + 1)


def get_size(pos):
    ret = pos.bit_length()
    return (1 << (DEPTH - ret))


def up(pos):
    pos += SEGTREE_SIZE // 2
    return pos // (pos & -pos)


def up_propagate(table, pos, binop):
    while pos > 1:
        pos >>= 1
        table[pos] = binop(
            table[pos * 2],
            table[pos * 2 + 1]
        )


def full_up(table, binop):
    for i in range(NONLEAF_SIZE - 1, 0, -1):
        table[i] = binop(
            table[2 * i],
            table[2 * i + 1])


def force_down_propagate(
    action_table, value_table, pos,
    action_composite, action_force, action_unity
):
    max_level = pos.bit_length() - 1
    size = NONLEAF_SIZE
    for level in range(max_level):
        size //= 2
        i = pos >> (max_level - level)
        action = action_table[i]
        if action != action_unity:
            action_table[i * 2] = action_composite(
                action, action_table[i * 2])
            action_table[i * 2 + 1] = action_composite(
                action, action_table[i * 2 + 1])
            # old_action = action_table[i * 2]
            # if old_action == action_unity:
            #     action_table[i * 2] = action
            # else:
            #     b1, c1 = old_action
            #     b2, c2 = action
            #     action_table[i * 2] = (b1 * b2, b2 * c1 + c2)

            # old_action = action_table[i * 2 + 1]
            # if old_action == action_unity:
            #     action_table[i * 2 + 1] = action
            # else:
            #     b1, c1 = old_action
            #     b2, c2 = action
            #     action_table[i * 2 + 1] = (b1 * b2, b2 * c1 + c2)

            action_table[i] = action_unity

            value_table[i * 2] = action_force(
                action, value_table[i * 2], size)
            value_table[i * 2 + 1] = action_force(
                action, value_table[i * 2 + 1], size)
            # b, c = action
            # value = value_table[i * 2]
            # value_table[i * 2] = (value * b + c * size) % MOD
            # value = value_table[i * 2 + 1]
            # value_table[i * 2 + 1] = (value * b + c * size) % MOD


def force_range_update(
    value_table, action_table, left, right,
    action, action_force, action_composite, action_unity
):
    """
    action_force: action, value, cell_size => new_value
    action_composite: new_action, old_action => composite_action
    """
    left += NONLEAF_SIZE
    right += NONLEAF_SIZE
    while left < right:
        if left & 1:
            value_table[left] = action_force(
                action, value_table[left], get_size(left))
            action_table[left] = action_composite(action, action_table[left])
            left += 1
        if right & 1:
            right -= 1
            value_table[right] = action_force(
                action, value_table[right], get_size(right))
            action_table[right] = action_composite(action, action_table[right])

        left //= 2
        right //= 2


def range_reduce(table, left, right, binop, unity):
    ret_left = unity
    ret_right = unity
    left += NONLEAF_SIZE
    right += NONLEAF_SIZE
    while left < right:
        if left & 1:
            ret_left = binop(ret_left, table[left])
            left += 1
        if right & 1:
            right -= 1
            ret_right = binop(table[right], ret_right)

        left //= 2
        right //= 2
    return binop(ret_left, ret_right)


def lazy_range_update(
        action_table, value_table, start, end,
        action, action_composite, action_force, action_unity, value_binop):
    "update [start, end)"
    L = up(start)
    R = up(end)
    force_down_propagate(
        action_table, value_table, L,
        action_composite, action_force, action_unity)
    force_down_propagate(
        action_table, value_table, R,
        action_composite, action_force, action_unity)

    force_range_update(
        value_table, action_table, start, end,
        action, action_force, action_composite, action_unity)
    up_propagate(value_table, L, value_binop)
    up_propagate(value_table, R, value_binop)


def lazy_range_reduce(
    action_table, value_table, start, end,
    action_composite, action_force, action_unity,
    value_binop, value_unity
):
    "reduce [start, end)"
    force_down_propagate(
        action_table, value_table, up(start),
        action_composite, action_force,  action_unity)
    force_down_propagate(
        action_table, value_table, up(end),
        action_composite, action_force, action_unity)

    return range_reduce(value_table, start, end, value_binop, value_unity)


def debug(*x):
    print(*x, file=sys.stderr)


def main():
    # parse input
    N, Q = map(int, input().split())
    AS = list(map(int, input().split()))
    set_width(N + 1)  # include N

    value_unity = 0
    value_table = [value_unity] * SEGTREE_SIZE
    value_table[NONLEAF_SIZE:NONLEAF_SIZE + len(AS)] = AS

    action_unity = None
    action_table = [action_unity] * SEGTREE_SIZE

    def action_force(action, value, size):
        if action == action_unity:
            return value
        # b, c = action
        b = action >> 32
        c = action - (b << 32)
        return (value * b + c * size) % MOD

    def action_composite(new_action, old_action):
        if new_action == action_unity:
            return old_action
        if old_action == action_unity:
            return new_action
        b1 = old_action >> 32
        c1 = old_action - (b1 << 32)
        # b1, c1 = old_action
        # b2, c2 = new_action
        b2 = new_action >> 32
        c2 = new_action - (b2 << 32)
        b = (b1 * b2) % MOD
        c = (b2 * c1 + c2) % MOD
        return (b << 32) + c

    def value_binop(a, b):
        return (a + b) % MOD
    full_up(value_table, value_binop)

    for _q in range(Q):
        q, *args = map(int, input().split())
        if q == 0:
            l, r, b, c = args
            lazy_range_update(
                action_table, value_table, l, r, ((b << 32) + c),
                action_composite, action_force, action_unity, value_binop)
        else:
            l, r = args
            print(lazy_range_reduce(
                action_table, value_table, l, r,
                action_composite, action_force, action_unity, value_binop, value_unity))


T1 = """
5 7
1 2 3 4 5
1 0 5
0 2 4 100 101
1 0 3
0 1 3 102 103
1 2 5
0 2 5 104 105
1 0 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
15
404
41511
4317767
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
