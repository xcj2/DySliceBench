h,w = map(int,input().split())
lst1 = [list(list(input())) for i in range(h)]

lst2 = [[0 for j in range(w)] for i in range(h)]

def search_of_height_branch(i,j):
    height = 0
    while True:
        if i >= h or lst1[i][j] == "#":
            break
        height += 1
        i += 1
    return height
        
def search_of_width_branch(i,j):
    width = 0
    while True:
        if j >= w or lst1[i][j] == "#":
            break
        width += 1
        j += 1
    return width

def search_of_height():
    flag = 0
    for i in range(w):
        flag = 0
        for j in range(h):
            if lst1[j][i] == "." and flag==0:
                point = search_of_height_branch(j,i)
                lst2[j][i] += point
                flag = 1
            elif lst1[j][i] == ".":
                lst2[j][i] += point
            else:
                flag = 0

def search_of_width():
    flag = 0
    for i in range(h):
        flag = 0
        for j in range(w):
            if lst1[i][j] == "." and flag==0:
                point = search_of_width_branch(i,j)
                lst2[i][j] += point
                flag = 1
            elif lst1[i][j] == ".":
                lst2[i][j] += point
            else:
                flag = 0

if __name__ == "__main__":
    search_of_height()
    search_of_width()
    ans = 0
    for i in range(h):
        ans = max(ans,max(lst2[i]))
    print(ans-1) #交差している点が重複して数えているので-1