#75c
import copy  
  
N,M = map(int, input().split())#M<=50

lines = set()
for _ in range(M):
    a,b = map(int, input().split())
    lines.add((a,b))

#union findを使う###############################################   
def connection_check(lines,start,goal):
    
    #接続追加
    def add_connect(A,B):
        A_parent = get_parent(A)
        B_parent = get_parent(B)

        if A_parent != B_parent:
            parent_dict[B_parent] = A_parent
    #接続有無判断
    def judge_connection(A,B):
        A_parent = get_parent(A) #未更新状態でも、ここで更新される
        B_parent = get_parent(B)

        if A_parent != B_parent:
            return False
        else:
            return True
    #親の取得
    def get_parent(child):
        if child not in parent_dict: #初出なら自分自身を親として追加
            parent_dict[child] = child
        parent = parent_dict[child]
        if parent == child:
            return parent
        else: 
            #最上位の親なら上の等式が成り立つ。不成立ならさらに上位の親を辿る。
            parent_dict[child] = get_parent(parent)
            return parent_dict[child]
    

    parent_dict = dict()
    
    for line in lines:
        A = line[0]
        B = line[1]
        add_connect(A,B)
    
    if judge_connection(start,goal) == True:
        return True
    else:
        return False
        
#################################################################
ans = 0

for line in lines:
    start = line[0]
    goal = line[1]
    remain_lines = copy.copy(lines) 
    remain_lines.remove(line)
    
    #print(start,goal)
    #print(remain_lines)
    
    if connection_check(remain_lines,start,goal) is False:
        ans += 1

print(ans)