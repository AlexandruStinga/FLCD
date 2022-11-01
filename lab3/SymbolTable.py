# 1a

class SymbolTable:
    def __init__(self):
        self.hash_table = [[] for i in range(5)]

    def hash(self, key):
        return key % len(self.hash_table)

    def insert(self, value):
        if len(value) > 0:
            key = ord(value[0])
        else:
            key = value

        hash_key = self.hash(key)
        nested_list = self.hash_table[hash_key]
        value_exists = False
        pos = -1
        for i, elem in enumerate(nested_list):
            if elem == value:
                value_exists = True
                pos = i
        if value_exists:
            return pos, hash_key
        else:
            nested_list.append(value)

    def search_position(self, value):
        if len(value) > 0:
            key = ord(value[0])
        else:
            key = value

        hash_key = self.hash(key)
        nested_list = self.hash_table[hash_key]
        for i, elem in enumerate(nested_list):
            if elem == value:
                return hash_key, i
        return -1

    def __str__(self) -> str:
        result = ""
        for i in range(len(self.hash_table)):
            result = result + str(i) + "->" + str(self.hash_table[i]) + "\n"
        return result