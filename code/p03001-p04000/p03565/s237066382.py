# coding: utf-8
def get_ln_inputs():
    return input().split()


def map_list(fn, xs):
    return list(map(fn, xs))


def get_ln_int_inputs():
    return map_list(int, get_ln_inputs())


def possible_to_insert(S, T, index):
    if index + len(T) > len(S):
        return False
    for i in range(len(T)):
        if S[index + i] != "?" and S[index + i] != T[i]:
            return False
    return True


def main():
    S = get_ln_inputs()[0]
    T = get_ln_inputs()[0]

    ins_idx = -1
    for i in range(len(S)):
        if possible_to_insert(S, T, i):
            ins_idx = i

    if ins_idx == -1:
        print("UNRESTORABLE")
        return

    S = S[:ins_idx] + T + S[ins_idx + len(T):]
    print(S.replace("?", "a"))

    return


main()