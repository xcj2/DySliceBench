import sys


def main():

    # Get Args
    args = _input_args()  # get arguments as an array from console/script parameters.

    # Call main Logic
    result = _main(args)

    # Output a result in a correct way.
    _output_result(result)


def _main(args):
    """Write Main Logic here for the contest.

    :param args: arguments
    :type args: list
    :return: result
    :rtype: depends on your logic.
    """
    # Extract arguments.
    N = int(args[0])
    K = int(args[1])

    # Write main logic here.
    now = 1
    for i in range(N):
        if now < K:
            now = now * 2
        else:
            now = now + K

    # Return something.
    return now


def _input_args():
    # Comment-out appropriate pattern depends on subject.

    # arguments = sys.argv[1:]  # ptn1: get args from script parameters.
    # arguments = _input().split()  # ptn2: get args from 1 line console prompt with space separated.

    # for multi-line console input, use this.
    arguments = _get_args_from_multiple_lines(end_of_lines_char=[''], limit=2)

    # Cast elements If you need.
    # arguments = list(map(int, arguments))  # cast elements to int for example.

    return arguments  # This will be array.


def _input():
    # If Subject requires interactive input, use this and patch mock in unittest.
    return input()  # Change if necessary.


def _get_args_from_multiple_lines(end_of_lines_char=[''], limit=2):
    """Get arguments from multiple lines standard input.

    :param end_of_lines_char: Strings that indicate the end of lines.
    :type end_of_lines_char: list of str
    :param limit: If a number of the input line are certain, you can use this param to close prompt immediately.
    :type limit: int
    :return: args
    :rtype list of str
    """
    args = []
    for i in range(limit):
        try:
            arg = _input()
            if arg in end_of_lines_char:
                break
            args.append(arg)
        except EOFError:  # Supports EOF Style. (Very Rare case)
            break
    return args


def _output_result(result):
    # Comment-out appropriate output pattern depends on subject.

    # sys.stdout.write(result)  # No Line Feed, and an result must be string (not useful). for single value output.
    print(result)  # The result will cast to strings. Line feed will be appended to the end. for single value output.
    # print(result, end='')  # Same as above except Line Feed won't be appended. for single value output.
    # print(','.join(map(str, result)))  # Print array elements as comma separated strings. for multi-value.
    # print('ans={}'.format(str(result)))  # Same as above, but more versatile.


if __name__ == '__main__':
    main()
