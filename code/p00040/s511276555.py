E = 10**-10
def decy(a):
    return [ord(i)-97 for i in a]
def encr(a):
    return "".join([chr(i+97) for i in a])
def deaffin(j,a,b):
    cont_ = 1
    for i in range(100):
        if cont_ == 0:
            break
        elif ((j-b+26*i)/a)//1 == (j-b+26*i)/a:
            cont_ = 0
            return int((j-b+26*i)/a)%26
n = int(input())
for _ in range(n):
    sen = input()
    words = sen.split()
    wordsl = [len(i) for i in words]
    wordsn = [decy(i) for i in words]
    fourn = []
    for i in range(len(wordsl)):
        if wordsl[i] == 4:
            fourn.append(wordsn[i])
    a_ = 0
    b_ = 0
    cont = 1
    for a in [1,3,5,7,9,11,15,17,19,21,23,25]:
        if cont != 0:
            for b in range(26):
                if cont != 0:
                    for i in fourn:
                        deco = [chr(deaffin(j,a,b)+97) for j in i]
                        if deco == ["t","h","i","s"] or deco == ["t","h","a","t"]:
                            a_ = a
                            b_ = b
                            cont = 0
                            break
    dec_wordsn = [[deaffin(j,a_,b_) for j in i] for i in wordsn]
    dec_words = [encr(i) for i in dec_wordsn]
    print(" ".join(dec_words))
