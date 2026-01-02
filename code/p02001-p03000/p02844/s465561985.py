#関数リスト
import sys
from copy import deepcopy
input = sys.stdin.readline


def RD(): return input().rstrip()
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))

def main():
    d = [[]]*10
    keta = I()
    num = input().rstrip()
    for i in range(keta):
        temp = int(num[i])
        if len(d[temp]) == 0:
            d[temp] = [int(keta-i)]
        else:
            d[temp].append(int(keta-i))
    result = 0
    for j in range(1000):
        a = j // 100
        b = (j % 100) // 10
        c = ((j % 100) % 10)
        try:
            a_num = d[a][0]
        except:
            continue
        try:
            if a == b:
                b_num = d[b][1]
            else:
                index = 0
                while True:
                    b_num = d[b][index]
                    if b_num < a_num:
                        break
                    else:
                        index += 1
        except:
            continue
        try:
            if a == c and a == b:
                c_num = d[c][2]
            elif a == c or b == c:
                c_num = min(d[c][1:])
            else:
                c_num = min(d[c])
        except:
            continue
        if a_num > b_num and b_num > c_num:
            result += 1

    print(result)

if __name__ == "__main__":
    main()