def int_multiple():
    return  [int(c) for c in input().split()]

def int_single():
    return int(input())

def str_multiple():
    return [c for c in input().split()]

def str_single():
    return input()

# start
N = int_single()


hash = []

d = {}

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]

for i in range(N):
    tmp = str_single()
    checksum = 1
    for ch in tmp:
        checksum *= primes[ord(ch)-97]

    if checksum in d:
        d[checksum] += 1
    else:
        d[checksum] = 1

res = 0
for key in d:
    if d[key] >= 2:
        res += int((d[key] * (d[key] - 1)) / 2)

print(res)
