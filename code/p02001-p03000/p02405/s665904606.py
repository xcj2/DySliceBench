def draw_rect(H,W):
    n=0
    for i in range(H):
        for j in range(W):
            if n % 2 == 0:
                print("#",end="")
            else:
                print(".",end="")
            n+=1
        if W % 2 == 0:
            #幅が偶数なら切り替えて同じ柄から開始する
            n+=1
        print("")



def read_data():
    ls=[]
    while True:
        s,t=tuple(input().split())
        
        H=int(s)
        W=int(t)
        
        if H==0 and W==0:
            break
        
        ls.append((H,W))
        
    return ls


def draw_all_rect(ls):
    for W,H in ls:
        draw_rect(W,H)
        print("")

ls=read_data()
draw_all_rect(ls)
