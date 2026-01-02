# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0147

"""
import sys
from sys import stdin
from heapq import heappop, heappush
from collections import deque
input = stdin.readline


class Seat():
    def __init__(self, n):
        self.seat = '_' * n

    def get(self, num):
        i = self.seat.find('_'*num)
        if i != -1:
            self.seat = self.seat[0:i] + 'o'*num + self.seat[i+num:]
            return i
        return None

    def release(self, i, num):
        self.seat = self.seat[0:i] + '_'*num + self.seat[i+num:]


def solve():
    waiting_time = [-1] * 100
    NUM_OF_SEAT = 17
    seat = Seat(NUM_OF_SEAT)
    LEAVE = 0
    COME = 1
    in_out = []                 #  ??\?????????????????????????????????
    Q = deque()                      #  ??§??????????????????
    # 100???????????\????????????????????????
    for group_id in range(100):
        if group_id % 5 == 1:
            num = 5
        else:
            num = 2
        heappush(in_out, (group_id * 5, COME, NUM_OF_SEAT+1, group_id, num))

    while in_out:
        time, event, start_seat, group_id, num = heappop(in_out)
        if event == COME:
            Q.append((time, group_id, num))
        else:
            seat.release(start_seat, num)
        while Q:
            res = seat.get(Q[0][2])
            if res is not None:
                arrive, group_id, num = Q.popleft()
                waiting_time[group_id] = time - arrive
                eating_time = 17 * (group_id % 2) + 3*(group_id % 3) + 19
                heappush(in_out, (time + eating_time, LEAVE, res, group_id, num))
            else:
                break
    return waiting_time


def main(args):
    waiting_time = solve()

    for line in sys.stdin:
        print(waiting_time[int(line)])


if __name__ == '__main__':
    main(sys.argv[1:])
    