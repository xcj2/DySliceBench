import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main(): 
    s = SI()
    t = SI()

    from collections import defaultdict
    s_dict = defaultdict(list)
    for i, char in enumerate(s):
        s_dict[char].append(i)

    # s_dict[char] には、 char が s の何番目に入っているかが記載されている。

    from bisect import bisect, bisect_left

    current_position = 0
    s_loops = 0
    first = True
    for char in t:
        li = s_dict[char]
        if not li:
            print(-1)
            return
        # current_position より大きい最小の要素を二分探索で得る。
        if first:
            first=False
            current_position = li[0]
        else:
            pos = bisect_left(li, current_position)
            try:
                if li[pos] == current_position:
                    current_position = li[pos+1]
                else:
                    current_position = li[pos]
            except IndexError:
                # s は次のループに入った。
                s_loops += 1
                current_position = li[0]
        # print(current_position)
    # if len(set(t)) == 1:
    #     add = 1
    # else:
    add = 1
    print(len(s)*s_loops + current_position+add)


main()