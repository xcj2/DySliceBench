import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    H = string_to_int(inputs[0])
    min_h = -1

    if len(H) == 1:
        return "Yes"

    not_operation_start = 0
    for i in range(len(H)-1):
        flg = True
        if H[i] - H[i+1] >= 2:
            return "No"
        elif H[i] - H[i+1] == 1:
            if i - 1 >= 0:
                if H[i] - H[i-1] >= 1:
                    flg = True
                else:
                    flg = False
            else:
                flg = True
            if flg is False and not_operation_start != -1:
                if not_operation_start - 1 >= 0:
                    # if H[not_operation_start] - H[not_operation_start-1] >= 1
                    flg = False
                    for j in range(not_operation_start, i+1):
                        if H[j] - H[j - 1] >= 1:
                            flg = True
                            break
                else:
                    flg = True
            if flg:
                H[i] -= 1
            else:
                return "No"
            not_operation_start = -1
        else:
            if not_operation_start == -1:
                not_operation_start = i
    return "Yes"


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
