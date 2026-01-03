# coding: utf-8
"""this is python work script"""

CHECK_WORDS = ['dream', 'dreamer', 'erase', 'eraser']

def check_word(word, check_word_list):
    find_word = False

    # print(word, check_word_list)
    for i, cw in enumerate(check_word_list):
        find_result = word.find(cw)
        # print(i, cw, find_result)

    # # remove check word if not find it in string
    # if find_result == -1:
    #     check_word_list.remove(cw)

    #  remove word if find it in string head
        if find_result == 0:
            word_length = len(cw)
            word = word[word_length:]
            find_word = True
        # print(word, check_word_list)

    return find_word, word

def solver(word, check_word_list):
    """solve this problem"""
    wip = True
    while wip:
        wip, word = check_word(word, check_word_list)

    answer = 'NO'
    if len(word) == 0:
        answer = 'YES'
    return answer

def reverse_string_list(string_list):
    answer_list = []
    for word in string_list:
        answer_list.append(word[::-1])

    return answer_list

def main():
    """main function"""
    word = input().rstrip()[::-1]
    word_list = reverse_string_list(CHECK_WORDS)
    answer = solver(word=word, check_word_list=word_list)
    print(answer)

if __name__ == '__main__':
    main()
