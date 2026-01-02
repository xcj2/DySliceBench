# Binary Indexed Treeを各アルファベットについてもつ (それぞれN+1の空間を保持し、1-indexで考える)
N = int(input())
S = list(input())
BITS = [[0]*(N+1) for _ in range(26)]
# 初期化を行おうと思ったが、これ自体に関数が必要である
# 値の加算


def ctoi(alphabet):
    return ord(alphabet)-97


# 1~idxまでの文字に各文字がどれだけ出現するか
def BIT_query(idx):
    res = [0]*26
    for i in range(26):
        p = idx
        tmp = 0
        while p > 0:
            tmp += BITS[i][p]
            p -= p & (-p)
        res[i] = tmp
    return res


def BIT_update(idx, alphabet, x):  # idx: int, alphabet: str, x: int
    while idx <= N:
        BITS[ctoi(alphabet)][idx] += x
        idx += idx&(-idx)


# 初期化を行う
for i in range(N):
    BIT_update(i+1, S[i], 1)

# クエリを受け取っていく
Q = int(input())
for _ in range(Q):
    type, a, b = map(str, input().split())
    if type == "1":  # 更新のクエリなら
        # このとき、aはindex, bは変更後の文字(str)である
        a = int(a)
        if S[a-1] == b:
            continue
        BIT_update(a, S[a-1], -1)  # 減らす処理
        BIT_update(a, b, 1)  # 増やす処理
        S[a-1] = b
    elif type == "2":  # 回答する必要があるクエリ
        # このとき、aは左端, bは右端
        a, b = int(a), int(b)
        cnt1 = BIT_query(a-1)
        cnt2 = BIT_query(b)
        ans = 0
        for i in range(26):
            if cnt2[i] > cnt1[i]:
                ans += 1
        print(ans)
