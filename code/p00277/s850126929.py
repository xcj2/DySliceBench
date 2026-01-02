# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0282

"""
import sys
from sys import stdin
from heapq import heappop, heappush
input = stdin.readline


pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = float('inf')      # placeholder for a removed task

def add_team(score, team):
    if team in entry_finder:
        remove_team(team)
    entry = [-score, team]
    entry_finder[team] = entry
    heappush(pq, entry)

def remove_team(team):
    entry = entry_finder.pop(team)
    entry[-1] = REMOVED

def pop_team():
    while pq:
        score, team = heappop(pq)
        if team is not REMOVED:
            del entry_finder[team]
            return score, team
    raise KeyError('pop from an empty priority queue')


def main(args):
    N, R, L = map(int, input().split(' '))
    on_tv = [0] * (N + 1)       #  ????????????????????¬???????????£??????????????????????¨?
    scores = [0] * (N + 1)       #  ????????????????????¨?????????

    #for i in range(1, N+1):
    #    add_team(0, i)
    
    add_team(0, 1)

    last_time = 0
    need_pop = True
    top_score = 0

    for i in range(R):
        d, t, x = [int(x) for x in input().split(' ')]
        if need_pop:
            need_pop = False
            top_score, team = pop_team()
            if d != team:
                add_team(scores[team], team)

        on_tv[team] += (t - last_time)

        scores[d] += x
        add_team(scores[d], d)
        if x > 0 and scores[d] > top_score:
            need_pop = True

        last_time = t

    t = L
    score, team = pop_team()
    on_tv[team] += (t - last_time)

    print(on_tv.index(max(on_tv)))


if __name__ == '__main__':
    main(sys.argv[1:])