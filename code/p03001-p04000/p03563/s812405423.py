import sys


def main():

    # Get Args
    args = _input_args()  # get arguments as an array from console/script parameters.

    # Call main Logic
    result = _main(args)

    # Export a result in a correct way.
    _export_result(result)


def _main(args):
    """Write Main Logic here for the contest.

    :param args: arguments
    :type args: list
    :return: result
    :rtype: depends on your logic.
    """
    # Extract arguments.
    R = int(args[0])
    G = int(args[1])

    # Write main logic here.
    X = (2 * G) - R

    # Return something.
    return X


def _input_args():
    # Comment-out appropriate pattern depends on subject.

    # arguments = sys.argv[1:]  # ptn1: get args from script parameters.
    # arguments = _input().split()  # ptn2: get args from 1 line console prompt with space separated.

    # for multi-line console input, use this.
    arguments = _get_args_from_multiple_lines(end_of_lines_char=[''])

    # Cast elements If you need.
    # arguments = list(map(int, arguments))  # cast elements to int for example.

    return arguments  # This will be array.


def _input():
    # If Subject requires interactive input, use this and patch mock in unittest.
    return input()  # Change if necessary.


def _get_args_from_multiple_lines(end_of_lines_char=['']):
    """Get arguments from multiple lines standard input.

    :param end_of_lines_char: Strings that indicate the end of lines.
    :type end_of_lines_char: list of str
    :return: args
    :rtype list of str
    """
    args = []
    while True:
        try:
            arg = _input()
            if arg in end_of_lines_char:
                break
            args.append(arg)
        except EOFError:  # Supports EOF Style. (Very Rare case)
            break
    return args


def _export_result(result):
    # Comment-out appropriate output pattern depends on subject.

    # sys.stdout.write(result)  # No Line Feed, and an result must be string (not useful). for single value output.
    # print(result)  # The result will cast to strings. Line feed will be appended to the end. for single value output.
    # print(result, end='')  # Same as above except Line Feed won't be appended. for single value output.
    # print(','.join(map(str, result)))  # Print array elements as comma separated strings. for multi-value.
    print('{}'.format(str(result)))  # Same as above, but more versatile.


if __name__ == '__main__':
    main()
