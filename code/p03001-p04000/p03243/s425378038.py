import sys

# 関数 solve は，もちろん，問題に応じて書き換える
def solve(n):
    a = []
    b = str(n)
    a.append(b)
    for i in a:
        c = i
    d = c[0]
    e = int(d)*100 + int(d)*10 + int(d)
    if e >= n:
        return e
    else:
        return int(e)+111

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