#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class peak():
    def __init__(self, loc, elevation):
        self.loc = loc
        self.elevation = elevation
        self.next_high = None


def peak_append(peak_list, loc, elevation):
    p = peak(loc, elevation)
    peak_list.append(p)
    return

def peak_set_next_high(peak_list):
    next_high = peak_list[-1]   # last peak
    for i in range(len(peak_list)-2, -1, -1):
        peak_list[i].next_high = next_high
        if peak_list[i].elevation >= next_high.elevation:
            next_high = peak_list[i]


def find_flood(elev_list, peak_list):
    peak_p = peak_list.pop(0)
    next_high = peak_p.next_high
    if not next_high:
        return None, None
    q_elev = next_high.elevation
    p_elev = peak_p.elevation

    if p_elev > q_elev:
        q_offset = next_high.loc
        p_offset = peak_p.loc
        while p_offset < len(elev_list):
            if elev_list[p_offset] == elev_list[q_offset]:
                return p_offset, q_offset
            p_offset += 1
        else:
            return None, None
    else:
        p_offset = peak_p.loc
        q_offset = elev_list.index(p_elev, p_offset+1)
        return p_offset, q_offset
    raise "Logic Error"


def calc_area(p, q, elev_list):
    elev_0 = elev_list[p]
    area = 0

    prev_elev = 0
    for x in range(p, q+1):
        elev = elev_list[x] - elev_0
        area += elev

    return (abs(area))


def adjust_peak_list(q, peak_list):
    while peak_list:
        if peak_list[0].loc >= q:
            return
        peak_list.pop(0)


s = list(sys.stdin.readline().strip())

flood_area = list()
peak_list = list()

ascending = True
elevation = 0
elev_list = list()

for i in range(len(s)):
    elev_list.append(elevation)

    if s[i] == '_':
        pass
    elif s[i] == '/':
        ascending = True
        elevation += 1
    elif s[i] == '\\':
        if ascending:
            peak_append(peak_list, i, elevation)
        ascending = False
        elevation -= 1

elev_list.append(elevation)

if ascending:
    peak_append(peak_list, len(s), elevation)

peak_set_next_high(peak_list)

while peak_list:
    p, q = find_flood(elev_list, peak_list)
    if p == None:
        break
    flood_area.append(calc_area(p, q, elev_list))
    adjust_peak_list(q, peak_list)
    
print(sum(flood_area))
print(len(flood_area), end='')
for i in range(len(flood_area)):
    print(' ', flood_area[i], sep='', end='')
print()

