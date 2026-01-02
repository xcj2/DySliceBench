import sys
data_list = []
for line in sys.stdin:
	data_list.append(line.split())

class Node():
    def __init__(self, name, transaction_list = None):
        self.transaction_list = transaction_list or []

    def add_node(self, node):
        self.transaction_list.append(node)

def convert_adjencentList_to_adjencentMatrix(adjencentList):
    adjencent_matrix = [[0 for i in range(len(adjencentList))] for j in range(len(adjencentList))]
    count = 0
    for targetList in adjencentList:
        targetList.transaction_list.sort()
        for target_index in targetList.transaction_list :
            adjencent_matrix[count][int(target_index) - 1] = 1
        count = count + 1

    for i in adjencent_matrix:
        print(*i)

if __name__ == "__main__":
        node_data_list = []

        for node_data in data_list[1:]:
            node = Node(node_data[1])
            for transaction_node in node_data[2:]:
                node.add_node(transaction_node)

            node_data_list.append(node)

        convert_adjencentList_to_adjencentMatrix(node_data_list)

