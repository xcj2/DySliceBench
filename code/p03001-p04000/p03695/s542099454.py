#!/usr/bin/env python3

def main():
    n = int(input())
    an = list(map(int, input().split()))
    colors = [color(a) for a in an]
    mi = max(1, count_colors(colors))
    ma = count_colors(colors) + free_players(colors)
    print(mi, ma)

def color(r):
    assert 1 <= r <= 4800
    if r < 400:
        return "grey"
    elif r < 800:
        return "brown"
    elif r < 1200:
        return "green"
    elif r < 1600:
        return "sky"
    elif r < 2000:
        return "blue"
    elif r < 2400:
        return "yellow"
    elif r < 2800:
        return "orange"
    elif r < 3200:
        return "red"
    else:
        return "free"

def count_colors(colors):
    res = set(colors)
    res -= {"free"}
    return len(res)

def free_players(colors):
    res = 0
    for c in colors:
        if c == "free":
            res += 1
    return res

main()
