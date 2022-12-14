
class Node:
    def __init__(self):
        self.index = None
        self.info = None
        self.parent = None
        self.right_sibling = None

class ParserOutput:
    def __init__(self):
        self.working_stack = []
