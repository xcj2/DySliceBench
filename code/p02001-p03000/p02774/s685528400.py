#!/usr/bin/env pypy3
import bisect
import sys
def input(): return sys.stdin.readline().rstrip()
 
 
def is_ok(arg, sei, hu, k):
    # 条件を満たすかどうか？問題ごとに定義
    count = 0
    for index, NN in enumerate(sei, 1):
        if NN==0:
            count+=len(sei)-index
        else:
            if NN**2 >= arg:
                break
            count += bisect.bisect_right(sei, ((arg)//NN))-index  # n以下の個数を数える
    for index, NN in enumerate(hu, 1):
        if NN**2 >= arg:
            break
        count += bisect.bisect_right(hu, ((arg)//NN))-index  # n以下の個数を数える
    return count >= k
 
 
def meguru_bisect(ng, ok, sei, hu, k):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, sei, hu, k):
            ok = mid
        else:
            ng = mid
    return ok
 
 
def is_ok2(arg, sei, hu, k):#seiとhuの組み合わせで-arg以上の数がk個あるか？
    # 条件を満たすかどうか？問題ごとに定義
    count = 0
    hulen=len(sei)
    for NN in hu:
        count += hulen-bisect.bisect_right(sei, ((-arg)-1)//NN)#n未満の個数を数える
    return count >= k
 
def meguru_bisect2(ng, ok, sei, hu, k):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok2(mid, sei, hu, k):
            ok = mid
        else:
            ng = mid
    return ok
 
def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    sei = []
    hu = []
    for AA in A:
        if AA >= 0:
            sei.append(AA)
        else:
            hu.append(-AA)
    sei.sort()
    hu.sort()
    seinum = len(sei)
    hunum = len(hu)
    if seinum*hunum < k:
        ans=meguru_bisect(-1, 10**18, sei, hu, k-seinum*hunum)
    else:
        ans=meguru_bisect2(-1*10**18, 0, sei, hu, k)
    print(ans)
 
if __name__ == '__main__':
    main()