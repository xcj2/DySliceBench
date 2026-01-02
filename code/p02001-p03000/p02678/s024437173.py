# import sys
# input = sys.stdin.readline
import itertools
import collections


# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    n, m = input_list()
    rooms = []
    for _ in range(m):
        rooms.append(input_list())
    prev = [0]*n
    to_list = [[] for i in range(n)]
    for a, b in rooms:
        to_list[a-1].append(b-1)
        to_list[b-1].append(a-1)
    next_q = collections.deque()
    flags = [-1] * n
    flags[0] = 999
    next_q.append(0)
    while next_q:
        cur = next_q.popleft()
        for room in to_list[cur]:
            if flags[room] == -1:
                flags[room] = cur
                next_q.append(room)
    print('Yes')
    for i in range(1, n):
        print(flags[i]+1)


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
