N,X = map(int,input().split())

def burger(n):#n次元バーガー出力(使わない)
    if n ==0:
        return "P"
    else:
        return "B" + burger(n-1) + "P" + burger(n-1) + "B"

def burger_size(n):#n次元バーガーのサイズ
    return 4*pow(2,n) - 3

def countP(n,x):#n次元バーガーのx層までのPの数を数えるよ
    if x <= 0:#一つも食わないとき
        return 0
    if burger_size(n)<=x:#全部食ったとき
        return 2*pow(2,n)-1
    else:
        return (1 if 2+burger_size(n-1)<=x else 0)+countP(n-1,x-1)+countP(n-1,x-2-burger_size(n-1))

print(countP(N,X))