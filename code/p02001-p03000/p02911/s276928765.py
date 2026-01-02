import collections
def main():
    li = list(map(int,input().split()))
    respondents = [int(input()) for i in range(li[2])]
    number_of_respondes = respondes_number_of_participants(respondents)
    check_surviver(number_of_respondes,li[0],li[1],li[2])


def respondes_number_of_participants(respondents):
    return collections.Counter(respondents)


def check_surviver(number_of_respondes,number_of_participants,gived_points,number_of_questions):
    for i in range(number_of_participants):
        if number_of_respondes[i+1]:
            if gived_points - number_of_questions + number_of_respondes[i+1] > 0:
                print("Yes")
            else:
                print("No")
        else:
            if gived_points - number_of_questions > 0:
                print("Yes")
            else:
                print("No")

main()
