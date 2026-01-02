import sys

# 関数 solve は，もちろん，問題に応じて書き換える
def solve( lst_a, lst_b,n):
    if n.count("-")!=1:
        answer= "No"
    else:
        N,NN=n.split("-")
        if lst_a == len(N) and lst_b == len(NN):
            answer = "Yes"
        else:
            answer = "No"
    return answer

# ここから下は，入力・出力形式が同じであれば，変えなくて良い．
def readQuestion():
    line1 = sys.stdin.readline().rstrip()
    [str_n, str_i] = line1.split(' ')
    line2 = sys.stdin.readline().rstrip()
    return (int(str_n), int(str_i), line2)

def main():
    n, i, s = readQuestion()
    answer = solve(n, i, s)
    print(answer)
    
if __name__ == '__main__':
    main()