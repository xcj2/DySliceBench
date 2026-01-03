import sys
line = []
for i in sys.stdin.readlines():
    line.append(i.rstrip())
data = line.pop(0).split(" ")
num_list = line.pop().split(" ")

def pick_up(num_list):
    use_list = ['0','1','2','3','4','5','6','7','8','9']
    for i in num_list:
        use_list.remove(i)
    return use_list

def advance(n_list, num):
    n_list[len(n_list)-1] += 1
    while((num) in n_list):
        chk = n_list.index(num)
        if chk == 0:
            return [0 for i in range(len(n_list))]
        else:
            n_list[chk] = 0
            n_list[chk-1] += 1
    return n_list

def solve(num, num_list):
    use_list = pick_up(num_list)
    ans_list = [0 for i in range(len(num))]
    count = 0

    while(count < len(use_list)**len(ans_list)):
        ans_num = ""
        for i in ans_list:
            ans_num += use_list[i]
        if (int(ans_num) - int(num) >= 0):
            break
        ans_list = advance(ans_list, len(use_list))
        count += 1

    if count == len(use_list)**len(ans_list):
        ans_num = ""
        if use_list[0] != "0":
            for i in range(len(num)+1):
                ans_num += use_list[0]
        else:
            ans_num += use_list[1]
            for i in range(len(num)):
                ans_num += use_list[0]
    
    return ans_num
    
def main():
    print(solve(data[0], num_list))
    
if __name__ == '__main__':
    main()