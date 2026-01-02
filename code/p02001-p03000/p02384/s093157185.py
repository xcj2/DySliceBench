def initialize(faces_int: list) -> list:
    list_sn = [faces_int[5], faces_int[4], faces_int[0], faces_int[1]]  # 6,5,1,2
    list_we = [faces_int[5], faces_int[2], faces_int[0], faces_int[3]]  # 6,3,1,4
    return [list_sn, list_we]


def roll_positive(list_a: list, list_b: list) -> list:
    list_a = list_a[1:] + list_a[0:1]  # Roll one unit in the positive direction.
    list_b[0] = list_a[0]  # Change the bottom face.
    list_b[2] = list_a[2]  # Change the top face.
    return [list_a, list_b]


def roll_negative(list_a: list, list_b: list) -> list:
    list_a = list_a[3:] + list_a[0:3]
    list_b[0] = list_a[0]  # Change the bottom face.
    list_b[2] = list_a[2]  # Change the top face.
    return [list_a, list_b]


if __name__ == "__main__":
    faces_int = list(map(lambda x: int(x), input().split()))  # 1,2,3,4,5,6
    question_num = int(input())

    for _ in range(question_num):
        SN_direction, WE_direction = initialize(faces_int)
        q_top, q_front = map(lambda x: int(x), input().split())
        for command in "NNNNWNNNWNNNENNNENNNWNNN":  # Check all patterns.
            if ("N" == command):
                SN_direction, WE_direction = roll_positive(SN_direction, WE_direction)
            elif ("S" == command):
                SN_direction, WE_direction = roll_negative(SN_direction, WE_direction)
            elif ("E" == command):
                WE_direction, SN_direction = roll_positive(WE_direction, SN_direction)
            else:
                WE_direction, SN_direction = roll_negative(WE_direction, SN_direction)
            if SN_direction[2] == q_top and SN_direction[3] == q_front:
                print(f"{WE_direction[1]}")  # Print the right side face.
                break

