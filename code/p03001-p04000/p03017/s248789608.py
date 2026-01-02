import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def II(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def SI(): return input()
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')

def main():
    N, A, B, C, D = LI_()
    S = SI().strip()

    if C < D:  # AがBを追い越さないとき
        if B < C:  # ABCDの並びのとき
            # A-Dに2つ以上連続の#がなければOK
            previous = '.'
            for i in range(A, D+1):
                if S[i] == '#':
                    if previous == '#':
                        print('No')
                        return
                    else:
                        previous = '#'
                else:
                    previous = '.'
            print('Yes')
            return

        elif C < B:  # ACBDの並びのとき
            # A-C, B-D に2つ以上連続の#がなければOK
            previous = '.'
            for i in range(A, C+1):
                if S[i] == '#':
                    if previous == '#':
                        print('No')
                        return
                    else:
                        previous = '#'
                else:
                    previous = '.'

            previous = '.'
            for i in range(B, D+1):
                if S[i] == '#':
                    if previous == '#':
                        print('No')
                        return
                    else:
                        previous = '#'
                else:
                    previous = '.'

            print('Yes')
            return

    elif D < C:  # AがBを追い越すとき: ABDCの並びしかない。
        # A-C に2つ以上連続の#がない かつ B-D に避難場所（3つ以上連続する . ）がある。
        count_continuous_dots = 0
        can_evac = False
        previous = '.'
        for i in range(A, C+1):
            if S[i] == '#':
                if previous == '#':
                    print('No')
                    return
                else:
                    previous = '#'
                    count_continuous_dots = 0
            else:
                previous = '.'
            if B-1 <= i <= D+1:
                if S[i] == '.':
                    count_continuous_dots += 1
                    if count_continuous_dots >= 3:
                        can_evac = True
        if can_evac:
            print('Yes')
        else:
            print('No')
        return


main()