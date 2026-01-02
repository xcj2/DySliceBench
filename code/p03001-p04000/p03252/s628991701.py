def listToString(_list, split=""):
    maped_list = map(str, _list)  # mapで要素すべてを文字列に
    mojiretu = split.join(maped_list)
    return mojiretu


def stringToList(_string, split=" "):
    str_list = []
    temp = ''
    for x in _string:
        if x == split:  # 区切り文字
            str_list.append(temp)
            temp = ''
        else:
            temp += x
    if temp != '':  # 最後に残った文字列を末尾要素としてリストに追加
        str_list.append(temp)
    return str_list


def asciiToindex(alphabet):
    return ord(alphabet) - ord("a")


s = input()
t = input()
# 　初期状態から、各操後の変換後テーブル
alpha = [i for i in range(asciiToindex("z") + 1)]
visited = [0 for i in range(asciiToindex("z") + 1)]

for i in range(len(s)):
    if alpha[asciiToindex(s[i])] != asciiToindex(t[i]):
        if visited[alpha[asciiToindex(s[i])]] == 1 or\
                        visited[asciiToindex(t[i])] == 1:
            print("No")
            exit()
        else:
            # tmp = 現在のs[i]の値
            tmp = alpha[asciiToindex(s[i])]
            for j in range(len(alpha)):
                if alpha[j] == tmp:
                    alpha[j] = asciiToindex(t[i])
                elif alpha[j] == asciiToindex(t[i]):
                    alpha[j] = tmp
    visited[asciiToindex(t[i])] = 1
    # print(listToString([chr(i+ord("a")) for i in alpha], "_"))
    # print("visited:{}".format(visited))
    # print(alpha)
print("Yes")
