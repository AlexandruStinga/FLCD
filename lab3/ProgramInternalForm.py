class ProgramInternalForm:
    def __init__(self):
        self.list = []

    def insert(self, key, value):
        self.list.append((key, value))

    def __str__(self):
        result = ""
        for pair in self.list:
            result += pair[0] + "->" + str(pair[1]) + "\n"
        return result