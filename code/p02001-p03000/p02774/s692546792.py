import sys
from itertools import count

def f(plus, minus, zero, val):
    t = 0
    if val > 0:
        t += len(plus) * len(minus) + zero * (len(plus) + len(minus)) + zero * (zero - 1) // 2
        # print(f'    zero {len(plus) * len(minus) + zero * (len(plus) + len(minus)) + zero * (zero - 1) // 2=}')
        if len(plus) >= 2:
            right_index = len(plus) -1
            for left_index, left in enumerate(plus):
                while left_index < right_index and left * plus[right_index] > val:
                    right_index -= 1
                t += max(0, right_index - left_index)
                # print(f'    plus {right_index-left_index=}')
        if len(minus) >= 2:
            left_index = 0
            for right_index, right in zip(count(len(minus) - 1, -1), reversed(minus)):
                while left_index < right_index and minus[left_index] * right > val:
                    left_index += 1
                t += max(0, right_index - left_index)
                # print(f'    minus {right_index-left_index=} {right_index=} {right=}')
    elif val < 0:
        if plus:
            plus_index = 0
            for m in minus:
                while plus_index < len(plus) and plus[plus_index] * m > val:
                    plus_index += 1
                t += len(plus) - plus_index
                # print(f'    mix {len(plus) - plus_index=}')
    else:
        t += len(plus) * len(minus) + zero * (len(plus) + len(minus)) + zero * (zero - 1) // 2
        # print(f'    zero {len(plus) * len(minus) + zero * (len(plus) + len(minus)) + zero * (zero - 1) // 2=}')
    # print(f'  {val=}, {t=}')
    return t


def resolve(in_):
    N, K = map(int, in_.readline().split())
    plus = []
    minus = []
    zero = 0
    for a in map(int, in_.readline().split()):
        if a > 0:
            plus.append(a)
        elif a < 0:
            minus.append(a)
        else:
            zero += 1

    plus.sort()
    minus.sort()

    ng = -(10 ** 18) - 1
    ok = 10 ** 18
    while ok - ng > 1:
        mid = (ok + ng) // 2
        # print(f'{ok=} {ng=} {mid=}')

        if f(plus, minus, zero, mid) >= K:
            ok = mid
        else:
            ng = mid

    # print(f'{ok=} {ng=} {mid=}')
    return ok


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
