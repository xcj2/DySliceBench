def insertionSort(A,n,g):#cを引数に入れる方針では更新が怒らないらしい
    global c #ここにglobal cを置くことでmainからcの値を変更可能になる.c=0と書くと(ローカル宣言したのでこの瞬間からcがlocalになり、mainのcと別物になる)
    #print(tp[2])の結果はmainのc=0のグローバル宣言の影響を受け0のままになる
    for i in range(g,n):
        v=A[i]
        j = i - g
        while j >= 0 and A[j] >v:
            A[j+g] = A[j]
            j = j- g
            c+=1
            #print(c)
        A[j+g] = v
def shellSort(A,n): #ローカルスコープ
    i = 0
    G=[1]
    while 3*G[i]+1 < n :
        G.append(3*G[i]+1)
        #print("\n")
        i+=1
    G.reverse()
    m=len(G)
    for i in range(m):#シェルソーとは3G[i]+1の感覚がだんだん狭まっていくように
       insertionSort(A,n,G[i])
    return m,G,c,A#ここにc書いてもエラー出されないのはglobalのおかげなんだろうか←main関数内のc=0の定義のおかげ
#この関数内でcに代入がされた時点でcはローカル変数になっていたが、ここでは何も代入してないのでmainのglobal宣言が生きる
"""
def test():
    return 'abc', 100
"""
#Pythonにおいて、構文上必要な場合を除き、カンマで区切られた値は
# 丸括弧を省略したタプルとみなされる。このため、上の例の関数はそれぞれの値を要素とするタプルを返すことになる。

if __name__=="__main__":#グローバルスコープ
    c = 0#ここで各関数実行前にcをかけばglobal変数になる
    n = int(input())
    l = [int(input().rstrip()) for _ in range(n)]
    tp = shellSort(l,n)
    print(tp[0])
    #print(tp[1])
    a = [str(tp[1][i]) for i in range(len(tp[1]))]
    #print(a)
    print(' '.join(a))
    print(tp[2])
    for i in range(len(tp[3])):
        print(tp[3][i])
