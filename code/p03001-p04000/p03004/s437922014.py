N = int(input())

x_list = [0]*N
y_list = [0]*N
d_list = ["A"]*N

for i in range(N):
    x, y, d = input().split()
    x_list[i] = int(x)
    y_list[i] = int(y)
    d_list[i] = d


def _calc_tv(v_keep, v_down, v_up):

    v_0 = min([v_keep, v_down, v_up])

    if v_down == v_0:
        t_1 = 0
        t_2 = 0
        v_c = v_down
    elif v_keep == v_0:
        t_1 = 0
        t_2 = v_down - v_keep
        v_c = v_keep
    else:
        t1 = v_keep - v_up
        t2 = (v_down - v_up) / 2
        if t1 == min([t1, t2]):
            t_1 = t1
            t_2 = v_down - v_keep
            v_c = v_keep
        else:
            t_1 = (v_down - v_up) / 2
            t_2 = t_1
            v_c = (v_down + v_up) / 2

    return t_1, t_2, v_0, v_c


def calc_tv(v_keep, v_down, v_up, reverse=False):

    if reverse:
        t_1, t_2, v_0, v_c = _calc_tv(-v_keep, -v_up, -v_down)
        return t_1, t_2, -v_0, -v_c

    else:
        return _calc_tv(v_keep, v_down, v_up)


# x_min, x_max
x_sub = [x_list[i] for i in range(N) if d_list[i] in ["D", "U"]]
if len(x_sub) > 0:
    x_min_du = min(x_sub)
    x_max_du = max(x_sub)
else:
    x_min_du = 10**10
    x_max_du = -10**10
x_sub = [x_list[i] for i in range(N) if d_list[i] == "L"]
if len(x_sub) > 0:
    x_min_l = min(x_sub)
    x_max_l = max(x_sub)
else:
    x_min_l = 10**10
    x_max_l = -10**10
x_sub = [x_list[i] for i in range(N) if d_list[i] == "R"]
if len(x_sub) > 0:
    x_min_r = min(x_sub)
    x_max_r = max(x_sub)
else:
    x_min_r = 10**10
    x_max_r = -10**10

t_x_min_1, t_x_min_2, v_x_min_0, v_x_min_1 = calc_tv(x_min_du, x_min_l, x_min_r, reverse=False)
t_x_max_1, t_x_max_2, v_x_max_0, v_x_max_1 = calc_tv(x_max_du, x_max_l, x_max_r, reverse=True)

# y_min, y_max
y_sub = [y_list[i] for i in range(N) if d_list[i] in ["L", "R"]]
if len(y_sub) > 0:
    y_min_lr = min(y_sub)
    y_max_lr = max(y_sub)
else:
    y_min_lr = 10**10
    y_max_lr = -10**10
y_sub = [y_list[i] for i in range(N) if d_list[i] == "D"]
if len(y_sub) > 0:
    y_min_d = min(y_sub)
    y_max_d = max(y_sub)
else:
    y_min_d = 10**10
    y_max_d = -10**10
y_sub = [y_list[i] for i in range(N) if d_list[i] == "U"]
if len(y_sub) > 0:
    y_min_u = min(y_sub)
    y_max_u = max(y_sub)
else:
    y_min_u = 10**10
    y_max_u = -10**10

t_y_min_1, t_y_min_2, v_y_min_0, v_y_min_1 = calc_tv(y_min_lr, y_min_d, y_min_u, reverse=False)
t_y_max_1, t_y_max_2, v_y_max_0, v_y_max_1 = calc_tv(y_max_lr, y_max_d, y_max_u, reverse=True)


def calc_v(t, v_type="x_min"):

    type_ind = ["x_min", "x_max", "y_min", "y_max"].index(v_type)

    t_1 = [t_x_min_1, t_x_max_1, t_y_min_1, t_y_max_1][type_ind]
    t_2 = [t_x_min_2, t_x_max_2, t_y_min_2, t_y_max_2][type_ind]
    v_0 = [v_x_min_0, v_x_max_0, v_y_min_0, v_y_max_0][type_ind]
    v_1 = [v_x_min_1, v_x_max_1, v_y_min_1, v_y_max_1][type_ind]
    c = [1, -1, 1, -1][type_ind]

    if t < t_1:
        return v_0 + c * t
    elif t < t_2:
        return v_1
    else:
        return v_1 - c * (t - t_2)


def calc_s(t):
    return (calc_v(t, "x_max") - calc_v(t, "x_min")) * (calc_v(t, "y_max") - calc_v(t, "y_min"))


t_list = [0]
t_list = t_list + [t_x_min_1, t_x_min_2]
t_list = t_list + [t_x_max_1, t_x_max_2]
t_list = t_list + [t_y_min_1, t_y_min_2]
t_list = t_list + [t_y_max_1, t_y_max_2]
# print(t_list)
res = min([calc_s(t) for t in t_list])
print(res)
