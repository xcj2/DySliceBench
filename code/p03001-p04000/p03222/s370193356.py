import itertools

def fibonacci(n):
    if (n == 0):
        f_n = 1
    elif (n == 1):
        f_n = 1
    else:
        f_n = fibonacci(n-1) + fibonacci(n-2)

    return f_n

def X_amida_number(W, W_i):
    x_amida = "0" * (W - 1)
    left_x_amida = x_amida[:(W_i-2)] if(W_i-2 >= 0) else ""
    right_x_amida = x_amida[(W_i+1):]

    return fibonacci(len(left_x_amida) + 1) * fibonacci(len(right_x_amida) + 1)

def Y_amida_number(W, W_i):
    y_amida = "0" * (W - 1)
    left_y_amida = y_amida[:W_i-1] if(W_i-1 >= 0) else ""
    right_y_amida = y_amida[W_i+1:]

    return fibonacci(len(left_y_amida) + 1) * fibonacci(len(right_y_amida) + 1)

def Z_amida_number(W, W_i):
    z_amida = "0" * (W - 1)
    left_z_amida = z_amida[:W_i-1] if(W_i-1 >= 0) else ""
    right_z_amida = z_amida[W_i+2:]

    return fibonacci(len(left_z_amida) + 1) * fibonacci(len(right_z_amida) + 1)

def amida_all(amida_list, W):
    for i, j in itertools.product(range(W), range(3)):
        if(j == 0):
            amida_list[i][j] = X_amida_number(W, i)
        elif(j == 1):
            amida_list[i][j] = Y_amida_number(W, i)
        else:
            amida_list[i][j] = Z_amida_number(W, i)

    return amida_list

H, W, K = map(int, input().split())
amida_list = [[0]*3 for i in range(W)]
amida_list = amida_all(amida_list, W)

seed_dp_array = [0 for i in range(W)]
dp_array = [list(seed_dp_array) for i in range(H + 1)]
dp_array[0][0] = 1

for H_i, W_i in itertools.product(range(1, H + 1), range(W)):
    if (W_i == 0):
        if(W == 1):
            dp_array[H_i][0] = dp_array[H_i - 1][W_i] * amida_list[W_i][1]
        else:
            dp_array[H_i][0] = dp_array[H_i - 1][W_i] * amida_list[W_i][1] + dp_array[H_i - 1][W_i + 1] * amida_list[W_i][2]
    elif (W_i == (W - 1)):
        dp_array[H_i][W - 1] = dp_array[H_i - 1][W_i - 1] * amida_list[W_i][0] + dp_array[H_i - 1][W_i] * amida_list[W_i][1]
    else:
        dp_array[H_i][W_i] = dp_array[H_i - 1][W_i - 1] * amida_list[W_i][0] + dp_array[H_i - 1][W_i] * amida_list[W_i][1] + dp_array[H_i - 1][W_i + 1] * amida_list[W_i][2]

print(dp_array[H][K - 1] % 1000000007)