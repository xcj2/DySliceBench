N,A,B,C,D = map(int, input().split())
A -= 1
B -= 1
C -= 1
D -= 1

S = list(input())

iwa2 = []
cnt = 0
for i in range(len(S)-1):
    if S[i] == S[i+1] == "#":
#         iwa2.append(1)
        cnt += 1
#     else:
#         iwa2.append(0)
    iwa2.append(cnt)
    
#長さ揃える
iwa2.append(cnt)        
        
def iwa2_check(s,g):
    if iwa2[s] < iwa2[g]:
        return True
    return False

# aki3は複数あったら、そのどれかに二人でたどり着ければ良い
aki3 = [0]
cnt = 0
for i in range(1,len(S)-1):
    if S[i-1] == S[i] == S[i+1] == ".":
        cnt += 1
    aki3.append(cnt)
aki3.append(cnt)

def aki3_check(B,CORD):
    # AさんがBさんと出会える（iwa2ない）
#     if not iwa2(A,B):
#         return False
    # Bさんがaki3にたどり着ける（最寄りの2つを見るだけで良い）
    # oBoのような状態でもOKなので-1
    if aki3[B-1] < aki3[CORD]:
        return True
    return False

# 順序が入れ替わらないとき
def solve():
    if iwa2_check(A,C) or iwa2_check(B,D):
#         print("1")
        return False
    if C<D:
#         print("2")
        return True
    else:
        if aki3_check(B, D):
#             print("3")
            return True
        else:
#             print("4")
            return False

if solve():
    print("Yes")
else:
    print("No")