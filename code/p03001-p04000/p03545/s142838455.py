import queue

def check(operator_list, num_list):
    res = num_list[0]
    for i, op in enumerate(operator_list):
        if op == '+':
            res += num_list[i + 1]
        elif op == '-':
            res -= num_list[i + 1]

    return res == 7

def concat(operator_list, num_list):
    res = str(num_list[0])
    for op, num in zip(operator_list, num_list[1:]):
        res += op
        res += str(num)

    return res + "=7"

def solve():
    line = input()
    num_list = []
    for s in line:
        num_list.append(int(s))

    q = queue.Queue()
    q.put([])
    N = len(num_list)
    while not q.empty():
        operator_list = q.get()
        # print(operator_list)
        if len(operator_list) == N - 1:
            if check(operator_list, num_list):
                return concat(operator_list, num_list)

        else:
            q.put(operator_list + [ '+' ])
            q.put(operator_list + [ '-' ])

    return "No Answer"


print(solve())
