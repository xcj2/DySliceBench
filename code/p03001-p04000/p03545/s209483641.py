import sys

def check(operate_list, num_list):
    res = num_list[0]
    for i, op in enumerate(operate_list):
        if op == "+":
            res += num_list[i+1]
        elif op == "-":
            res -= num_list[i+1]
    return res == 7

def concat(operate_list, num_list):
    num_list = list(map(str, num_list))
    string = num_list[0]
    for op, num in zip(operate_list, num_list[1:]):
        # it is beautiful!
        string += op
        string += num
    string += "=7"
    return string

def main():
    line = sys.stdin.readline().strip()
    num_list = []
    for s in line:
        num_list.append(int(s))
    result = ""
    stack = []
    stack.append([])
    N = len(num_list)
    while(len(stack) != 0):
        l = stack.pop()
        if len(l) == N-1:
            if check(l, num_list):
                result = concat(l, num_list)
                break
        else:
            stack.append(l + ["+"]) # careful code
            stack.append(l + ["-"])

    print(result)

if __name__ == "__main__":
    main()
