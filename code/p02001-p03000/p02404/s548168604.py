def draw_rect(H,W):
    for i in range(H):
        for j in range(W):
            if i==0 or i==H-1:
                print("#",end="")
            elif j==0 or j==W-1:
                print("#",end="")
            else:
                print(".",end="")
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
