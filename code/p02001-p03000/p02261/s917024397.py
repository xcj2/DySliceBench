n = int(input())
R = [x for x in input().split()]#リスト内包表記
R2=R.copy()

def selected_sort(a,n):
    for i in range(0,n-1):#一個前までやれば全てソートが完了する
        minj=i#未ソート部の先頭をminとみなす
        for j in range(i,n):
            if a[j][1]<a[minj][1]:#
                minj=j#最小インデックスの更新
                judge=True#インデックスが更新されたかどうかの判定
        a[i],a[minj]=a[minj],a[i]#最小値と未ソートの先頭をswap
    print(*a)

def bubble_sort(r,n):
    flag=True
    i=0
    count=0
    while flag:
        flag=False
        for i in range(n-1,i,-1):#iは1でとまらないとi-1が-1となってしまう
            if r[i][1]<r[i-1][1]:
                r[i],r[i-1]=r[i-1],r[i]#swap
                count+=1
                flag=True#入れ替える条件があって初めてtrueになる
    print(*r)

def isStable(a,b):
    if R==R2:
        print("Stable")
    else:
        print("Not stable")


bubble_sort(R,n)
print("Stable")

selected_sort(R2,n)
isStable(R,R2)

