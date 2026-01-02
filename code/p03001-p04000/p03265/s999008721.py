import sys

# 関数 solve は，もちろん，問題に応じて書き換える
def solve(a,b,c,d):
    x = c-a
    y = d-b
    x3 = 0
    x4 = 0
    y3 = 0
    y4 = 0
    #print(x,y)
    x3 = c-y
    y3 = d+x
    x4 = x3-x
    y4 = y3-y
    return str(x3) + ' '  + str(y3) + ' ' + str(x4) + ' ' + str(y4) + ' '

# ここから下は，入力・出力形式が同じであれば，変えなくて良い．
def readQuestion():
    line = sys.stdin.readline().rstrip()
    [str_a, str_b, str_c, str_d] = line.split(' ')
    return (int(str_a), int(str_b), int(str_c), int(str_d))

def main():
    a, b, c, d = readQuestion()
    answer = solve(a, b, c, d)
    print(answer)
    
if __name__ == '__main__':
    main()