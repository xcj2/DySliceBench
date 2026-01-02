## coding: UTF-8
N = int(input())
#N = 4
s = "abcdedcba" #よく更新する文字列
answer = ['a'] #回答となる文字列のリストを入れる場所 　初期値はN=1の['a']を入れておきます。

#文字列の中から辞書順で最大のアルファベットを検索するコード
def search_max(s):
    max = 'Z' #大文字の方が文字コードが若い。aよりも若いものを最大値として押さえておく
    for i in range(len(s)):
        if(s[i] > max):
            max = s[i]
    return max

#アルファベットに対して次の文字を返すコードではなく
#アルファベットに対して次の文字までのリストを返す
def next(p):
    list_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    alpha_index = -100
    for i in range(len(list_alpha)):
        if(p == list_alpha[i]):
            alpha_index = i
    #return list_alpha[alpha_index + 1]
    return list_alpha[:alpha_index+2]



#n文字の文字列（回答）が入ったリストを受け取ったら、その各文字列に対して1文字付け足して返す関数
def one_plus(l): 
    ret_list = [] #最終的に返すリスト
    for i in range(len(l)): #listの各要素に対して
        max_alpha = search_max(l[i]) #まずは要素の辞書順最大アルファベットを探す
        next_list = next(max_alpha) #次に入るアルファベット候補の羅列
        #print(next_list)
        for j in range(len(next_list)):
            ret_list.append(l[i] + next_list[j])
    return ret_list

for i in range(N-1):
    answer = one_plus(answer) #answerリストに1文字ずつ付け足して返す
#print(answer)

for i in range(len(answer)):
    print(answer[i]) #1行ずつ出力

'''
def sum(n):
    if n < 1:
        return n
    return n + sum(n-1)

si = sum(100)
print("1から100の合計は", si, "です")
'''
#print(search_max(s))
#print(next('a'))
#print(next('c'))
#print(one_plus(["aa", 'ab']))