import sys

# 標準入力からデータを読み込む
def read_data():
    n, m = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    matrix = []
    for _ in range(n):
        matrix.append([int(num) for num in sys.stdin.readline().strip().split(' ')])

    vector = []
    for _ in range(m):
        vector.append(int(sys.stdin.readline().strip()))

    return matrix, vector

# 行列xベクトルの計算
def multiple(matrix, vector):
    n = len(matrix)
    m = len(vector)
    ans = []

    for i in range(n):
        sum = 0
        for j in range(m):
            sum += (matrix[i][j] * vector[j])

        ans.append(sum)

    return ans

# メイン関数
def main():
    matrix, vector = read_data()
    ans = multiple(matrix, vector)
    for i in ans:
        print(i)
        
if __name__ == '__main__':
    main()
