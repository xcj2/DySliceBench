import sys
from copy import deepcopy
# coding: utf-8


class Node(object):

    def __init__(self, value):
        self.value = value
        self.visited = False
        self.adjacencies = []

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.value)

    def add_adjaency(self, node):
        if isinstance(node, Node):
            self.adjacencies.append(node)
        else:
            raise TypeError('Type "Node" expected, but received {0}'.format(type(node)))

    def remove_adjacency(self, node):
        self.adjacencies.remove(node)

    def is_visited(self):
        return self.visited

    def mark_as_visited(self):
        self.visited = True

    def clear_history(self):
        self.visited = False


class Graph(object):

    def __init__(self):
        self.nodes = []
        self.root = None
        self.search_result = None  # Not Thread Safe Now.

    def __str__(self):
        return self.nodes

    def mark_as_root(self, node):
        self.root = node

    def add_node(self, node):
        if isinstance(node, Node):
            self.nodes.append(node)
            if self.root is None:
                self.mark_as_root(node)
        else:
            raise TypeError('Type "Node" expected, but received {0}'.format(type(node)))

    @staticmethod
    def add_uni_link(from_node, to_node):  # unidirectional
        from_node.add_adjaency(to_node)

    @staticmethod
    def remove_uni_link(from_node, to_node):  # unidirectional
        from_node.remove_adjacency(to_node)

    @staticmethod
    def add_bi_link(node1, node2):  # bidirectional
        node1.add_adjaency(node2)
        node2.add_adjaency(node1)

    @staticmethod
    def remove_bi_link(node1, node2):  # bidirectional
        node1.remove_adjacency(node2)
        node2.remove_adjacency(node1)

    def clear_history(self):
        for node in self.nodes:
            node.clear_history()

    def dfs(self, value, start_node=None):
        """Depth First Search
        :returns reference of node where the value matches attribute value.
        """
        self.search_result = None
        self.clear_history()

        if start_node is None:
            start_node = self.root

        self._dfs(start_node, value)

    def _dfs(self, start_node, value):
        self._visit(node=start_node, search_value=value)

        for adjacency in start_node.adjacencies:
            if not adjacency.is_visited():
                self._dfs(start_node=adjacency, value=value)
        return

    def _visit(self, node, search_value):
        node.mark_as_visited()
        if node.value == search_value:
            self.search_result = node
        else:
            return


def main():

    # Get Args
    a, b, N, M = _input_args()  # get arguments as an array from console/script parameters.

    # Call main Logic
    result = _main(a, b, N, M)

    # Output a result in a correct way.
    _output_result(result)


def _main(a, b, N, M):
    """Write Main Logic here for the contest.

    :param args: arguments
    :type args: list
    :return: result
    :rtype: depends on your logic.
    """

    bridges = 0  # counter
    offset = -1  # between subject

    for i in range(M):
        # Initialize Graph
        graph = Graph()

        # Add nodes
        for n in range(N):
            graph.add_node(Node(value=n + 1))

        # Add lines, but drops one of them
        a_temp = deepcopy(a)
        b_temp = deepcopy(b)

        del a_temp[i]
        del b_temp[i]

        # Add lines
        for n1_index, n2_index in zip(a_temp, b_temp):
            graph.add_bi_link(graph.nodes[n1_index + offset], graph.nodes[n2_index + offset])

        # check if all node can be found by dfs
        for nd in range(N):
            graph.dfs(value=nd+1)
            if graph.search_result is None:
                bridges += 1
                break

    return bridges


def _input_args():

    arguments = _get_args_from_multiple_lines(end_of_lines_char=[''], limit=10000000)

    a = []
    b = []
    N, M = map(int, arguments[0].split())
    pairs = arguments[1:]

    for i in range(0, len(pairs)):
        ai, bi = map(int, pairs[i].split())
        a.append(ai)
        b.append(bi)

    return a, b, N, M


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
    print('{}'.format(str(result)))  # Same as above, but more versatile.


if __name__ == '__main__':
    main()
