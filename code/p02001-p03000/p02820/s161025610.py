'''input
3 5
1 2 1
2 3 0
'''
# connected components
from sys import stdin, setrecursionlimit
from bisect import bisect_left
import sys, threading
#


def get_cost(m, h):
    if m == 'r':
        if h == 'p':
            return paper
    elif m == 's':
        if h == 'r':
            return rock
    else:
        if h == 's':
            return scissor
    return 0


def make(first, second):
    return str(first) + ' ' + str(second)


def brute(string, index, last, dp):
    if index == len(string):
        return 0
    x = -float('inf'); y = -float('inf'); z = -float('inf')
    if make(index, last) in dp:
        return dp[make(index, last)]
    if index != 0:
        if last != 'p':
            x = get_cost(string[index], 'p') + brute(string, index + 1, 'p', dp)
        if last != 's':
            y = get_cost(string[index], 's') + brute(string, index + 1, 's', dp)
        if last != 'r':
            z = get_cost(string[index], 'r') + brute(string, index + 1, 'r', dp)

    else:
        x = get_cost(string[index], 'p') + brute(string, index + 1, 'p', dp)
        y = get_cost(string[index], 's') + brute(string, index + 1, 's', dp)
        z = get_cost(string[index], 'r') + brute(string, index + 1, 'r', dp)
    dp[make(index, last)] = max(x, y, z)
    return max(x, y, z)

#
# def solve(string):
#     dp = [[0 for x in range(3)] for y in range(len(string))]
#     if string[0] == 'r':
#         dp[0] = [0, 0, paper]
#     elif string[0] == 's':
#         dp[0] = [rock, 0, 0]
#     else:
#         dp[0] = [0, scissor, 0]
#
#     for i in range(1, len(string)):
#         if string[i] == 'r':
#             dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])
#             dp[i][1] = max(dp[i - 1][0], dp[i - 1][2])
#             dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + paper
#         elif string[i] == 's':
#             dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + rock
#             dp[i][1] = max(dp[i - 1][0], dp[i - 1][2])
#             dp[i][2] = max(dp[i - 1][0], dp[i - 1][1])
#         else:
#             dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])
#             dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + scissor
#             dp[i][2] = max(dp[i - 1][0], dp[i - 1][1])
#     # print(dp)
#     return max(dp[-1])

# main starts
paper = 0
scissor = 0
rock = 0
def main():
    global paper, rock, scissor
    n, k = list(map(int, stdin.readline().split()))
    rock, scissor, paper = list(map(int, stdin.readline().split()))
    string = stdin.readline().strip()
    cost = 0
    for i in range(k):
        temp = []
        j = i
        while j < n:
            temp.append(string[j])
            j += k
        dp = dict()
        cost += brute(temp, 0, '$', dp)
    print(cost)

if __name__ == "__main__":
    sys.setrecursionlimit(200005)
    threading.stack_size(1 << 27)
    thread = threading.Thread(target=main)
    thread.start()