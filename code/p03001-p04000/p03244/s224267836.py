N=int(input())
n=list(map(int,input().split()))

#Binary tree
class Node:
    def __init__(self, x):
        self.data  = x
        self.left  = None
        self.right = None
        self.count = 1

class BST:
    def __init__(self, number_list): #コンストラクタ
        self.root = None #ルートノード初期化
        for node in number_list: #数値を持つ配列から二分木を生成
            self.insert(node) #挿入メソッドを使ってノードを挿入する

    def insert(self, data):
        n = self.root #nにルートを代入
        if n == None: #ルートに何も入っていない場合
            self.root = Node(data) #ルートにノードを代入(二分探索木の一番上の部分が出来る)
            return #呼び出し部分に戻る
        else: #ルートノードに既に数値が入ってる場合
            while True: #return等が入るまでずっと実行
                entry = n.data #entryにnが持つデータ(数値)を入れる
                if data < entry: #entryとdata(代入するデータ)を比較してentryの方が大きい場合
                    if n.left is None: #nの左エッジに何も入っていない場合
                        n.left = Node(data) #nの左エッジにdata(代入するデータ)を代入
                        return ##呼び出し部分に戻る
                    n = n.left #nの左に何か入っている場合nにnのleftを代入
                elif data > entry: #entryとdata(代入するデータ)を比較してentryの方が小さい場合
                    if n.right is None: #nの右エッジに何も入っていない場合
                        n.right = Node(data) #nの右エッジにdata(代入するデータ)を代入
                        return #呼び出し部分に戻る
                    n = n.right #nの右エッジに何か入っている場合nにnのrightを代入
                else: #上2つの条件分岐以外の場合
                    n.data = data #nのdataにdata(代入するデータ)を代入
                    n.count+=1
                    return #呼び出し部分に戻る


    def traverse(self,node,func,len):
        if node is not None:
            len.append([node.count,node.data])
            self.traverse(node.right,func,len)
            self.traverse(node.left,func,len)
        return len


def print_data(x): 
    print(x)

def append_data(l,x):
    l.append(x)
#end

#Divide it into even and odd
n1=[]
n2=[]
for i in range(N//2):
    n1.append(n[i*2])
    n2.append(n[i*2-1])
#end

#insert tree
tree1=BST(n1)
tree2=BST(n2)
#end

#make lile {key,value} 
cn1=[]
cn1=tree1.traverse(tree1.root,append_data,cn1)
cn2=[]
cn2=tree2.traverse(tree2.root,append_data,cn2)
#end

#for example(4,1 1 1 1)
cn1.append([0,0])
cn2.append([0,0])
#end

#sort
    #first input
sum1=0
sum2=0
if cn1[0][0]>=cn1[1][0]:
    max11=cn1[0][0]
    num11=cn1[0][1]

    max12=cn1[1][0]
    num12=cn1[1][1]
else:
    max11=cn1[1][0]
    num11=cn1[1][1]

    max12=cn1[0][0]
    num12=cn1[0][1]


if cn2[0][0]>=cn2[1][0]:
    max21=cn2[0][0]
    num21=cn2[0][1]

    max22=cn2[1][0]
    num22=cn2[1][1]
else:
    max21=cn2[1][0]
    num21=cn2[1][1]

    max22=cn2[0][0]
    num22=cn2[0][1]
    #end

for i in range(2,len(cn1)):
    if max12<cn1[i][0]:
        if max11<cn1[i][0]: #if new one is max
            sum1+=max12

            max12=max11
            num12=num11

            max11=cn1[i][0]
            num11=cn1[i][1]
        else:                #if new one is second max
            sum1+=max12

            max12=cn1[i][0]
            num12=cn1[i][1]
    else:
        sum1+=cn1[i][0]


for i in range(2,len(cn2)):
    if max22<cn2[i][0]:
        if max21<cn2[i][0]: #if new one is max
            sum2+=max22

            max22=max21
            num22=num21

            max21=cn2[i][0]
            num21=cn2[i][1]
        else:               #if new one is second max
            sum2+=max22

            max22=cn2[i][0]
            num22=cn2[i][1]
    else:
        sum2+=cn2[i][0]
#end

#answer
if num11 != num21:
    ans=sum1+sum2+max12+max22
elif max11-max12 > max21-max22:#prefer large disadvantage  
    ans=sum1+sum2+max12+max21
else:
    ans=sum1+sum2+max11+max22
print(ans)
#end