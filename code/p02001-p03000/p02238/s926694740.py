# -*- coding: utf-8 -*-

def DFS_stack(adj, start):
    n = len(adj)
    d = [0] * n
    f = [0] * n
    flag = [0] * n # 0:????¨????, 1:?¨??????????, 2:?¨??????????
    S = []
    time = 1

    S.append(start)
    flag[start] = 1
    d[start] = time
    time = time + 1
    
    while flag.count(2) != n: # ??¨????????????????????¢?´¢????????????????????§
        if len(S) != 0:
            u = S.pop()
            v = [i for i, x in enumerate(adj[u]) if (x == 1) and (flag[i] == 0)] 
            # v := ??£??\???????????????????????¢?´¢??????????????????
            if len(v) != 0:
                S.append(u)
                S.append(v[0])
                flag[v[0]] = 1
                d[v[0]] = time
                time = time + 1
            else:
            #??£??\??????????????¨????¨??????????
                flag[u] = 2
                f[u] = time
                time = time + 1

        else:
        	#??????????????????????????£?????´????????¢?´¢??????????????????????????¢?´¢????§?
            u = flag.index(0)
            S.append(u)
            flag[u] = 1
            d[u] = time
            time = time + 1            

    return d, f    

def DFS(adj, start):
    
    n = len(adj)
    d = [0] * n
    f = [0] * n
    flag = [0] * n
    time = 1
    
    def DFS_recursive(u, time):
        #print(u, flag)
        flag[u] = 1
        d[u] = time
        time = time + 1
        v = [i for i, x in enumerate(adj[u]) if x == 1]
        for i in v:
            if flag[i] == 0:
                time = DFS_recursive(i, time)
        flag[u] = 2
        f[u] = time
        time = time + 1
        return time
        
    time = DFS_recursive(start, time)
    for i in range(n):
        if flag[i] == 0:
           time =  DFS_recursive(i, time)
    
    return d, f



def main():
    
    n = int(input())
    adj = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        tmp = list(map(int, input().split()))
        u = tmp[0]
        u = u -1
        k = tmp[1]
        v = tmp[2:]
        for j in range(k):
            adj[u][v[j]-1] = 1
            
    #d, f = DFS_stack(adj, 0)
    d, f = DFS(adj, 0)
    for i in range(n):
        print(i+1, d[i], f[i])

if __name__ == "__main__":
    main()    