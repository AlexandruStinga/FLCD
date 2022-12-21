from Node import Node


class ParserOutput:
    def __init__(self, parser):
        self.parser = parser
        self.tree = []
        self.index = 0

    def build_tree(self):
        self.tree.append(Node(0, self.parser.working_stack[0][0], -1, -1))
        for i in range(1, len(self.parser.working_stack)):
            if self.parser.working_stack[i][0].isupper():
                self.tree.append(Node(i, self.parser.working_stack[i][0], self.index, -1))
                self.index = i
            else:
                self.tree.append(Node(i, self.parser.working_stack[i][0], self.index, -1))
        self.find_left_sibling()

    def find_right_sibling(self):
        for i in range(0, len(self.tree)):
            for j in range(i + 1, len(self.tree)):
                if self.tree[i].parent == self.tree[j].parent:
                    self.tree[i].right_sibling = self.tree[j].index
                    break

    def find_left_sibling(self):
        for i in range(0, len(self.tree)):
            for j in range(i - 1, -1, -1):
                if self.tree[i].parent == self.tree[j].parent:
                    self.tree[i].right_sibling = self.tree[j].index
                    break


    def print_parsing_tree(self):
        table = []
        for i in range(0, len(self.tree)):
            table.append([self.tree[i].index, self.tree[i].info, self.tree[i].parent, self.tree[i].right_sibling])
        # print the table
        print("index info parent right")
        for i in range(0, len(table)):
            message = str(table[i][0]) + "  " + str(table[i][1]) + "  " + str(table[i][2]) + "  " + str(table[i][3])
            print(message)


