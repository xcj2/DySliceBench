#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def convert(i, n):
    ret = []
    for j in range(n):
        if i & (1<<j):
            ret.append(1)
        else:
            ret.append(0)
    return ret

def check(tf, people):
    for i in range(len(people)):
        if not tf[i]:
            continue
        for j in range(len(people[i])):
            say = people[i][j]
            if say[1] != tf[say[0]]:
                return False
    return True

def main():
    n = ri()
    people = []
    for i in range(n):
        a = ri()
        say = []
        for j in range(a):
            x, y = rli()
            x -= 1
            say.append([x, y])
        people.append(say)
    ans = 0
    for i in range(pow(2, n)):
        tf = convert(i, n)
        ok = check(tf, people)
        if not ok:
            continue
        ans = max(ans, sum(tf))
    print(ans)


if __name__ == '__main__':
    main()
