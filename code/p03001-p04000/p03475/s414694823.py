def MI(): return map(int, input().split())
def II(): return int(input())
def IS(): return input()
def LI(): return list(map(int, input().split()))

n = II()
train = [list(MI()) for _ in range(n-1)]

for i in range(n-1):
    # 開通式が開始するまでの時間+次の駅に到着するまでの時間
    time = train[i][0] + train[i][1]
    for j in range(i+1, n-1):
        # 駅に着いた時まだ開通式後の最初の電車が駅を発車していない場合
        if time < train[j][1]:
            # 駅を出発する時刻は開通式の時刻になる
            time = train[j][1]
        elif time % train[j][2] == 0:  # そのまま出発可能
            pass
        else: # time % train[j][2] != 0 待ち時間を加算する必要がある
            time += (train[j][2] - (time % train[j][2]))

        time += train[j][0]  # 次の駅へ行くための時間

    print(time)
print(0)

