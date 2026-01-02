def create_decrement_list(num):
    decrement_list = []
    while(num >= 0):
        decrement_list.append(num)
        num -=2
    return decrement_list

def check_route(num_list, offset):
    is_path_possible = False
    for num in num_list:
        if offset == num:
            is_path_possible = True
            break
    return is_path_possible

def route_checker(N, list_t, list_x, list_y):
    for n in range(N):
        if n == 0:
            offset_x = abs(list_x[n])
            offset_y = abs(list_y[n])
        else:
            offset_x = abs (list_x[n] - list_x[n-1])
            offset_y = abs (list_y[n] - list_y[n-1])
        offset_total = offset_x + offset_y
        time_offset = list_t[n] if n==0 else list_t[n] - list_t[n-1]
        time_offset_list = create_decrement_list(time_offset)
        if check_route(time_offset_list, offset_total)==False:
            print("No")
            break
    else:
        print("Yes")

N = int(input())
t = []
x = []
y = []
# 要素を配列に格納
for i in range(N):
    a_list = list(map(int, input().split()))
    t.append(a_list[0])
    x.append(a_list[1])
    y.append(a_list[2])

route_checker(N, t, x, y)