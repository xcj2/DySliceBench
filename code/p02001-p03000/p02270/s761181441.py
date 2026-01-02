

def check(P, k, w): # 最大積載量Pのトラックがk台ある時、積める荷物の個数
    i = 0 # 返値＝積める荷物の個数のカウンター
    n = len(w) # 積まなければならない荷物の総数
    for _ in range(k):# トラックの台数分のループ
        s = 0 # そのトラックの積載量
        while s + w[i] <= P: # トラックに新たな荷物を積んでもP以下ならば
            s += w[i] # その荷物を積む
            i += 1 # 次の荷物に移る
            if i==n: # もし荷物を全部詰めたら
                return n # 荷物の総数を返す
    return i

def solve(n, k, w): # 二分探索
    left = 0
    right = n*max(w)
    while right - left > 1:
        mid = int((left + right)/2)
        v = check(mid, k, w)
        if v>=n:
            right = mid
        else:
            left = mid
    return right

def main():
    n, k = map(int, input().split())
    w = [int(input()) for i in range(n)]
    answer = solve(n, k, w)
    print(answer)

main()
