import numpy as np
N, M = map(int, input().split())
 
Adj_matrix = np.zeros((N, N))
for _ in range(M):
    a, b = map(int, input().split())
    Adj_matrix[a - 1, b - 1] += 1
    Adj_matrix[b - 1, a - 1] += 1
    
def initialize():
    explored_list = np.zeros((N, 1))
    return explored_list
  
def is_move(vertex, explored_list, Adj_martrix):
    for i in range(len(explored_list)):
        if explored_list[i] == 0 and Adj_martrix[vertex - 1, i] == 1:
            return True
    return False
  
import copy
 
g_count = 0
 
def graph_exp(vertex, explored_list, Adj_matrix):
    global g_count
    
    explored_list[vertex - 1] += 1
    
    # Recursive End
    if not is_move(vertex, explored_list, Adj_matrix):
        g_count += all(explored_list)
        return 0
    
    # Recursive Call
    for i in range(len(explored_list)):
        if explored_list[i] == 0 and Adj_matrix[vertex - 1, i] == 1:
            graph_exp(i + 1, copy.copy(explored_list), Adj_matrix)
    
explored_list = initialize()
 
graph_exp(1, explored_list, Adj_matrix)
 
print(g_count)