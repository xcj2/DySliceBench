def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

def read_s_list_loop(n):
    return [input() for _ in range(n)]

N,M = read_int_map()
Hn = read_int_list()
tree_list = [[] for i in range(N)]
for _ in range(M):
    A,B = read_int_map()
    A -= 1
    B -= 1
    tree_list[A].append(B)
    tree_list[B].append(A)
ans = 0
for i in range(len(tree_list)):
    depend = tree_list[i]
    base_high = Hn[i]
    flag = True
    for i2 in depend:
        compare_high = Hn[i2]
        if base_high <= compare_high:
            flag = False
            break
    if flag:
        ans += 1
print(ans)