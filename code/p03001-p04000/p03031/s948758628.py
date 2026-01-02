import sys
N, M = map(int, input().split())
k_list_list = []
for m in range(M):
    k_list_list.append(list(map(int, input().split()[1:])))
p_list = list(map(int, input().split()))
    
def add_num(on_off_list_list):
    new_list = []
    for on_off_list in on_off_list_list:
        for i in [[0], [1]]:
            new_list.append(on_off_list+i)
    return new_list

def create_on_off_list(N):
    on_off_list_list = [[]]
    for n in range(N):
        on_off_list_list = add_num(on_off_list_list)
    return on_off_list_list

def check(k_list, p, on_off_list):
    total = 0
    for k in k_list:
        k -= 1
        swich = on_off_list[k]
        if swich == 1:
            total += 1
    if total%2 == p:
        return True
    else:
        return False

def main():
    on_off_list_list = create_on_off_list(N)
    ans = 0
    for on_off_list in on_off_list_list:
        for k_list, p in zip(k_list_list, p_list):
            if check(k_list, p, on_off_list): continue
            else: break
        else:
            ans += 1
    print(ans)
    
main()