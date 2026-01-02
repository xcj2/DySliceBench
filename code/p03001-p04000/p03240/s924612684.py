n = int(input())
data=[]
for i in range(0,n):
    x, y, h = map(int,input().split())
    data.append((x,y,h))
data = sorted(data,key=lambda x:x[2],reverse=True)
st_x, st_y, st_h = data[0]
 
 
def get_search_area(x,y,n):
    area_list=[]
    for i in range(-n,n+1):
        for j in range(-n,n+1):
            if abs(i) == n or abs(j) == n:
                xi = x+i
                yi = y+j
                if 0<= xi <= 100 and 0 <= yi <= 100:
                    area_list.append((x+i, y+j, abs(i)+abs(j) ))
    return area_list
 
def meets_all_conditions(top, top_h,data):
    top_x, top_y, top_z = top
    top_h += top_z
    for item in data:
        pt_x, pt_y, pt_h = item
        tmp = max(top_h - abs(pt_x - top_x) - abs(pt_y - top_y), 0)       
        if pt_h != tmp:
            #print(pt_h, tmp ,"False")
            return False    
    #print("True")
    return True
    
def main():    
    for i in range(200):
        #print(i)
        a = get_search_area(st_x,st_y,i)
        #print(a)
        for item in a:
            if meets_all_conditions(item, st_h , data):
                print("{} {} {}".format(item[0],item[1],st_h+item[2]))
                return
    return
main()