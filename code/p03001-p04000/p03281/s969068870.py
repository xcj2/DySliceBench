import sys

# 関数 solve は，もちろん，問題に応じて書き換える
def solve(n):
    listc = []
    for i in range(1,201):
        lista = []
        for j in range(1,201):
            if i%j == 0:
                lista.append(j)
        if len(lista) >= 8 and lista[-1] %2 != 0:
            listc.append(lista[-1])
    #print(listc)#デバッグ用
    for i in range(len(listc)):
        if n < listc[0]:
            return 0
        elif n >= listc[-(i+1)]:
            return len(listc)-i

# ここから下は，入力・出力形式が同じであれば，変えなくて良い．
def readQuestion():
    line = sys.stdin.readline().rstrip()
    return int(line)

def main():
    n = readQuestion()
    answer = solve(n)
    print(answer)
if __name__ == '__main__':
    main()