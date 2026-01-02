#!usr/bin/env python3

import sys


def init_matrix_vector():
    m, n = [int(col_row) for col_row in sys.stdin.readline().split()]
    matrix = [[0 for col in range(n)] for row in range(m)]
    vector = [0 for row in range(n)]

    for row in range(m):
        lst = [int(element) for element in sys.stdin.readline().split()]
        for col in range(n):
            matrix[row][col] += lst[col]

    for row in range(n):
        lst = [int(element) for element in sys.stdin.readline().split()]
        vector[row] += lst[0]

    return matrix, vector


def print_matrix_vector_multiplication_result(matrix, vector):
    for row in range(len(matrix)):
        sum_of_row = 0
        for col in range(len(vector)):
            sum_of_row += matrix[row][col] * vector[col]
        print(sum_of_row)


def main():
    matrix, vector = init_matrix_vector()
    print_matrix_vector_multiplication_result(matrix, vector)


if __name__ == '__main__':
    main()