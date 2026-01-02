#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def calc(d, mask, probs, g):
    score = 0
    ret = 0
    flags = [mask & (1<<i) for i in range(d)]
    for i in range(d):
        val = (i+1)*100
        p = probs[i][0]
        c = probs[i][1]
        if flags[i]:
            ret += p
            score += c+p*val
    if g <= score:
        return ret
    for i in range(d, -1, -1):
        val = i*100
        p = probs[i-1][0]
        c = probs[i-1][1]
        if flags[i-1]:
            continue
        else:
            if (g - score) > val*(p-1):
                score += val*(p-1)
                ret += p-1
            else:
                np = (g-score+val-1)//val
                score += val*np
                ret += np
                break
    if score < g:
        return 100000
    return ret

def main():
    d, g = rli()
    probs = []
    for i in range(d):
        p, c = rli()
        probs.append([p, c])
    ans = -1
    for i in range(2**d):
        ret = calc(d, i, probs, g)
        # print(bin(i), ret)
        if ans == -1:
            ans = ret
        else:
            ans = min(ans, ret)
    print(ans)


if __name__ == '__main__':
    main()
