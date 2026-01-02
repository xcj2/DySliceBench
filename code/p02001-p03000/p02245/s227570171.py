import sys;
import heapq

def iterative(i,j):
    q = []
    heapq.heappush(q,(sumcost,(0,i,j,0,puz)))
    global finding

    while len(q):
        cost, items = heapq.heappop(q)
        c_depth = items[0]
        _i = items[1]
        _j = items[2]
        prev_move = items[3]
        c_puz = items[4]
        _sum_cost = cost - c_depth
        if(_sum_cost == 0):
            finding = 1
            print(c_depth)
            break
        if(cost > depth):
            continue

        c_cost = HS(_i,_j,c_puz[_i*3+_j])

        if(_i != 0 and prev_move != 1):
            swap_puz = swapPuz(c_puz[0:],_i,_j,_i-1,_j)
            n_cost = cost+1+checkCost(c_cost,HS(_i-1,_j,c_puz[(_i-1)*3+_j]),HS(_i,_j,swap_puz[_i*3+_j]),HS(_i-1,_j,swap_puz[(_i-1)*3+_j]))
            if(n_cost <= depth):
                heapq.heappush(q,(n_cost,(c_depth+1,_i-1,_j,2,swap_puz)))
        if(_i != 2 and prev_move != 2):
            swap_puz = swapPuz(c_puz[0:],_i,_j,_i+1,_j)
            n_cost = cost+1+checkCost(c_cost,HS(_i+1,_j,c_puz[(_i+1)*3+_j]),HS(_i,_j,swap_puz[_i*3+_j]),HS(_i+1,_j,swap_puz[(_i+1)*3+_j]))
            if(n_cost <= depth):
                heapq.heappush(q,(n_cost,(c_depth+1,_i+1,_j,1,swap_puz,)))
        if(_j != 0 and prev_move != 3):
            swap_puz = swapPuz(c_puz[0:],_i,_j,_i,_j-1)
            n_cost = cost+1+checkCost(c_cost,HS(_i,_j-1,c_puz[_i*3+_j-1]),HS(_i,_j,swap_puz[_i*3+_j]),HS(_i,_j-1,swap_puz[_i*3+_j-1]))
            if(n_cost <= depth):
                heapq.heappush(q,(n_cost,(c_depth+1,_i,_j-1,4,swap_puz)))
        if(_j != 2 and prev_move != 4):
            swap_puz = swapPuz(c_puz[0:],_i,_j,_i,_j+1)
            n_cost = cost+1+checkCost(c_cost,HS(_i,_j+1,c_puz[_i*3+_j+1]),HS(_i,_j,swap_puz[_i*3+_j]),HS(_i,_j+1,swap_puz[_i*3+_j+1]))
            if(n_cost <= depth):
                heapq.heappush(q,(n_cost,(c_depth+1,_i,_j+1,3,swap_puz)))

def checkCost(c_cost,m_cost,c2_cost,m2_cost):
    return c2_cost - c_cost + m2_cost - m_cost

def sumCost(puz):
    value = 0
    for i in range(3):
        value += HS(i,0,puz[i*3])
        value += HS(i,1,puz[i*3+1])
        value += HS(i,2,puz[i*3+2])
    return value

def HS(i,j,num):
    if(num != 0):
        k = num-1
    else:
        k = 8
    ki = (int)(k/3)
    kj = k - ki*3
    value = abs(i-ki)+abs(j-kj)
    return value


def swapPuz(c_puz, i, j, i2,j2):
    c_puz[i2*3+j2],c_puz[i*3+j] = c_puz[i*3+j],c_puz[i2*3+j2]
    return c_puz

correctPuz = [i+1 for i in range(9)]
correctPuz[8] = 0
puz = [0 for i in range(9)]

i_start = 0
j_start = 0

for i in range(3):
    puz[i*3],puz[i*3+1],puz[i*3+2] = map(int, input().split());
    if(puz[i*3] == 0):
        i_start,j_start = i,0
    elif(puz[i*3+1] == 0):
        i_start,j_start = i,1
    elif(puz[i*3+2] == 0):
        i_start,j_start = i,2

sumcost = sumCost(puz)

finding = 0
depth = 0
while True:
    if(finding == 1):
        break
    iterative(i_start,j_start)
    depth+=1

