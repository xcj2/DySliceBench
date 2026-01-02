import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    from itertools import accumulate
    #素数判定用の関数を定義
    #素数だったら１、素数じゃなかったら０と返す
    def main(n):
        if n==1:
            return 0
        else:
            for j in range(2,int(n**0.5)+1):
                if n%j==0:
                    return 0
            return 1

    q = int(input())
    # 要素がｑ個あって要素が全部０のリストをl格納用とr格納用で２つ作る
    l=[0]*q
    r=[0]*q
    # 入力してlとrを塗り替えていく
    for i in range(q):
        l[i],r[i]=list(map(int, input().split()))

    # 素数判定する範囲を定めるためにminとmaxとる
    lmin=min(l)
    rmax=max(r)

    # min~maxの値について素数判定を行う
    # 素数だったら０、素数じゃなかったら１が入ってるリストを作る
    sosucheck=[]
    for i in range(lmin,rmax+1):
        if i%2==0:
            sosucheck.append(0)
        else:
            if main(i)==1 and main((i+1)/2)==1:
                sosucheck.append(1)
            else:
                sosucheck.append(0)

    # 累積和のリスト作る（最初を０にしたいから最初に０を足す）
    rui=[0]+sosucheck
    rui=list(accumulate(rui))

    #出力
    for i in range(q):
        sr=r[i]-lmin+1
        sl=l[i]-lmin
        print(rui[sr]-rui[sl])
resolve()