import sys

# 関数 solve は，もちろん，問題に応じて書き換える
def solve(n, k, as1):
    if (n-1)%(k-1)==0:
        return (n-1)//(k-1)
    else:
        return (n-1)//(k-1)+1

# ここから下は，入力・出力形式が同じであれば，変えなくて良い．
def readQuestion():
    line = sys.stdin.readline().rstrip()
    [str_n, str_k] = line.split(' ')
    line = sys.stdin.readline().rstrip()
    as1 = line.split(' ')
    return (int(str_n), int(str_k), [int(a) for a in as1])

def main():
    n, k, as1 = readQuestion()
    answer = solve(n, k, as1)
    print(answer)
    
if __name__ == '__main__':
    main()