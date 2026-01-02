def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

def read_s_list_loop(n):
    return [input() for _ in range(n)]

def bit_cal(n):
    return_list = ['']* (2 ** n)
    for i in range(2 ** n):
        for j in range(n):
            if ((i >> j) & 1):
                return_list[i] = return_list[i] + '1'
            else:
                return_list[i] = return_list[i] + '0'
    return return_list

N,M,X = read_int_map()
Cn = [list(read_int_map()) for _ in range(N) ]

ans = float('inf')
bit_list = bit_cal(N)
for bit in bit_list:
    m_list = [0]*M
    price = 0
    for i in range(N):
        if bit[i] == '1':
            price += Cn[i][0]
            for j in range(1,M+1):
                m_list[j-1] += Cn[i][j]
    flag = True
    for m in m_list:
        if m < X:
            flag = False
            break
    if flag:
        ans = min(price,ans)
if ans == float('inf'):
    print(-1)
else:
    print(ans)