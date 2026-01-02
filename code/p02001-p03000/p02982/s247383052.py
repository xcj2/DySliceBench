import math

def input_from_console():
    n, d = map(int, input().split())
    x_matrix = []
    for i in range(n):
        x = map(int, input().split())
        x_matrix.append(list(x))
    return n, d, x_matrix


def solve(n, d, x_matrix):
    result = 0
    for i in range(n):
        for j in range(n - i -1):
            distance = math.sqrt(sum([(p1 - p2) ** 2 for p1, p2 in zip(x_matrix[i], x_matrix[j + i + 1])]))
            if distance == int(distance):
                result += 1
    return result


def main():
    n, d, x_matrix = input_from_console()
    print(solve(n, d, x_matrix))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()
