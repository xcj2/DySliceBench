#提出が大幅に遅れてしまい、本当に申し訳ありません。
#着席位置は左*奥
#問題は「Curling 2.0」(http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1144&lang=jp)

#要は全探索しろという話なのですが、DFSで5日ほど頑張って結局バグが取れなかったのと、
#枝刈りができなかったのとが原因でQueueを使ったBFSに切り替えました
#無限にバグを出したので実装が相当気持ち悪い事になっています

from queue import Queue as q

#以下、しばらく上下左右それぞれの移動の関数です
#移動はとにかく一方向に見ていって、ゴールなら終わり、壁なら次の状態を返す、端までいったらNoneを返すものです
#ただし、試行回数が10を超えてしまったら強制的にNoneを返します
def l_move(data):
    global flag
    field,n,i,j = data[0],data[1],data[2],data[3]
    if j == 0 or field[i][j-1] == 1 or n == 0:
        return(None)
    while(j):
        if field[i][j-1] == 0:
            j -= 1
        elif field[i][j-1] == 3:
            flag = True
            print(11-n)
            return(None)
        else:
            nfield = field[:i] + [field[i][:j-1] + [0] + field[i][j:]] + field[i+1:]
            n -= 1
            return([nfield,n,i,j])
    return(None)

def u_move(data):
    global flag
    field,n,i,j = data[0],data[1],data[2],data[3]
    if i == 0 or field[i-1][j] == 1 or n == 0:
        return(None)
    while(i):
        if field[i-1][j] == 0:
            i -= 1
        elif field[i-1][j] == 3:
            flag = True
            print(11-n)
            return(None)
        else:
            nfield = field[:i-1] + [field[i-1][:j] + [0] + field[i-1][j+1:]] + field[i:]
            n -= 1
            return([nfield,n,i,j])
    return(None)

def r_move(data):
    global flag
    field,n,i,j = data[0],data[1],data[2],data[3]

    if j == y-1 or field[i][j+1] == 1 or n == 0:
        return(None)
    while(j < y-1):
        if field[i][j+1] == 0:
            j += 1
        elif field[i][j+1] == 3:
            flag = True
            print(11-n)
            return(None)
        else:
            nfield = field[:i] + [field[i][:j+1] + [0] + field[i][j+2:]] + field[i+1:]
            n -= 1
            return([nfield,n,i,j])
    return(None)

def d_move(data):
    global flag
    field,n,i,j = data[0],data[1],data[2],data[3]
    if i == x-1 or field[i+1][j] == 1 or n == 0:
        return(None)
    while(i < x-1):
        if field[i+1][j] == 0:
            i += 1
        elif field[i+1][j] == 3:
            flag = True
            print(11-n)
            return(None)
        else:
            nfield = field[:i+1] + [field[i+1][:j] + [0] + field[i+1][j+1:]] + field[i+2:]
            n -= 1
            return([nfield,n,i,j])
    return(None)

while(True):
    flag = False #これがTrueになったら出力して次のデータセット
    y,x = map(int,input().split()) #入力部
    lis = q() #BFS用のQueue
    if x == 0:
        break
    field = [] #これはカーリングの盤面
    for i in range(x):
        field.append(list(map(int, input().split()))) #盤面の入力部
    for i in range(x):
        for j in range(y):
            if field[i][j] == 2:
                start_x, start_y = i,j #開始位置を探す
                field[i][j] = 0
    data = [field,10,start_x,start_y] #これから扱うデータは[盤面、残り試行回数、石のx座標、y座標]とします
    lis.put(data) #とりあえずQueueに初期状態をぶっこむ
    while(lis.qsize()):
        #後はひたすらQueueから状態を持ってきて上下左右に動かしてQueueに入れ直すことを繰り返します
        #ゴールについた瞬間に出力して次のデータセットに移ります
        #一番苦労したのはPythonだとシャローコピーのせいで盤面を直接いじれない点でした
        #かといって二次元配列のディープコピーはめちゃくちゃ遅くTLEが取れませんでした
        #仕方ないので上の実装にあるように無理やり盤面を作る方針にしました
        d = lis.get()
        tmp = l_move(d)
        if flag:
            break
        if tmp != None:
            lis.put(tmp)
        tmp = u_move(d)
        if flag:
            break
        if tmp != None:
            lis.put(tmp)
        tmp = d_move(d)
        if flag:
            break
        if tmp != None:
            lis.put(tmp)
        tmp = r_move(d)
        if flag:
            break
        if tmp != None:
            lis.put(tmp)
    #最後までたどり着かなかったら-1を出力して終わり
    if not flag:
        print(-1)

