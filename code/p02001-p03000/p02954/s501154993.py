from collections import Counter


def split_RL_block(S):
    N = len(S)
    ret = []

    RL = "R"
    c = "R"
    for i in range(1, N):
        now = S[i]
        if RL == "R" and now == "R":
            c += "R"
        elif RL == "R" and now == "L":
            RL = "L"
            c += "L"
        elif RL == "L" and now == "R":
            ret.append(c)
            RL = "R"
            c = "R"
        else:
            c += "L"
    else:
        ret.append(c)
    return ret


def count_children_RL_border(RL):
    N = len(RL)
    ret = [0] * N
    
    cnt_RL = Counter(RL)
    idx_r = cnt_RL["R"] - 1
    idx_l = idx_r + 1

    r = 0
    l = 0
    for i in range(N):
        if abs(i - idx_r) % 2 == 0:
            r += 1
        else:
            l += 1
    ret[idx_r] = r
    ret[idx_l] = l

    return ret


def main():
    S = input()
    N = len(S)
    RL = split_RL_block(S)
    ans = []
    for rl in RL:
        tmp = count_children_RL_border(rl)
        ans += tmp
    
    print(*ans)


if __name__ == "__main__":
    main()