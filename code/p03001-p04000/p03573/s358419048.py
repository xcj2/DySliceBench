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
    hash = HashMap()

    for value in args:
        hash.add(value)

    # Return something.
    return hash.find_unique()


class HashMap(object):
    def __init__(self):
        self.map = {}

    def add(self, value):
        if self.map.get(value) is None:
            self.map[value] = [value]
        else:
            self.map[value].append(value)

    def find_unique(self):
        for value, array in self.map.items():
            if len(array) == 1:
                return array[0]


def _input_args():

    arguments = _input().split()  # ptn2: get args from 1 line console prompt with space separated.

    return arguments  # This will be array.


def _input():
    # If Subject requires interactive input, use this and patch mock in unittest.
    return input()  # Change if necessary.


def _output_result(result):

    print('{}'.format(str(result)))  # Same as above, but more versatile.


if __name__ == '__main__':
    main()
