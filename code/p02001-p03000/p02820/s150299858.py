import math


N, K = map(int, input().split(" "))
R, S, P = map(int, input().split(" "))
T = input()



# print(N, K, R, S, P)


# Lets wrirte a  Greedy SOlution

mapped_dict = {
    0 : "r",
    1 : "s",
    2 : "p"
}
reverse_mapped_dict = {
    "r" : 0,
    "s" : 1,
    "p" : 2
}

def determine_R_P_S(val):
    if val == "r":
        # print("p")
        return "p"
    elif val == "p":
        # print("s")
        return "s"
    else:
        # print("r")
        return "r"
    
def add_profit(machine_val, you_played, succeed, R, P, S):
    if machine_val == "r":
        if succeed == 1:
            return P
        else:
            return 0

    if machine_val == "p":
        if succeed == 1:
            return S
        else:
            return 0

    if machine_val == "s":
        if succeed == 1:
            return R
        else:
            return 0
    


def total_profit(T, R, P, S, K, N):
    profit = 0
    S_played = ""
    for i in range(0, K):
        I_played = determine_R_P_S(T[i])
        S_played += I_played
        # print("SHOULD PLAY")
        # print(S_played)   
        # print(i)
        # print(I_played)
        # print()
        profit += add_profit(T[i], I_played, 1, R, P, S)

    for i in range(K, N):
        I_played = determine_R_P_S(T[i])
        I_played_previous = S_played[i - K]
        # # print("SHOULD PLAY")
        # print(i )
        # print(I_played, I_played_previous)
        # print()
        if I_played != I_played_previous:
            S_played += I_played
            profit += add_profit(T[i], I_played, 1, R,  P, S)
        else:   
            if i + K < N:
                To_play_future = determine_R_P_S(T[i + K])
                if To_play_future != I_played_previous:
                    S_played += mapped_dict[3 - reverse_mapped_dict[To_play_future] - reverse_mapped_dict[I_played_previous]]
                else:
                    S_played += T[i]
                    
            else:
                S_played += T[i]
                

    # print(S_played)
    return profit



print(total_profit(T, R, P, S, K, N))



