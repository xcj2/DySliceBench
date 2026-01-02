import sys
from collections import deque
def input(): return sys.stdin.readline().strip()

# Cubeクラス
class Cube:
    # CP, CO, EO配列を作る
    def __init__(self):
        self.Cp = [0, 1, 2, 3]
        self.Eo = [0, 0, 0, 0]
    
    # 回転処理 CP (コーナーの位置)
    def move_cp(self, num):
        res = [i for i in self.Cp]
        res[num], res[(num + 1) % 4] = res[(num + 1) % 4], res[num]
        return res

    # 回転処理 EO (エッジの向き)
    def move_eo(self, num):
        res = [i for i in self.Eo]
        res[num] += 1
        res[num] %= 2
        return res

    # 回転処理 全体
    def move(self, num):
        res = Cube()
        res.Eo = self.move_eo(num)
        res.Cp = self.move_cp(num)
        return res
    
    # CP, CO, EOの配列インデックスを返す
    def idxes(self):
        cp_idx = 0
        for i in range(4):
            cnt = 0
            for j in self.Cp[:i]:
                if j < self.Cp[i]:
                    cnt += 1
            cp_idx += fac[3 - i] * (self.Cp[i] - cnt)
        
        eo_idx = 0
        for i in range(4):
            eo_idx *= 2
            eo_idx += self.Eo[i]

        return cp_idx, eo_idx

# 階乗をO(1)で計算できるよう前計算
fac = [1 for _ in range(5)]
for i in range(1, 5):
    fac[i] = fac[i - 1] * i


solved = Cube() # 揃っている状態のパズルを定義しておく

# 枝刈りに使うcp, eo配列
cp = [100 for _ in range(fac[4])]
eo = [100 for _ in range(2 ** 4)]

# 幅優先探索を行う。キューを使う。
# 要素はパズルの状態とその状態になるまでにかかった手数、最後に回した2手を表す。
que = deque([[solved, 0, -10, -20]])
while que:
    status, num, l_mov, ll_mov = que.popleft()

    # 回転処理を行うかのフラグ
    move_flag = 2

    # cp, eo配列を更新する。どれか一つでも更新されたら次に動かす操作をする。
    idxes = status.idxes()
    for i, arr in zip(idxes, [cp, eo]):
        if arr[i] < 100:
            move_flag -= 1
        else:
            arr[i] = num
    
    # cp, eoの一つも更新されなかったらこのパズルを動かす必要はない。
    if not move_flag:
        continue

    # 直前の2手が上下または右左であったとき(l_movとll_movの差が2であったとき)にTrueになるフラグ
    mov_flag = True if abs(l_mov - ll_mov) == 2 else False

    # 次に回す手をfor文で回す
    for mov in range(4):
        # 計算量の削減!!!!!
        if mov == l_mov or (mov_flag and mov == ll_mov):
            continue

        # パズルを動かす
        n_status = status.move(mov)        

        que.append([n_status, num + 1, mov, l_mov])


# 深さ優先探索
def dfs(status, depth, num, l_mov, ll_mov):

    # 最大深さに達していたらFalseを返す
    if num == depth:
        return False
    
    # depth以内にCP, EOのどちらか一つでも揃わないとわかったら枝刈りをする
    continue_flag = False
    idxes = status.idxes()
    for i, arr in zip(idxes, [cp, eo]):
        if arr[i] + num > depth:
            continue_flag = True
            break
    if continue_flag:
        return False

    # 揃ったかどうかのフラグ
    flag = False

    # 直前の2手が上下または右左であったとき(l_movとll_movの差が2であったとき)にTrueになるフラグ
    mov_flag = True if abs(l_mov - ll_mov) == 2 else False

    # 次に回す手をfor文で回す
    for mov in range(4):
        # 計算量の削減!!!!!
        if mov == l_mov or (mov_flag and mov == ll_mov):
            continue

        # パズルを動かす
        n_status = status.move(mov)

        # 揃ったか?
        if num + 1 == depth:
            if n_status.Cp == solved.Cp and n_status.Eo == solved.Eo:
                flag = True
                break
        else:
            flag = flag or dfs(n_status, depth, num + 1, mov, l_mov)
    
    return flag


n = int(input())

for _ in range(n):
    # 入力
    p = [int(i) for i in input().split()]

    # 入力されたパズルの色の状態をpuzzleに格納 ここはどうしても手打ちが必要
    puzzle = Cube()
    for i, j in enumerate([[15, 20], [18, 14], [12, 11], [9, 17]]): # CPの処理
        tmp = [[6, 5, 4, 2], [5, 4, 2, 6]]
        for k in range(4):
            flag = 0
            for l in range(2):
                for m in range(2):
                    if p[j[l]] == tmp[m][k]:
                        flag += 1
            if flag == 2:
                puzzle.Cp[i] = k
                break
    for i, j in enumerate([1, 5, 7, 3]): # EOの処理
        if p[j] == 3:
            puzzle.Eo[i] = 1
    
    # 0手で揃う場合のみ例外
    if puzzle.Eo == solved.Eo and puzzle.Cp == solved.Cp:
        print(0)
        continue

    # IDA* 最大深さは7。
    for depth in range(1, 8):
        if dfs(puzzle, depth, 0, -10, -20):
            print(depth)
            break
    else:
        print(8)

