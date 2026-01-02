def X_amida_number(W, W_i):
    x_amida = "0" * (W - 1)

    if (W_i-2 >= 0):
        left_x_amida = x_amida[:(W_i-2)]
    else:
        left_x_amida = ""

    right_x_amida = x_amida[(W_i+1):]

    if(len(left_x_amida) > 0):
        left_counter = 0

        for left_bin in range(2**len(left_x_amida)):
            if (("11" in format(left_bin, "b")) == False):
                left_counter += 1
    else:
        left_counter = 1

    if(len(right_x_amida) > 0):
        right_counter = 0

        for right_bin in range(2**len(right_x_amida)):
            if (("11" in format(right_bin, "b")) == False):
                right_counter += 1

    else:
        right_counter = 1

    return (left_counter * right_counter)

def Y_amida_number(W, W_i):
    y_amida = "0" * (W - 1)

    if (W_i-1 >= 0):
        left_y_amida = y_amida[:W_i-1]
    else:
        left_y_amida = ""

    right_y_amida = y_amida[W_i+1:]

    if(len(left_y_amida) > 0):
        left_counter = 0

        for left_bin in range(2**len(left_y_amida)):
            if (("11" in format(left_bin, "b")) == False):
                left_counter += 1
    else:
        left_counter = 1

    if(len(right_y_amida) > 0):
        right_counter = 0

        for right_bin in range(2**len(right_y_amida)):
            if (("11" in format(right_bin, "b")) == False):
                right_counter += 1
    else:
        right_counter = 1

    return (left_counter * right_counter)

def Z_amida_number(W, W_i):
    z_amida = "0" * (W - 1)

    if (W_i-1 >= 0):
        left_z_amida = z_amida[:W_i-1]
    else:
        left_z_amida = ""

    right_z_amida = z_amida[W_i+2:]

    if(len(left_z_amida) > 0):
        left_counter = 0

        for left_bin in range(2**len(left_z_amida)):
            if (("11" in format(left_bin, "b")) == False):
                left_counter += 1
    else:
        left_counter = 1

    if(len(right_z_amida) > 0):
        right_counter = 0

        for right_bin in range(2**len(right_z_amida)):
            if (("11" in format(right_bin, "b")) == False):
                right_counter += 1
    else:
        right_counter = 1

    return (left_counter * right_counter)


H, W, K = map(int, input().split())

seed_dp_array = [0 for i in range(W)]
dp_array = [list(seed_dp_array) for i in range(H + 1)]
dp_array[0][0] = 1

for H_i in range(1, H + 1):
    for W_i in range(W):
        if (W_i == 0):
            if(W == 1):
                dp_array[H_i][0] = dp_array[H_i - 1][W_i] * Y_amida_number(W, W_i)
            else:
                dp_array[H_i][0] = dp_array[H_i - 1][W_i] * Y_amida_number(W, W_i) + dp_array[H_i - 1][W_i + 1] * Z_amida_number(W, W_i)
        elif (W_i == (W - 1)):
            dp_array[H_i][W - 1] = dp_array[H_i - 1][W_i - 1] * X_amida_number(W, W_i) + dp_array[H_i - 1][W_i] * Y_amida_number(W, W_i)
        else:
            dp_array[H_i][W_i] = dp_array[H_i - 1][W_i - 1] * X_amida_number(W, W_i) + dp_array[H_i - 1][W_i] * Y_amida_number(W, W_i) + dp_array[H_i - 1][W_i + 1] * Z_amida_number(W, W_i)

print(dp_array[H][K - 1] % 1000000007)