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


ss = in_str()


def check(ss):
    i = 0
    j = len(ss)-1
    while i < j:
        if ss[i] != ss[j]:
            return False

        i+=1
        j-=1

    return True



n = len(ss)

if n%2 == 0:
    print('No')
else:
    if check(ss) and check(ss[:n//2]):
        print("Yes")
    else:
        print('No')


