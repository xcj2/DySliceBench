import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def II(): return int(sys.stdin.readline())


from collections import deque

from copy import copy
#debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)
def main():
    N = II()
    a_mat = []
    for i in range(N):
        a_mat.append(deque(LI()))

    cnt = 0
    first_list = [a_list.popleft() for a_list in a_mat]
    nend = 0
    previous_match_list = list(range(N))
    while True:
        # この日に試合できる可能性リスト
        # 試合する人リスト
        match_list = []
        for i in previous_match_list:
            a_no = first_list[i]
            a = a_no-1
            no = i+1
            # 試合をするペアの要素を入れていく
            if first_list[a] == no:
                match_list.append(i)

        dprint(first_list, match_list)

        if len(match_list) == 0:
            print(-1)
            return

        previous_match_list = copy(match_list)

        # 試合をしたことを反映
        for i in match_list:
            if len(a_mat[i]) == 0:
                first_list[i] = 0
                nend += 1 # 終わった人
            else:
                next_no = a_mat[i].popleft()
                next = next_no - 1
                first_list[i] = next_no
                previous_match_list.append(next)

        previous_match_list = list(set(previous_match_list))

        dprint(match_list, previous_match_list)
        dprint("")
        # 一日経過
        cnt += 1

        # 終了判定
        if nend == N:
            break


    print(cnt)


main()