import itertools

def input_data():
    n = int(input())
    a = []
    tmp_list = []
    lst = []
    for i in range(n):
        tmp_list = []
        tmp_a = int(input())
        a.append(tmp_a)
        for j in range(tmp_a):
            x,y = map(int,input().split())
            tmp_list.append([x-1,y])
        lst.append(tmp_list)
    return n,a,lst

def comb(x):
    return list(itertools.combinations(range(n),x))

def check(honests):
    flag = True
    check_list = [0]*n
    for i in honests:
        check_list[i] = 1
    for i in honests:
        for e in lst[i]:
            if (check_list[e[0]] != e[1]):
                flag = False
                break
        if not flag:
            break
    return flag    
  
def main():
    for i in reversed(range(n+1)):
        for honests in comb(i):
            if check(honests):
                return i

n,a,lst = input_data()
print(main())