import io
import sys
def solve(lista):    
    listb = []
    hantei = "true"
    for i in lista:
        if i not in listb:
            listb.append(i)
        else:
            hantei = "false"
    for i in range(len(listb)-1):
        if listb[i][-1] != listb[i+1][0]:
            hantei = "false"
    if hantei == "true":
        return("Yes")
    else:
        return("No")
# ここから下は，入力・出力形式が同じであれば，変えなくて良い．
def readQuestion():
    line1 = sys.stdin.readline().rstrip()
    lista = []
    for i in range(int(line1)):
        line2 = sys.stdin.readline().rstrip()
        lista.append(line2)
    return (lista)

def main():
    a = readQuestion()
    answer = solve(a)
    print(answer)
    
if __name__ == '__main__':
    main()