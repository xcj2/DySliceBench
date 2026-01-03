

def read_input():
    n = int(input())
    return n

def div_2(x, memo):
    # memoに答えがあれば返す
    if x in memo.keys():
        return memo[x], memo

    if x % 2 == 0:
        c, memo = div_2(x/2, memo)
        count = 1 + c
        memo[x] = count
        return count, memo

    return 0, memo

def submit():
    n = read_input()

    div_memo = {}
    for i in range(1, n + 1):
        _, div_memo = div_2(i, div_memo)

    counts = list(div_memo.items())
    counts.sort(key=lambda x:x[1], reverse=True)

    if not counts:
        print(1)
    else:
        print(counts[0][0])

if __name__ == '__main__':
    submit()