def input_int():
    return map(int, input().split())

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

K=one_int()



def solve(start, goal, lists):
    ret_lists=[]
    
    for i in lists:
        str_i = str(i)
        t = int(str_i[-1])
        
        if t==0:
            ret_lists.append(i*10)
            start+=1
            if start==goal:
                return ret_lists, start
            
            ret_lists.append(i*10+1)
            start+=1
            if start==goal:
                return ret_lists, start

        elif t==9:
            ret_lists.append(i*10+8)
            start+=1
            if start==goal:
                return ret_lists, start
            
            ret_lists.append(i*10+9)
            start+=1
            if start==goal:
                return ret_lists, start
        
        else:
            for s in range(-1,2):
                ret_lists.append(i*10+int(t)+s)
                start+=1
                if start==goal:
                    return ret_lists, start
  
    return ret_lists, start

if K>9:
    lists = [i for i in range(1,10)]
    start = 9
    while True:
        lists, start = solve(start, K, lists)
        if K<=start:
            print(lists[-1])
            break
else:
    print(K)