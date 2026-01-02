import sys

# 関数 solve は，もちろん，問題に応じて書き換える
def solve(N):
    hantei = 0
    for i in range(26):
        for j in range(20):
            if 4*i + 7*j == N :
                hantei = 4*i + 7*j
    if hantei == N :
        return ('Yes')
    else :
        return('No')
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