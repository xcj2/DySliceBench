import random
import bisect
import math

option = 0  # 0:PSO 1:CFA 2:CFArank
max_or_min = 0  # 0:minimize 1:maxmize
filewrite = 0  # 1:writefile 2:benchmark
dimension = 1
iter = 1

N = 100  # 粒子の数
T = 5000  # 世代数(ループの回数)
maximum = 10 ** 12
minimum = 0

n = int(input())
x_left = []
x_right = []
y_up = []
y_down = []
x_const = []
y_const = []
for i in range(n):
    x, y, d = input().split()
    x = int(x)
    y = int(y)
    if d == "U":
        x_const.append(x)
        y_up.append(y)
    elif d == "D":
        x_const.append(x)
        y_down.append(y)
    elif d == "L":
        y_const.append(y)
        x_left.append(x)
    elif d == "R":
        y_const.append(y)
        x_right.append(x)

x_const.sort()
y_const.sort()
x_left.sort()
x_right.sort()
y_up.sort()
y_down.sort()

try:
    x_const_max = x_const[-1]
    x_const_min = x_const[0]
except:
    x_const_max = -float("inf")
    x_const_min = float("inf")

try:
    y_const_max = y_const[-1]
    y_const_min = y_const[0]
except:
    y_const_max = -float("inf")
    y_const_min = float("inf")

try:
    x_left_max = x_left[-1]
    x_left_min = x_left[0]
except:
    x_left_max = -float("inf")
    x_left_min = float("inf")

try:
    x_right_max = x_right[-1]
    x_right_min = x_right[0]
except:
    x_right_max = -float("inf")
    x_right_min = float("inf")

try:
    y_up_max = y_up[-1]
    y_up_min = y_up[0]
except:
    y_up_max = -float("inf")
    y_up_min = float("inf")

try:
    y_down_max = y_down[-1]
    y_down_min = y_down[0]

except:
    y_down_max = -float("inf")
    y_down_min = float("inf")


# --------粒　子　群　最　適　化------------------------------

# 評価関数
def criterion(x, x_min, x_max):
    z = 0
    i = x[0]
    max_x = max(x_const_max, x_left_max - i, x_right_max + i)
    min_x = min(x_const_min, x_left_min - i, x_right_min + i)
    max_y = max(y_const_max, y_down_max - i, y_up_max + i)
    min_y = min(y_const_min, y_down_min - i, y_up_min + i)
    z = (max_x - min_x) * (max_y - min_y)
    if x < x_min:
        z = float("inf")
    return z


# 粒子の位置の更新を行う関数
def update_position(x, v):
    new_x = [x[i] + v[i] for i in range(dimension)]
    return new_x


# 粒子の速度の更新を行う関数
def update_velocity(x, v, p, g, w, ro_max=1.0, c1=1.6, c2=1.6):
    # パラメーターroはランダムに与える
    phi = c1 + c2
    K = 2 / abs(2 - phi - (phi * phi - 4 * phi) ** 0.5)

    # 粒子速度の更新を行う
    if option != 0:
        new_v = [K * (w * v[i] + c1 * random.uniform(0, ro_max) * (p[i] - x[i]) + c2 * random.uniform(0, ro_max) * (
                    g[i] - x[i])) for i in range(dimension)]
    else:
        new_v = [
            w * v[i] + c1 * random.uniform(0, ro_max) * (p[i] - x[i]) + c2 * random.uniform(0, ro_max) * (g[i] - x[i])
            for i in range(dimension)]

    return new_v


def main():
    w = 0.5
    w_best, w_worst = 1.25, 0.25
    x_min = [minimum for i in range(dimension)]
    x_max = [maximum for i in range(dimension)]

    # 粒子位置, 速度, パーソナルベスト, グローバルベストの初期化を行う
    ps = [[random.uniform(x_min[j], x_max[j]) for j in range(dimension)] for i in range(N)]
    vs = [[0.0 for j in range(dimension)] for i in range(N)]

    personal_best_positions = list(ps)
    personal_best_scores = [criterion(p, x_min, x_max) for p in ps]
    best_particle = personal_best_scores.index(max(personal_best_scores))
    global_best_position = personal_best_positions[best_particle]

    for t in range(T):
        for n in range(N):
            x = ps[n]
            v = vs[n]
            p = personal_best_positions[n]

            if option >= 2:
                best_list = sorted(personal_best_positions)
                mu = bisect.bisect_left(best_list, p) + 1
                w = w_best - mu * (w_best - w_worst) / (N - 1)

            # 粒子の位置の更新を行う
            new_x = update_position(x, v)
            ps[n] = new_x

            # 粒子の速度の更新を行う
            new_v = update_velocity(new_x, v, p, global_best_position, w)
            vs[n] = new_v

            # 評価値を求め, パーソナルベストの更新を行う
            score = criterion(new_x, x_min, x_max)

            if max_or_min == 1:
                if score > personal_best_scores[n]:
                    personal_best_scores[n] = score
                    personal_best_positions[n] = new_x
            elif max_or_min == 0:
                if score < personal_best_scores[n]:
                    personal_best_scores[n] = score
                    personal_best_positions[n] = new_x

        # グローバルベストの更新を行う
        if max_or_min == 1:
            if filewrite >= 1: f.write(str(max(personal_best_scores)) + "\n")
            best_particle = personal_best_scores.index(max(personal_best_scores))
            global_best_position = personal_best_positions[best_particle]

        elif max_or_min == 0:
            if filewrite >= 1: f.write(str(min(personal_best_scores)) + "\n")
            best_particle = personal_best_scores.index(min(personal_best_scores))
            global_best_position = personal_best_positions[best_particle]

    #            if min(personal_best_scores)<=10**5:
    #                return min(personal_best_scores)

    # 最適解
    if max_or_min == 1:
        return max(personal_best_scores)
    elif max_or_min == 0:
        #print(global_best_position)
        return min(personal_best_scores)


# --------------------------------------------------------------

if max_or_min == 1:
    best = -float("inf")
    for i in range(iter):
        if filewrite >= 2: option = i
        if filewrite >= 1:
            with open('result_' + str(option) + ".txt", 'w') as f:
                best = max(best, main())
        else:
            best = max(best, main())

elif max_or_min == 0:
    best = float("inf")
    for i in range(iter):
        if filewrite >= 2: option = i
        if filewrite >= 1:
            with open('result_' + str(option) + ".txt", 'w') as f:
                best = min(best, main())
        else:
            best = min(best, main())

print(best)

