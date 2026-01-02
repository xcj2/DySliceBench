#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools

def rdp_resolve(e: str) -> int:
    def evaluate() -> int:
        nonlocal p
        if e[p] in env:
            p += 1
            return env[e[p - 1]]
        if e[p] == '-':
            p += 1
            return 1 - evaluate()
        p += 1
        lval = evaluate()
        op = e[p]
        p += 1
        rval = evaluate()
        p += 1
        if op == '^':
            return lval ^ rval
        else:
            return lval & rval
    res = 0
    env = {"0": 0, "1": 1}
    for a, b, c, d in itertools.product(range(2), range(2), range(2), range(2)):
        env.update({"a": a, "b": b, "c": c, "d": d})
        p = 0
        res = (res << 1) | evaluate()
    return res

def rdp_init() -> None:
    global rdp_sessions
    rdp_sessions = dict()
    rookies = dict()
    for ch in "01abcd":
        rookies[rdp_resolve(ch)] = 1
    while rookies:
        rdp_sessions.update(rookies)
        entries = dict()
        for k, v in rookies.items():
            candidate = 0xFFFF - k
            weight = v + 1
            if weight <= 16 and weight <= rdp_sessions.get(candidate, 16) and weight <= entries.get(candidate, 16):
                entries[candidate] = weight
        for (k1, v1), (k2, v2) in itertools.product(rookies.items(), rdp_sessions.items()):
            candidate = k1 ^ k2
            weight = v1 + v2 + 3
            if weight <= 16 and weight <= rdp_sessions.get(candidate, 16) and weight <= entries.get(candidate, 16):
                entries[candidate] = weight
            candidate = k1 & k2
            weight = v1 + v2 + 3
            if weight <= 16 and weight <= rdp_sessions.get(candidate, 16) and weight <= entries.get(candidate, 16):
                entries[candidate] = weight
        rookies = entries

        
if __name__ == '__main__':
    rdp_init()
    while True:
        line = input()
        if line == '.':
            break
        print(rdp_sessions[rdp_resolve(line)])