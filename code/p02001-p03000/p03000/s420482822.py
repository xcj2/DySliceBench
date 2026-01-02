def input_from_console():
    n, x = map(int, input().split())
    l_list = list(map(int, input().split()))
    return n, x, l_list


def solve(n, x, l_list):
    result = 0
    position = 0
    for i in range(n):
        if position > x:
            return result
        result +=1
        position += l_list[i]
    if position > x:
        return result 
    else:
        return result + 1



def main():
    n, x, l_list = input_from_console()
    print(solve(n, x, l_list))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()
