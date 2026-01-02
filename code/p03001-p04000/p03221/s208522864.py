import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n, m= LI()
    dic = collections.defaultdict(list)
    ans_lst = []

    for i in range(m):
        p, y = LI()
        dic[p].append((i, y))

    for key in dic.keys():
        dic[key].sort(key=lambda x: x[1])
        pfil = str(key).zfill(6)

        for i in range(len(dic[key])):
            id = pfil + str(i+1).zfill(6)
            ans_lst.append((dic[key][i][0], id))

    ans_lst.sort()
    ans = list(zip(*ans_lst))[1]
    print(*ans,sep="\n")
main()
