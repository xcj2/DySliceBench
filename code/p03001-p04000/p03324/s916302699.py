import sys

# 関数 solve は，もちろん，問題に応じて書き換える
def solve(d,n):
    if  n != 100 :
        return (100**d)*n
    elif n == 100:
         return (100**d)*101 
    else:
        return n

# ここから下は，入力・出力形式が同じであれば，変えなくて良い．
def readQuestion():
    line = sys.stdin.readline().rstrip()
    [str_a, str_b] = line.split(' ')
    return (int(str_a), int(str_b))

def main():
    a, b = readQuestion()
    answer = solve(a, b)
    print(answer)
    
if __name__ == '__main__':
    main()