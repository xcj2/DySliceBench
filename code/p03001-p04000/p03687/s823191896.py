import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
#======================================================#
def main():
    s = IS()
    cnt = len(s)
    for c in set(s):
        dist = 0
        max_d = 0
        for si in s:
            if c != si:
                dist += 1
            else:
                max_d = max(max_d, dist)
                dist = 0
        cnt = min(cnt, max(max_d, dist))
    print(cnt)

if __name__ == '__main__':
    main()