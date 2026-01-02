import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)

A,B,C,D,E,F = LI()

"""
100gあたりEgとける

ABCDは何回でも行える
A,Bは100A, 100B

Fg以内で砂糖を溶け残らせてはいけない
水全体と砂糖の量を求める

濃度は100b/(a+b)

砂糖を細かく追加して、溶け残らないようにする？
2, 5あれば、4,5にできるので、組み合わせを全部試す？
ビーカー量が200gで、溶ける量が15gなら、最大でも30gまでしか溶けない
10, 20なら、10, 10, 10,と10, 20の組み合わせが考えられる
Cの最大回数とDの最大回数を求める
それぞれの量の組み合わせをすべて試す
例えば10回、10回なら、0,0/1,0/2,0...とすべて試す
"""
max_sugar_amount = int(F//(100+E)*E)
max_C_times = int(max_sugar_amount // C)
max_D_times = int(max_sugar_amount // D)
#  print('max sugar', max_sugar_amount, 'max c', max_C_times, 'max d', max_D_times)
#  exit()
ans_sugar = 0
ans_water = 0
ans_density = 0
def check_density(sugar, water, new_sugar, new_water):
    if water + sugar == 0:
        return True 
    density = (100*sugar) / (water+sugar)
    new_density = (100*new_sugar) / (new_water + new_sugar)
    return density < new_density


for i in range(0, max_C_times+1):
    #  print('i', i)
    if max_D_times == 0:
        sugar_amount = i*C
        if sugar_amount > max_sugar_amount:
            break
        else:
            # 溶け切る場合
            #  print('溶け切る')
            water_limit = F - sugar_amount
            min_water_amount = sugar_amount / E * 100
            #  print(sugar_amount, min_water_amount)
            max_A_times = int(water_limit // (A*100))
            max_B_times = int(water_limit // (B*100))
            #  print('maxA', max_A_times)
            for k in range(1, max_A_times+1):
                if max_B_times == 0:
                    # 水Bはいれられないとき
                    water = k*100*A
                    if water_limit >= water >= min_water_amount:
                        # 水の量が砂糖を溶かすのに十分 # 水量がこえていない
                        if check_density(ans_sugar, ans_water, sugar_amount, water):
                            ans_sugar = sugar_amount
                            ans_water = water
                else:
                    for l in range(0, max_B_times+1):
                        water = k*100*A + l*100*B
                        if water_limit >= water >= min_water_amount:
                            # 水の量が砂糖を溶かすのに十分
                            if check_density(ans_sugar, ans_water, sugar_amount, water):
                                ans_sugar = sugar_amount
                                ans_water = water

    for j in range(0, max_D_times+1):
        #  print(j)
        sugar_amount = i*C + j*D
        if sugar_amount > max_sugar_amount:
            break
        else:
            water_limit = F - sugar_amount
            min_water_amount = sugar_amount / E * 100
            max_A_times = int(water_limit // (A*100))
            max_B_times = int(water_limit // (B*100))
            for k in range(1, max_A_times+1):
                if max_B_times == 0:
                    water = k*100*A
                    if water_limit >= water >= min_water_amount:
                        # 水の量が砂糖を溶かすのに十分 # 水量がこえていない
                        if check_density(ans_sugar, ans_water, sugar_amount, water):
                            ans_sugar = sugar_amount
                            ans_water = water
                else:
                    for l in range(max_B_times+1):
                        water = k*100*A + l*100*B
                        if water_limit >= water >= min_water_amount:
                            if check_density(ans_sugar, ans_water, sugar_amount, water):
                                ans_sugar = sugar_amount
                                ans_water = water
print(ans_water + ans_sugar, ans_sugar)
