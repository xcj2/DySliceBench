import sys


def num_patty(level):
    return 2 ** (level + 1) - 1


def num_all(level):
    return 2 ** (level + 2) - 3


def total_patty(n, x):
    res = 0
    pos = x - 1
    for cur_level in range(n + 1)[::-1]:
        print("L = {}, P = {}, R = {}: ".format(cur_level, pos, res), file=sys.stderr, end="")
        if cur_level == 0:
            print("level zero", file=sys.stderr)
            res += 1
            break
        prev_level_total = num_all(cur_level - 1)
        cur_level_total = num_all(cur_level)
        if pos == 0:
            print("left bread", file=sys.stderr)
            break
        elif 1 <= pos <= prev_level_total:
            print("left block", file = sys.stderr)
            pos -= 1
            continue
        elif pos == prev_level_total + 1:
            print("middle patty", file = sys.stderr)
            res += num_patty(cur_level - 1) + 1
            return res
        elif prev_level_total + 2 <= pos <= cur_level_total - 2:
            print("right block", file = sys.stderr)
            res += num_patty(cur_level - 1) + 1
            pos -= prev_level_total + 2
            continue
        else:
            print("right bread", file = sys.stderr)
            res += num_patty(cur_level)
            break
    return res


def main():
    n, x = (int(z) for z in input().split())
    res = total_patty(n, x)
    print(res)


if __name__ == "__main__":
    main()