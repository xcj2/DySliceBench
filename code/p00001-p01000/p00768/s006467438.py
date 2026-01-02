from inspect import currentframe


def debug_print(s):
    # print(s)
    return


def debug_key(*args):
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    debug_print(', '.join(names.get(id(arg), '???')+' = '+repr(arg) for arg in args))


def solve(M, T, P, R, m, t, p, j):
    debug_print("\n-----solve-----")
    AC_COUNT = 0
    TEAM_NUMBER = 2
    SUM_TIME = 1
    QUE_NUMBER = 3


    record = [[0, 0, i + 1] + [0] * P for i in range(T)]
    debug_print(record)

    for i in range(R):
        if j[i] == 0:
            record[t[i] - 1][AC_COUNT] += 1
            record[t[i] - 1][SUM_TIME] -= m[i] + record[t[i] - 1][QUE_NUMBER + p[i] - 1] * 20
        else:
            record[t[i] - 1][QUE_NUMBER + p[i] - 1] += 1

    record.sort()
    record.reverse()
    debug_print(record)

    ans = str(record[0][TEAM_NUMBER])

    for i in range(1, T):
        if record[i][SUM_TIME] == record[i-1][SUM_TIME] and record[i][AC_COUNT] == record[i-1][AC_COUNT]:
            ans += "=" + str(record[i][TEAM_NUMBER])
        else:
            ans += "," + str(record[i][TEAM_NUMBER])

    print(ans)


    return


if __name__ == '__main__':

    while True:
        M_input, T_imput, P_imput, R_imput = map(int, input().split())
        if M_input == T_imput == P_imput == R_imput == 0:
            break
        m_input = [0 for _ in range(R_imput)]
        t_input = [0 for _ in range(R_imput)]
        p_input = [0 for _ in range(R_imput)]
        j_input = [0 for _ in range(R_imput)]

        for i in range(R_imput):
            m_input[i], t_input[i], p_input[i], j_input[i] = map(int, input().split())

        solve(M_input, T_imput, P_imput, R_imput, m_input, t_input, p_input, j_input)


