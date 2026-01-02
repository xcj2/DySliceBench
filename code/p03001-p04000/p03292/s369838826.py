import sys

# 関数 solve は，もちろん，問題に応じて書き換える
def solve(a,b,c):
    f = [a,b,c]
    f.sort()
    #print(f)
    x = 0
    y = 0

    if a == b and b == c :
        return 0
    else:
        x = f[1] - f[0]
        y = f[2] - f[1]
        return x+y
# ここから下は，入力・出力形式が同じであれば，変えなくて良い．
def readQuestion():
    line = sys.stdin.readline().rstrip()
    [str_a, str_b, str_c] = line.split(' ')
    return (int(str_a), int(str_b), int(str_c))

def main():
    a, b, c = readQuestion()
    answer = solve(a, b, c)
    print(answer)
    
if __name__ == '__main__':
    main()