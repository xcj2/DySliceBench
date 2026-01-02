# D - Lamp

#import numpy as np

H, W = map(int, input().split())
#S = np.array([list(input()) for _ in range(H)])
S = [list(input()) for _ in range(H)]

def trans(M):
    output_list = []
    for col in range(len(M[0])):
        tmp = []
        for row in range(len(M)):
            tmp.append(M[row][col])
        output_list.append(tmp)
    return output_list
            
def n_row_lighten(l):
    output_list = []
    left_block_idx = -1
    
    for idx in range(len(l)):
        if l[idx] == "#":
            right_block_idx = idx
            for _ in range(right_block_idx - left_block_idx - 1):
                output_list.append(right_block_idx - left_block_idx - 1)
            output_list.append(0)
            left_block_idx = right_block_idx
            
        if idx == len(l) - 1 and l[idx] == ".":
            right_block_idx = idx + 1
            for _ in range(right_block_idx - left_block_idx - 1):
                output_list.append(right_block_idx - left_block_idx - 1)
        
    return output_list        

def n_matrix_lighten(S):
    output_list = []
    for row in range(len(S)):
        output_list.append(n_row_lighten(S[row]))
    return output_list

#n_lighten = n_matrix_lighten(S) + np.array(n_matrix_lighten(S.T)).T - 1
ans = 0
tmp1 = n_matrix_lighten(S)
tmp2 = trans(n_matrix_lighten(trans(S)))

for row in range(H):
    for col in range(W):
        ans = max(ans, tmp1[row][col] + tmp2[row][col] - 1)

print(ans)