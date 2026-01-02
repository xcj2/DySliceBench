BEF_STR= "A"
AFT_STR = "Un"

def get_data():
    data = input()
    return data

def make_data_list(num):
    data_list = [None] * num
    for i in range(num):
        data_list[i] = get_data()
    return data_list

#A-Unでワンセットとなるかを確認する関数を作りたい
def check_STR1_to_STR2_correspondence(data_list):
    count = 0
    if len(data_list) % 2 != 0 or data_list[0] == AFT_STR:
        return False
    for s in data_list:
        if s == BEF_STR:
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
    if count != 0:
        return False
    return True

if __name__ == "__main__":
    speak_sum = int(get_data())
    record_list = make_data_list(speak_sum)
    is_A_Un = check_STR1_to_STR2_correspondence(record_list)
    if is_A_Un is False:
        print("NO")
    else:
        print("YES")


