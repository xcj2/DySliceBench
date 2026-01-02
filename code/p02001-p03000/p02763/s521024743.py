def ctoi(c):  # a~zを0~25に変換する(各アルファベットを数字に変換する)
    return ord(c) - 97


N = int(input())
S = list(input())
bits = [[0]*(N+1) for _ in range(26)]  # Binary Indexed Treeを26種類の各アルファベットについてもつ(0初期化, 1-index)


def BIT_query(idx):  # 各文字について1からidx番目までの文字数を数える
    res = [0]*26
    for i in range(26):
        tmp = 0
        p = idx
        while p > 0:  # 1からidx番目までの要素の和を取る
            tmp += bits[i][p]
            p -= p&(-p)  # 区間の長さを引くことで次のindexを得ることができる
        res[i] = tmp
    return res


def BIT_update(idx, alphabet, x):  # alphabet番目のアルファベットについてidx番目の要素の値にxを加える
    while idx <= N:  # idx番目の要素を含む全ての要素についてxを加える
        bits[alphabet][idx] += x
        idx += idx&(-idx)


for i in range(N):  # 各BITを与えられた文字列で初期化する
    BIT_update(i+1, ctoi(S[i]), 1)  # Sのi番目(0-index)の文字に対応するBITのi+1番目の要素を1として更新する

Q = int(input())
for _ in range(Q):
    flag, a, b = map(str, input().split())
    flag = int(flag)
    a = int(a)
    if flag == 1:
        if S[a-1] == b:  # 同じ文字の場合, 変更しない
            continue
        else:
            BIT_update(a, ctoi(S[a-1]), -1)  # a番目の要素を別のものに変えるので、-1
            BIT_update(a, ctoi(b), 1)  # a番目の要素を文字bに変えるので+1
            S[a-1] = b  # 文字列のa番目の文字を変更する
    elif flag == 2:  # aとbは区間の左端と右端
        b = int(b)
        cnt1 = BIT_query(b)  # 1からbまでの各文字の文字数
        cnt2 = BIT_query(a-1)  # 1からa-aまでの各文字の文字数
        ans = 0
        for i in range(26):
            if cnt1[i]-cnt2[i] > 0:  # lからrまでのその文字の文字数が1以上であれば、その文字はlからrまでの部分文字列に現れるので種類数を1増やす
                ans += 1
        print(ans)
