#####################################################################################################
##### 深さ優先探索 幅優先探索　（グラフ）
#####################################################################################################

'''

キューに頂点を入れる回数は各々高々１回のみ。
各辺を使う回数は高々一回のみ（辺を戻るような探索は枝切りされている）
結果として、計算量はO(N + M)

'''

from collections import deque
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline



def bfs(conj, start, goal=None, visit=set()):
    visit.add(start)                            # スタート地点はすでに訪れている
    next_set = deque([(start, 0)])              # 次に進む候補を列挙する。スタック（右から取り出す = pop）だと深さ優先になり、キュー（左から取り出す = popleft）だと幅優先になる
                                                # 第一成分はスタート地点、第二成分は時刻を表す。
    while next_set:                             # p = [] になったら止める
        p, t = next_set.popleft()               # 要素を消去して、消去した要素を出力
        for q in conj[p]:                       # 頂点 p から進める経路の候補から一つ選ぶ
            if q in visit:                      # 一度訪れていた場合は進まない
                continue
            if q == goal:                       # ゴールがあるならば、ここで判定
                return t + 1                    # 経路の長さは t + 1 で与えられる
            visit.add(q)                        # 頂点 q に一度訪れた事をメモ (for の前に書くと、ここで選ばれた q が最短であるはずなのに、違う経路でvisit = Trueを踏んでしまう可能性がある)
            next_set.append((q, t + 1))         # p から q へと移動。時刻を 1 進める
    return -1


def connection_counter(conj):                   # conj の連結成分の個数を返す。関数 bfs が必要
    cnt = 0
    visit = set()
    for start in range(N):
            if start not in visit:
                cnt += 1
                bfs(start, conj, visit)
    return cnt


def distance_list(conj, start, visit=set()):    # スタート地点からの距離の全列挙
    dist = [0]*N
    visit.add(start)
    next_set = deque([(start, 0)])
    while next_set:
        p, t = next_set.popleft()
        for q in conj[p]:
            if q in visit:
                continue
            dist[q] = t+1
            visit.add(q)
            next_set.append((q, t + 1))
    return dist


def dfs(conj, start, goal=None, visit=set()):
    visit.add(start)                            # スタート地点はすでに訪れている
    next_set = [(start, 0)]                     # 次に進む候補を列挙する。スタック（右から取り出す = pop）だと深さ優先になり、キュー（左から取り出す = popleft）だと幅優先になる
                                                # 第一成分はスタート地点、第二成分は時刻を表す。
    while next_set:                             # p = [] になったら止める
        p, t = next_set.pop()                   # 要素を消去して、消去した要素を出力
        for q in conj[p]:                       # 頂点 p から進める経路の候補から一つ選ぶ
            if q in visit:                      # 一度訪れていた場合は進まない
                continue
            if q == goal:                       # ゴールがあるならば、ここで判定
                return t + 1                    # 経路の長さは t + 1 で与えられるる
            visit.add(q)                        # 頂点 q に一度訪れた事をメモ (for の前に書くと、ここで選ばれた q が最短であるはずなのに、違う経路でvisit = Trueを踏んでしまう可能性がある)
            next_set.append((q, t + 1))         # p から q へと移動。時刻を 1 進める
    return -1

#############################################################
# キャッシュにメモしながら動的計画法を行う場合など、
# 帰りがけ時に子ノードたちの結果をまとめるような処理が重要な場合には、
# 再帰関数を用いた DFS が簡明 (メモ化再帰)。
#############################################################


def dfs2(conj, p=0, goal=None, t=0, past_p=None, visit=set(), second_visit=set()):
    # global res
    visit.add(p)
    for q in conj[p]:
        if q == past_p:
            # 逆流した際の処理
            continue
        if q in second_visit:
            # 帰り道に訪れた際の処理
            continue
        if q in visit:
            continue
        if q == goal:
            # ゴール時の処理
            # return t+1
            continue
        # p から q への引継ぎ処理
        # res[q] += res[p]
        dfs2(conj, q, goal, t+1, p, visit, second_visit)
    second_visit.add(p)
    # 帰り際の処置（壊した道を元に戻す等)
    # visit.discard(p)
    return # res


def cycle_detector(conj, p=0, t=0, dictated=False, past_p=None, path=[], visit=set(), second_visit=set(), cycle=[]):
    visit.add(p)
    path.append(p)
    for q in sorted(conj[p]):
        if not dictated:
            if q == past_p:
                continue
        if q in second_visit:
            continue
        if q in visit:
            if not cycle:
                while path:
                    r = path.pop()
                    cycle.append(r)
                    if r == q:
                        break
            continue
        cycle_detector(conj, q, t+1, dictated, p, path, visit, second_visit, cycle)
    second_visit.add(p)
    return cycle


def tree_counter(conj, detail=False):           # 木（閉路を含まない）の個数を返す。detail = True で、閉路のリストを返す
    connection_number = 0
    cycle_list = []
    visit = set()
    second_visit = set()
    for start in range(N):
        if start not in visit:
            connection_number += 1
            cycle = cycle_detector(conj, start, visit=visit, second_visit=second_visit, cycle=[])
            if cycle:
                cycle_list.append(cycle)
    if not detail:
        return connection_number - len(cycle_list)
    else:
        return cycle_list


def path_detector(conj, p=0, t=0, past_p=None, full_path=[], visit=set(), second_visit=set(), decrement=False):   # 距離と探索経路を返す。デクリメントされている場合は、decrement=True にする
    visit.add(p)
    full_path.append((p + decrement,t))
    for q in sorted(conj[p]):
        if q == past_p:
            continue
        if q in second_visit:
            continue
        if q in visit:
            continue
        path_detector(conj, q, t+1, p, full_path, visit, second_visit, decrement)
    second_visit.add(p)
    full_path.append((p + decrement,t))
    return full_path

##################################################################


N, K = map(int, input().split())

A = list(map(int, input().split()))


M = N
conj = [set() for _ in range(N)]
for i in range(M):
    u = i
    v = A[i] - 1
    conj[u].add(v)

p = 0
cnt = 0
if K <= N:
    while cnt + 1 <= K:
        p = A[p] - 1
        cnt += 1
    res = p + 1
else:
    cycle = list(
        reversed(cycle_detector(conj, p=0, t=0, dictated=True, past_p=None, path=[], visit=set(), second_visit=set(), cycle=[])))
    len_cycle = len(cycle)

    p = 0
    cnt = 0
    res = 0
    if not len_cycle:
        while cnt < K:
            p = A[p] - 1
            cnt += 1
        res = p + 1
    else:
        while p != cycle[0]:
            p = A[p] - 1
            cnt += 1
        k = (K - cnt) % len_cycle
        res = cycle[k] + 1
print(res)



