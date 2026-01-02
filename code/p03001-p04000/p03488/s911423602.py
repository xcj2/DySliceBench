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

# def can_reach(x, default_pos, x_moves):  # 全探索
#     for tries in range(2**len(x_moves)):  # x_moves は最大 4000, 2**100 で既に 10**30 なのでぜんぜん間に合わない。
#         result = default_pos
#         for digit in range(len(x_moves)):
#             result += (x_moves[digit] if tries & (1<<digit) else -x_moves[digit])
#         if result == x:
#             return True
#     return False

# def can_reach(x_aim, default_pos, x_moves):  # ソートして貪欲 → ACだが嘘解法かもしれない。
#     for i in sorted(x_moves, reverse=True):
#         if x_aim > default_pos:
#             default_pos += i
#         else:
#             default_pos -= i
#     if default_pos == x_aim:
#         return True
#     else:
#         return False

# def can_reach(x_aim, default_pos, x_moves):  # dp → TLE
#     def dp(i, pos):
#         if i == 0:
#             if pos == default_pos: return True
#             else: return False
#         else:
#             return dp(i-1, pos - x_moves[i-1])  or dp(i-1, pos + x_moves[i-1])

#     return dp(len(x_moves), x_aim)

# def can_reach(x_aim, default_pos, x_moves):  # dp with table → TLE
#     dp = [[False for _ in range(20000)] for _ in range(len(x_moves)+1)]  # 20000 * 8000 = O(10**8) ぐらい
#     def read_dp(i, j):
#         return dp[i][j+10000]
#     def write_dp(i, j, k):
#         dp[i][j+10000] = k
#     write_dp(0, default_pos, True)
#     for i in range(len(x_moves)):
#         for j in range(20000):
#             if dp[i][j] == True:
#                 dp[i+1][j+x_moves[i]] = True
#                 dp[i+1][j-x_moves[i]] = True
#     return read_dp(len(x_moves), x_aim)
    

def can_reach(x_aim, default_pos, x_moves):  # dp with set → AC
    dp = set([default_pos])
    for i in x_moves:
        new_dp = []
        for j in dp:
            new_dp.append(j+i)
            new_dp.append(j-i)
        dp = set(new_dp)
    return x_aim in dp


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