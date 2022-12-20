from tabulate import tabulate


class Node:
    def __init__(self, index, info, parent, right_sibling):
        self.index = index
        self.info = info
        self.parent = parent
        self.right_sibling = right_sibling


class ParserOutput:
    def __init__(self, working_stack, productions):
        self.working_stack = working_stack
        self.productions = productions
        self.tree = []
        self.working_stack_index = 0
        self.start_tree()

    def start_tree(self):
        info, productionIndex = self.working_stack[0]
        root = Node(0, info, None, None)
        self.tree.append(root)
        self.build_tree_recursive(0)

    def build_tree_recursive(self, parent_index):
        prod_length = len(self.productions[self.working_stack[self.working_stack_index][0]]
                          [self.working_stack[self.working_stack_index][1]])
        
        for i in range(prod_length):
            self.working_stack_index += 1
            current = self.working_stack[self.working_stack_index]
            if type(current) is tuple:
                info = current[0]
                node = Node(self.working_stack_index, info, parent_index, None)
                self.tree.append(node)
                self.build_tree_recursive(self.working_stack_index)
            else:
                node = Node(self.working_stack_index, current, parent_index, None)
                self.tree.append(node)

    def find_right_sibling(self, node):
        # for i in range(node.index + 1, len(self.tree)):
        for i in range(0, node.index):
            if self.tree[i].parent == node.parent:
                return self.tree[i].index

    def __str__(self):
        table = []
        headers = ["index", "info", "parent", "right sibling"]
        for node in self.tree:
            line = (node.index, node.info, node.parent, self.find_right_sibling(node))
            table.append(line)
        return tabulate(table, headers, "grid")
