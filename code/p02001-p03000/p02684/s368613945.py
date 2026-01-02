def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

def read_s_list_loop(n):
    return [input() for _ in range(n)]

N,K = read_int_map()
An = read_int_list()
memo = [0]*(N+1)
memo_indx = [0]*(N+1)
memo[1] = 1
memo_indx[1] = 0
seq_an = [1]
next_place = An[0]
for i in range(len(An)):
    if memo[next_place] == 0:
        seq_an.append(next_place)
        memo[next_place] = 1
        memo_indx[next_place] = i + 1
        next_place = An[next_place-1]
    else:
        break
loop_idx = memo_indx[next_place]
loop_list = seq_an[loop_idx:]
if K <= len(seq_an)-1:
    print(seq_an[K])
else:
    num = (K - len(seq_an)) % len(loop_list)
    print(loop_list[num])