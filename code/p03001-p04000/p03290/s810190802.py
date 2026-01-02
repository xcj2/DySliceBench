import random
import bisect
import math

option = 0     # 0:PSO 1:CFA 2:CFArank
max_or_min = 0 # 0:minimize 1:maxmize

iter=2

N = 50 #粒子の数
T = 1000 #世代数(ループの回数)
maximum=1
minimum=0

dimension, limit = [int(i) for i in input().split()]

pi = [0 for i in range(dimension)]
ci = [0 for i in range(dimension)]
       
for i in range(dimension):
    pi[i], ci[i] = [int(i) for i in input().split()]

tot = [pi[i] * (i+1) * 100 + ci[i] for i in range(dimension)]
#print(pi)
#print(ci)
#print(tot)


#--------粒　子　群　最　適　化------------------------------

#評価関数
def criterion(x):
    
    z = sum([pi[i] * x[i] for i in range(dimension)])
    z2 = sum([tot[i] * x[i] for i in range(dimension)])
    k = -1
    for i in range(dimension):
      if x[dimension -1 -i] == 0:
        k = dimension -1 -i
        break
    if k != -1:
      for i in range(pi[k]):
        if limit > z2:
          z += 1
          z2 +=  (k+1) * 100
        else:
          break

    if limit > z2:
        z = 10000
    return z

#粒子の位置の更新を行う関数
def update_position(x, v, x_min, x_max):
#    new_x = [x_min[i] if x[i]+ v[i] < x_min[i] else x_max[i] if x[i]+ v[i] > x_max[i] else x[i]+ v[i] for i in range(dimension)]
    new_x = [1 if random.uniform(0, 1)< 1/(1+math.e**(-v[i])) else 0 for i in range(dimension)]
    return new_x

#粒子の速度の更新を行う関数
def update_velocity(x, v, p, g, w, ro_max=1.0, c1=2.00, c2=0.75):
    #パラメーターroはランダムに与える
    phi=c1+c2
    K=2/abs(2-phi-(phi*phi-4*phi)**0.5)
    
    #粒子速度の更新を行う
    if option!=0:
        new_v = [K * ( w * v[i] + c1 * random.uniform(0, ro_max) * (p[i] - x[i]) + c2 * random.uniform(0, ro_max) * (g[i] - x[i]) ) for i in range(dimension)]
    else:
        new_v = [w * v[i] + c1 * random.uniform(0, ro_max) * (p[i] - x[i]) + c2 * random.uniform(0, ro_max) * (g[i] - x[i]) for i in range(dimension)]

    return new_v

def main():
    w = 1.0
    w_best, w_worst = 1.25, 0.25
    x_min = [minimum for i in range(dimension)]
    x_max = [maximum for i in range(dimension)]
    
    #粒子位置, 速度, パーソナルベスト, グローバルベストの初期化を行う
    ps = [[random.randint(x_min[j], x_max[j]) for j in range(dimension)] for i in range(N)]
    vs = [[0.0 for j in range(dimension)] for i in range(N)]

    personal_best_positions = ps[:] 
    personal_best_scores = [criterion(p) for p in ps]

    if max_or_min == 1:
        best_particle = personal_best_scores.index(max(personal_best_scores))
    elif max_or_min == 0:
        best_particle = personal_best_scores.index(min(personal_best_scores))
    global_best_position = personal_best_positions[best_particle][:]

    for t in range(T):
        for n in range(N):
            x = ps[n][:]
            v = vs[n][:]
            p = personal_best_positions[n][:]

            if option>=2:
                best_list = sorted(personal_best_positions)
                mu = bisect.bisect_left( best_list, p ) + 1
                w = w_best - mu * (w_best - w_worst) / (N - 1)


            #粒子の位置の更新を行う
            new_x = update_position(x, v, x_min, x_max)
            ps[n] = new_x[:]

            #粒子の速度の更新を行う
            new_v = update_velocity(new_x, v, p, global_best_position, w)
            vs[n] = new_v[:]

            #評価値を求め, パーソナルベストの更新を行う
            score = criterion(new_x)

            if max_or_min == 1:
                if score > personal_best_scores[n]:
                    personal_best_scores[n] = score
                    personal_best_positions[n] = new_x[:]
            elif max_or_min == 0:
                if score < personal_best_scores[n]:
                    personal_best_scores[n] = score
                    personal_best_positions[n] = new_x[:]

        #グローバルベストの更新を行う
        if max_or_min == 1:
            best_particle = personal_best_scores.index(max(personal_best_scores))
            global_best_position = personal_best_positions[best_particle][:]

        elif max_or_min == 0:
            best_particle = personal_best_scores.index(min(personal_best_scores))
            global_best_position = personal_best_positions[best_particle][:]
                     
        f.write(str(max(personal_best_scores))+"\n")
    #最適解
    if max_or_min == 1:
        return max(personal_best_scores)
    elif max_or_min == 0:
        return min(personal_best_scores)

#--------------------------------------------------------------
with open('test_'+ str(option)+".txt", 'w') as f:
    
  if max_or_min == 1:
    best=-float("inf")
    for i in range(iter):
        best=max(best, main())

  elif max_or_min == 0:
    best=float("inf")
    for i in range(iter):
        best=min(best, main())

print(best)
