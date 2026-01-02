import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


############ ---- Input Functions ---- ############
def in_int():
    return (int(input()))


def in_list():
    return (list(map(int, input().split())))


def in_str():
    s = input()
    return (list(s[:len(s) - 1]))


def in_ints():
    return (map(int, input().split()))




n = in_int()

a = in_list()

m = {}
max_1 = 0
val_1 = -1
max_2 = 0
val_2 = -1
for xx in a:
    if xx in m:
        m[xx]+=1
    else:
        m[xx] = 1


ans = 0

for xx in m:
    tt = m[xx]
    ans += tt*(tt-1)//2



for xx in a:
    tt = m[xx]

    print(ans - (tt)*(tt-1)//2 + (tt-1)*(tt-2)//2)