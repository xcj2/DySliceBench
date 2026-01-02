import random

#--------ピ　ザ　群　最　適　化------------------------------

#評価関数: 　双対問題
def criterion(x, y):
    z=xo*x+yo*y

    if x>a or y>b or x+y>2*c or x<0 or y<0:
        z=-z
    
    return z

#粒子の位置の更新を行う関数
def update_position(x, y, vx, vy):
 
    new_x = x + vx
    new_y = y + vy

    return new_x, new_y

#粒子の速度の更新を行う関数
def update_velocity(x, y, vx, vy, p, g, w=1, ro_max=0.5,v_max=10):
    #パラメーターroはランダムに与える
    ro1 =random.uniform(0, ro_max)
    ro2 =random.uniform(0, ro_max)
    #粒子速度の更新を行う
    new_vx = int((w * vx + ro1 * (p["x"] - x) + ro2 * (g["x"] - x)))
    new_vy = int((w * vy + ro1 * (p["y"] - y) + ro2 * (g["y"] - y)))
    if abs(new_vx)>v_max:
        new_vx=int(v_max*new_vx/abs(new_vx))
    if abs(new_vy)>v_max:
        new_vy=int(v_max*new_vy/abs(new_vy))

    #print(new_vx, new_vy)
    return new_vx, new_vy
    
def main():
    N = 2000  #粒子の数
    x_min, x_max = 0, a
    y_min, y_max = 0, b
    #粒子位置, 速度, パーソナルベスト, グローバルベストの初期化を行う
    ps = [{"x": random.randint(x_min, x_max), 
        "y": random.randint(y_min, y_max)} for i in range(N)]
    vs = [{"x": 0, "y": 0} for i in range(N)]

    personal_best_positions = list(ps)
    personal_best_scores = [criterion(p["x"], p["y"]) for p in ps]

    best_particle = personal_best_scores.index(max(personal_best_scores))
    global_best_position = personal_best_positions[best_particle]

    T = 100  #制限時間(ループの回数)
    for t in range(T):
        for n in range(N):
            x, y = ps[n]["x"], ps[n]["y"]
            vx, vy = vs[n]["x"], vs[n]["y"]
            p = personal_best_positions[n]
            #粒子の位置の更新を行う
            new_x, new_y = update_position(x, y, vx, vy)
            ps[n] = {"x": new_x, "y": new_y}
            #粒子の速度の更新を行う
            new_vx, new_vy = update_velocity(
                new_x, new_y, vx, vy, p, global_best_position)
            vs[n] = {"x": new_vx, "y": new_vy}
            #評価値を求め, パーソナルベストの更新を行う
            score = criterion(new_x, new_y)
            if score > personal_best_scores[n]:
                personal_best_scores[n] = score
                personal_best_positions[n] = {"x": new_x, "y": new_y}
        #グローバルベストの更新を行う
        best_particle = personal_best_scores.index(max(personal_best_scores))
        global_best_position = personal_best_positions[best_particle]
#        print(max(personal_best_scores), global_best_position["x"], global_best_position["y"])

    #最適解
    return max(personal_best_scores), global_best_position["x"], global_best_position["y"]


#--------------------------------------------------------------

a, b, c, xo, yo = [int(i) for i in input().split()]
#a, b, c, xo, yo = 1500, 2000, 500, 90000, 100000
best=-100000000
xx=0
yy=0
for i in range(3):
    kouho_best, kouho_x, kouho_y=main()
    if best<kouho_best:
        best=kouho_best
        xx=kouho_x
        yy=kouho_y

print(best)

