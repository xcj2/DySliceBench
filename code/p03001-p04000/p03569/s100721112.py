import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
from collections import defaultdict #d = defaultdict(int) d[key] += value

def main():
    S = input()
    if S == S[::-1]:
        print(0)
        exit()
    l = len(S)
    T = S.replace('x', '')
    if T != T[::-1]:
        print(-1)
        exit()
    st, end = 0, l-1
    l = len(T) % 2
    cnt = 0
    while True:
        if S[st] == S[end]:
            if st+1!=end:
                st += 1
                end -= 1
            else:
                st=end
        elif S[st] == 'x':
            st += 1
            cnt += 1
        elif S[end] == 'x':
            end -= 1
            cnt += 1
        if st==end:
            break
    print(cnt)
    '''
    else:
        al = T[len(T)//2]
    pos_list = []
    for i in range(l):
        if S[i] == al:
            pos_list.append(i)
    cnt = 0
    if len(pos_list)%2 == 1:
        mid = pos_list[len(pos_list)//2]
        if mid>0:
            st = mid-1
        else:
            st = 0
        if mid<l-1:
            end = mid+1
        else:
            end = l-1
    else:
        mids = pos_list[len(pos_list)//2-1 : len(pos_list)//2+1]
        if mids[0]>0:
            st = mids[0]-1
        else:
            st = 0
        if mids[1]<l-1:
            end = mids[1]+1
        else:
            end = l-1
    flag = 0
    while True:
        if st==0 and end==l-1:
            flag = 1
        if S[st] == S[end]:
            if st > 0:
                st -= 1
            if end < l-1:
                end += 1
        elif S[st] == 'x':
            if st > 0:
                st -= 1
            cnt += 1
        elif S[end] == 'x':
            if end < l-1:
                end += 1
            cnt += 1
        if flag:
            break
    print(cnt)
    '''

if __name__ == "__main__":
    main()
