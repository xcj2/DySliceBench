
def read_input():
    n = int(input())

    stations = []
    for i in range(n - 1):
        c, s, f = map(int, input().split())
        stations.append((c, s, f))

    return n, stations


# 時刻currにてstationにいるとして、次の駅にたどり着く時刻を求める
def time_calc(curr, station):
    if curr <= station[1]:
        return station[0] + station[1]

    diff = curr - station[1]
    if diff % station[2] == 0:
        coef = diff // station[2]
    else:
        coef = diff // station[2] + 1
    return station[0] + station[1] + coef*station[2]


def total_time(stations):
    curr = 0
    for station in stations:
        curr = time_calc(curr, station)

    return curr


def submit():
    n, stations = read_input()

    for i in range(n - 1):
        print(total_time(stations[i:]))
    print(0)

if __name__ == '__main__':
    submit()