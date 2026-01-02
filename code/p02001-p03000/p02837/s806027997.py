#!/usr/bin/python3

import sys
import math

def input():
    return sys.stdin.readline().rstrip('\n')

N = int(input())

# honest_claims[claimer] = a list of honest persons who claimee claims
honest_claims = [0 for _ in range(N)]
unkind_claims = [0 for _ in range(N)]

for i in range(N):
    A = int(input())
    for _ in range(1,A+1):
        j,claim = list(map(int, input().split()))
        if claim == 1:
            honest_claims[i] |= 1<<(j-1)
        else:
            unkind_claims[i] |= 1<<(j-1)

#print([bin(i) for i in honest_claims])
#print([bin(i) for i in unkind_claims])

def get_unkind_claim(honests):
    unkinds = 0
    i = 0
    for _ in range(N):
        if honests & 1 > 0:
            unkinds |= unkind_claims[i]
        honests = honests >> 1
        i += 1
    return unkinds

def get_honest_claim(honests):
    honest_claim = 0
    i = 0
    for _ in range(N):
        if honests & 1 > 0:
            honest_claim |= honest_claims[i]
        honests = honests >> 1
        i += 1
    return honest_claim

def count_1(honests):
    count = 0
    while(honests>0):
        if honests & 1 > 0:
            count += 1
        honests = honests >> 1
    return count

max_honests = 0

for honests in range(1,2**N):
    unkind_claim = get_unkind_claim(honests)
    honest_claim = get_honest_claim(honests)
    if unkind_claim & honests > 0:
        continue
    if (honest_claim | honests) > honests:
        continue
    else:
        max_honests = max(max_honests, count_1(honests))

print(max_honests)
