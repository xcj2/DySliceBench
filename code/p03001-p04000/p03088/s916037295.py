N = int(input())

def checkAGC(string):
    str0 = string[0] +string[1] +string[2] +string[3]
    str1 = string[1] +string[0] +string[2] +string[3]
    str2 = string[0] +string[2] +string[1] +string[3]
    str3 = string[0] +string[1] +string[3] +string[2]
    
    if "AGC" in str0 or "AGC" in str1 or "AGC" in str2 or "AGC" in str3:
        return True
    else:
        return False

def checkAGC3(string):
    str0 = string[0] +string[1] +string[2]
    str1 = string[1] +string[0] +string[2] 
    str2 = string[0] +string[2] +string[1] 
    
    if "AGC" in str0 or "AGC" in str1 or "AGC" in str2 :
        return True
    else:
        return False
      

import itertools

words = list(itertools.product("ATGC", "ATGC","ATGC"))

#3文字のインデックスを返す
nucleotide_dict =  dict(list( (words[i],i) for i in range(len(words))))

import numpy as np
# 重み行列を求める
W = np.zeros((len(words),len(words)))
for word_prev in words:
    for word_next in words:
        if word_prev[1:] == word_next[:-1] and not checkAGC(word_prev[:-1]+word_next[1:]):
            #print(nucleotide_dict[word_next],nucleotide_dict[word_prev],word_prev[:-1]+word_next[1:] )
            W[nucleotide_dict[word_next],nucleotide_dict[word_prev]] = 1
b = np.array([0 if checkAGC3(i) else 1 for i in words])

def mod(num):
    return num % int(pow(10,9)+7)
  
res = b
for i in range(N-3):
    res = np.vectorize(lambda x: mod(x))(np.dot(W,res))
print(int(mod(np.sum(res))))
