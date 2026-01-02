from collections import defaultdict

def get_alphadic(string):
    dic = defaultdict(lambda: 0)
    for c in string:
        dic[c] += 1
    return dic


def get_newstring(dic):
    string = ''
    for item in sorted(dic.items(), key=lambda x: x[0]):
        string += item[0]*item[1]
    return string


def main():
    s = input()
    t = input()
    s_dic = get_alphadic(s)
    t_dic = get_alphadic(t)
    s_ = get_newstring(s_dic)
    t_ = get_newstring(t_dic)[::-1]

    if s_ < t_:
        print('Yes')
    else:
        print('No')



if __name__ == '__main__':
    main()