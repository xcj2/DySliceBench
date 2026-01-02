#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_D
#??????????????????

def cal(truck_num, cargos):
    p = 0
    
    for i in range(len(cargos) - truck_num + 1):
        if not i == 0 and p < sum(cargos[:i + 1]):
            continue
        if truck_num > 1:
            r = max(sum(cargos[:i + 1]), cal(truck_num - 1, cargos[i + 1:]))
            if i == 0:
                p = r
            elif p > r:
                p = r
        else:
            return sum(cargos)
    return p

def check(truck_num, carogs, target_load):
    
    cur_truck = 1
    cur_weight = 0
    for weight in cargos:
        cur_weight += weight
        if cur_weight > target_load:
            cur_weight = weight
            cur_truck += 1
            if cur_truck > truck_num:
                return False
    return True

def solve(truck_num, cargs):

    max_load = sum(cargos)
    min_load = max(cargos)
    #print(min_load, max_load)
    while min_load < max_load:
        target_load = int((min_load + max_load)/2)
        if check(truck_num, cargos, target_load):
            max_load = target_load
        else:
            min_load = target_load + 1
        #print(min_load, max_load)
        
    return max_load

if __name__ == "__main__":
    line = input()
    truck_num = int(line.split(" ")[1])
    line_num = int(line.split(" ")[0])
    cargos = [int(input()) for i in range(line_num)]
    print(solve(truck_num,cargos))