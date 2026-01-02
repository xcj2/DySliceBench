import numpy as np

#l,rまでの配列に+1する関数
def give_water(flower, lr):
    flower_with_water = [x+1 if i>=lr[0] and i<=lr[1] else x for i,x in enumerate(flower)]
    return flower_with_water

def TF_list(flower, h):
    h = np.array(h)
    TF_list_0 = []
    for i in range(len(flower)):
        TF_list_0.append(flower[i] < h[i])
    return TF_list_0

#Trueが連続しているindexの範囲を[(0, 1), (2,4)]みたいな形で出力
def list_tuple_True(flower, h, N):
    TF_list = (flower < h)
    TF_list = np.insert(TF_list, N, False)
    True_range = []
    #FLAGは一つ前のTFを表す。初期値はFalse
    FLAG = False
    for i, TF in enumerate(TF_list):
        if TF:
            if FLAG:
                #Trueが連続している場合
                pass
            else:
                #FalseからTrueに切り替わった場合
                start = i
        else:
            if FLAG:
                #TrueからFalseも切り替わった場合
                end = i-1
                True_range.append((start, end))
            else:
                #Falseが連続している場合
                pass
        FLAG = TF
    return True_range
            
N = int(input())
h = list(map(int, input().split()))

h = np.array(h)
flower = np.zeros(N)

count = 0
while not((h == flower).all()):
    water_range = list_tuple_True(flower, h, N)
    count += len(water_range)
    for lr in water_range:
        flower = give_water(flower, lr)
        
print(count)
        
