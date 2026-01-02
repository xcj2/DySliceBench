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
    lines = args
    H, W = int(lines[0].split()[0]), int(lines[0].split()[1])
    field_map = get_field_map(lines[1:])
    result_map = [[0 for col in range(W)] for row in range(H)]

    for h in range(H):
        for w in range(W):
            result_map[h][w] = sweep_perimeters(h, w, field_map, H, W)

    result_lines = convert_map_to_lines(result_map)

    # Return something.
    return result_lines


def sweep_perimeters(h, w, field_map, H, W):
    found_mine = 0

    if field_map[h][w] == '#':
        return '#'

    for i in range(h-1, h+1+1):
        for j in range(w-1, w+1+1):
            if (0 <= i < H) and (0 <= j < W):
                target = field_map[i][j]
                if target == '#':
                    found_mine += 1

    return found_mine


def get_field_map(lines):
    field_maps = []
    for line in lines:
        elements = list(line)
        field_maps.append(elements)
    return field_maps


def convert_map_to_lines(result_map):
    result_lines = []
    for row_array in result_map:
        stringfied_row = ''
        for value in row_array:
            value = str(value)
            stringfied_row += value
        result_lines.append(stringfied_row)

    return result_lines

def _input_args():
    # Comment-out appropriate pattern depends on subject.

    # arguments = sys.argv[1:]  # ptn1: get args from script parameters.
    # arguments = _input().split()  # ptn2: get args from 1 line console prompt with space separated.

    # for multi-line console input, use this.
    arguments = _get_args_from_multiple_lines(end_of_lines_char=[''], limit=10000000)

    # Cast elements If you need.
    # arguments = list(map(int, arguments))  # cast elements to int for example.

    return arguments  # This will be array.


def _input():
    # If Subject requires interactive input, use this and patch mock in unittest.
    return input()  # Change if necessary.


def _get_args_from_multiple_lines(end_of_lines_char=[''], limit=10000000):
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

    for line in result:
        print('{}'.format(str(line)))  # Same as above, but more versatile.


if __name__ == '__main__':
    main()
