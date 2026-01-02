import sys, collections, heapq
def input(): return sys.stdin.readline().strip()

d = {'A': 0, 'B': 0, 'C': 0}
ans = []
S = []

def distribute(s):
    if d[s[0]] < d[s[1]]:
        d[s[0]] += 1
        d[s[1]] -= 1
        ans.append(s[0])
    else:
        d[s[0]] -= 1
        d[s[1]] += 1
        ans.append(s[1])

def main():
    N, A, B, C = map(int, input().split())
    summation = A + B + C
    d['A'], d['B'], d['C'] = A, B, C

    """
    最低3個は実験しないといけんですわ。。。
    まずA+B+Cが不変量なことに気づく（これはよし）
    そしたらA+B+C=0,1,2の場合に実験してみる。
    和が0の場合は明らかにアウト。和が1の場合は実際にN回通してみれば良い。

    和が2の場合は（これを試さなかったのが敗因！！！！！！）
        (A, B, C) = (2, 0, 0) or (1, 1, 0)
    の２パターン（ただし順不問）があるが、前者はBCの指示がきたらアウト。
    それ以外は後者に変化する。
    一方後者の場合はBC, CAの指示では変化なし、ABの指示で前者になる。
    このとき次の一手でドボンしないようにABのどちらを2にするか考えれば、
    再び後者に戻ってくる。

    つまり後者の安定型に初手でなれれば勝ち。このロジックはN>=3でも通じる。
    """

    if summation == 0:
        print("No")
        return

    if summation == 1:
        for _ in range(N):
            s = input()
            distribute(s)
            if d['A'] < 0 or d['B'] < 0 or d['C'] < 0:
                print("No")
                return
        print("Yes")
        for s in ans: print(s)

    if summation >= 2:
        for _ in range(N): S.append(input())
        S.append("AB") # sentry
        if d[S[0][0]] == 0 and d[S[0][1]] == 0:
            print("No")
            return
        print("Yes")

        for i in range(N):
            if d[S[i][0]] > 1 or d[S[i][1]] > 1:
                distribute(S[i])
            elif d[S[i][0]] == 0 or d[S[i][1]] == 0:
                distribute(S[i])
            else: # both are 1
                char_list = [S[i][0], S[i][1], S[i + 1][0], S[i + 1][1]]
                if S[i] == S[i + 1]:
                    distribute(S[i])
                elif char_list.count('A') == 2:
                    d['A'] += 1
                    d[S[i][1]] -= 1
                    ans.append('A')
                elif char_list.count('C') == 2:
                    d['C'] += 1
                    d[S[i][0]] -= 1
                    ans.append('C')
                else:
                    d['B'] += 1
                    if S[i] == "AB":
                        d['A'] -= 1
                    else:
                        d['C'] -= 1
                    ans.append('B')

        for s in ans: print(s)






if __name__ == "__main__":
    main()
