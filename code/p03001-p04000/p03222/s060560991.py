def amida_counter(H_i_amida_list):
    counter = 0

    for amida_bin in range(2**len(H_i_amida_list)):
        if (("11" in format(amida_bin, "b")) == False):
            counter += 1

    return counter

def amida_number(left_amida, right_amida):
    left_counter = amida_counter(left_amida) if(len(left_amida) > 0) else 1
    right_counter = amida_counter(right_amida) if(len(right_amida) > 0) else 1

    return (left_counter * right_counter)

def X_amida_number(W, W_i):
    x_amida = "0" * (W - 1)
    left_x_amida = x_amida[:(W_i-2)] if(W_i-2 >= 0) else ""
    right_x_amida = x_amida[(W_i+1):]

    return amida_number(left_x_amida, right_x_amida)

def Y_amida_number(W, W_i):
    y_amida = "0" * (W - 1)
    left_y_amida = y_amida[:W_i-1] if(W_i-1 >= 0) else ""
    right_y_amida = y_amida[W_i+1:]

    return amida_number(left_y_amida, right_y_amida)

def Z_amida_number(W, W_i):
    z_amida = "0" * (W - 1)
    left_z_amida = z_amida[:W_i-1] if(W_i-1 >= 0) else ""
    right_z_amida = z_amida[W_i+2:]

    return amida_number(left_z_amida, right_z_amida)

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