## coding: UTF-8
N = int(input())
s = input().split()
l1 = [int(p) for p in s]
s2 = input().split()
l2 = [int(p) for p in s2]

#print(N)
#print(l1)
#print(l2)
#print(sum(l1[2:]))

def Cumulative_sum(l):
    output_list = []
    for i in range(len(l)):
        output_list.append(sum(l[:i+1]))
    return output_list

#print(Cumulative_sum(l1))
#print(Cumulative_sum(l2))
#print(Cumulative_sum(l2)[len(l2)-1])


def calc_sum(cut_off):
    if(cut_off != 0):
        add = Cumulative_sum(l1)[cut_off] + Cumulative_sum(l2)[len(l2)-1] - Cumulative_sum(l2)[cut_off - 1]
    else:
        add = Cumulative_sum(l1)[cut_off] + Cumulative_sum(l2)[len(l2)-1]
    return add

#print(calc_sum(0))
#print(calc_sum(1))
#print(calc_sum(2))

answer = 0
for i in range(N):
    if(answer <= calc_sum(i)):
        answer = calc_sum(i)
        #print(answer)
print(answer)

'''
answer = 0

mode = 1 #上の段

def countup(mode, index):
    if(mode == 1):
        add = l1[index]
    if(mode == 2):
        add = l2[index]
    return add


answer += countup(mode, 0)
for i in range(1,N):
    #print(sum(l1[i:]))
    #print(sum(l2[i-1:]))
    if( mode == 1 and sum(l1[i:]) < sum(l2[i-1:]) ):
        mode = 2 #下の段に移動
        answer += countup(mode, i-1)
    #print('mode:{}, index:{}'.format(mode, i))
    answer += countup(mode, i)
if(N == 1):
    answer += l2[0]
print(answer)
'''




