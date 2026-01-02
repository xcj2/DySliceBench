import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

# def can_reach(x, default_pos, x_moves):
#     for tries in range(2**len(x_moves)):  # x_moves は最大 4000, 2**100 で既に 10**30 なのでぜんぜん間に合わない。
#         result = default_pos
#         for digit in range(len(x_moves)):
#             result += (x_moves[digit] if tries & (1<<digit) else -x_moves[digit])
#         if result == x:
#             return True
#     return False

def can_reach(x_aim, default_pos, x_moves):  # ソートして貪欲？
    for i in sorted(x_moves, reverse=True):
        if x_aim > default_pos:
            default_pos += i
        else:
            default_pos -= i
    if default_pos == x_aim:
        return True
    else:
        return False

def main(): 
    s = SI()
    x, y = LI()

    x_moves = []
    y_moves = []
    moving_x = True
    for i in s.split('T'):
        if moving_x:
            x_moves.append(len(i))
        else:
            y_moves.append(len(i))
        moving_x = not moving_x

    if can_reach(x, x_moves[0], x_moves[1:]) and can_reach(y, 0, y_moves):
        print('Yes')
    else:
        print('No')


main()