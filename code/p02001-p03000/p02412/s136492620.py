def find_conb(result_list,candidate,result,cond):
    
    if len(result)>3:
        return
    
    #2つめの要素の処理で処理が完了する
    #->level3の展開が不要になる
    if len(result)==2:
        res=cond-sum(result)
        if res in candidate:
            result_list.append(result[:]+[res])
            return
        else:
            return
    
    if sum(result) == cond and len(result)==3:
        return
        result_list.append(result[:])
        return
    
    #和が超えたら終了
    if sum(result) > cond:
        return
    
    #候補がなくなったら終了
    if len(candidate) == 0:
        return
    #canditateの最小値がcondを超えたら枝仮
    if candidate[0] >= cond:
        return
    

    
    n=candidate.pop(0)
    
    # print(result[:]+[n])
    find_conb(result_list,candidate[:],result[:]+[n],cond)
    #nを含まないとき
    find_conb(result_list,candidate[:],result[:],cond)
    

def run():
    
    data_list=[]
    
    while True:
        n,x=tuple(map(int,input().split()))
        
        if n==0 and x==0:
            break
        
        data_list.append((n,x))
    
    
    for n,x in data_list:
        #組み合わせの計算
        #動的計画法が必要
        result_list = []
        candidate=[i for i in range(1,n+1)]
        cond=x
        result=[]
        find_conb(result_list,candidate,result,cond)
        
        print(len(result_list))
    # print(result[:]+[n])
    find_conb(result_list,candidate[:],result[:]+[n],cond)
    #nを含まないとき
    find_conb(result_list,candidate[:],result[:],cond)
    

def run():
    
    data_list=[]
    
    while True:
        n,x=tuple(map(int,input().split()))
        
        if n==0 and x==0:
            break
        
        data_list.append((n,x))
    
    
    for n,x in data_list:
        #組み合わせの計算
        #動的計画法が必要
        result_list = []
        candidate=[i for i in range(1,n+1)]
        cond=x
        result=[]
        find_conb(result_list,candidate,result,cond)
        
        print(len(result_list))

run()
