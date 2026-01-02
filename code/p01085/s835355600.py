def get_input():
    data_list = input().split()
    for i in range(len(data_list)):
        data_list[i] = int(data_list[i])
    return data_list

def get_score_list(student_num):
    score_list = [None] * student_num
    for i in range(student_num):
        score_data = int(input())
        score_list[i] = score_data
    score_list = sorted(score_list, reverse=True)
    return score_list

def decide_success_student_num(score_list, min_num, max_num):
    max_diff = -float('inf')
    for i in range(min_num - 1, max_num):
        tmp_num = score_list[i] - score_list[i+1]
        if tmp_num >= max_diff:
            max_diff = tmp_num
            success_student_num = i + 1
    return success_student_num


if __name__ == "__main__":
    while True:
        student_num, min_num, max_num = get_input()
        if student_num == 0:
            break
        score_list = get_score_list(student_num)
        success_student_num = decide_success_student_num(score_list, min_num, max_num)
        print(success_student_num)

