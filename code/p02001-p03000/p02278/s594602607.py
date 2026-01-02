#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_D
#????°???????????????????

def processA(target_list, correct_list, i):

    cost = 0
    while not correct_list[i] == target_list[i]:
        min_i = target_list.index(correct_list[i])
        change_i = target_list.index(correct_list[min_i])
        cost += (target_list[min_i] + target_list[change_i])
        target_list[min_i], target_list[change_i] = target_list[change_i], target_list[min_i]
        #print("A", target_list)
    return cost
    
def processB(target_list, correct_list, i):
    minv = correct_list[0]
    target = correct_list[i]

    if minv == target:
        return 10 ** 9
    cost = (minv + target)
    #print(minv, target)
    mmi = target_list.index(minv)
    smi = target_list.index(target)
    target_list[mmi], target_list[smi] = target_list[smi], target_list[mmi]
    
    while not correct_list[i] == target_list[i]:
        min_i = target_list.index(minv)
        change_i = target_list.index(correct_list[min_i])
        cost += (target_list[min_i] + target_list[change_i])
        target_list[min_i], target_list[change_i] = target_list[change_i], target_list[min_i]
        #print("B",target_list)
    return cost
    
def minimum_cost_sort(target_list):
    correct_list = sorted([a for a in target_list])
    cost = 0
    i = 0
    while not correct_list == target_list:
        cost_b = processB([a for a in target_list], correct_list, i)
        cost_a = processA(target_list, correct_list, i)
        cost += min(cost_a, cost_b)
        #print(cost_a, cost_b)
        #print(target_list)
        i += 1
    return cost
def main():
    n_list = input()
    target_list = [int(s) for s in input().split()]
    print(minimum_cost_sort(target_list))
    
if __name__ == "__main__":
    main()