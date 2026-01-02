import sys

sys.setrecursionlimit(10 ** 7)
debug = True

debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()

INF = 10 ** 18
MOD = 10 ** 9 + 7

def main():
    N = II()
    S = SI()

    #mark = [-1 for i in range(N)]
    ans = -1

    from collections import defaultdict
    posd = defaultdict(list)

    for i, c in enumerate(S):
        posd[c].append(i)

    for i in range(N):
        si = S[i]

        # headの文字の位置のリスト
        pos_list = posd[si]

        for pos in pos_list:
            if pos >= i:
                # 自分より前のところだけを探す
                continue

            # この場合は直前により長いシーケンスを見ているので見なくていい
            if pos > 0 and S[pos - 1] == S[i - 1]:
                continue

            # どこまであうかをやっていく
            for j in range(N):
                # 前回見たシーケンスは見ない
                # 自分のところまで来てたらやめる
                if pos+j == i:
                    break
                # 突き抜けたらやめる
                if i+j == N:
                    break

                you = pos + j
                me = i + j

                # 違ったらやめる
                if S[you] != S[me]:
                    break

                # 同じなら、マークする
                ans = max(ans, j)
                #mark[you] = max(mark[you], j)

    #dprint(mark)
    #print(max(mark)+1)
    print(ans + 1)

main()