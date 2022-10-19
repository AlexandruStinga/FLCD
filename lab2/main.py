# 1a

class HashTable:
    def __init__(self):
        self.hash_table = [[] for i in range(5)]

    def hash(self, key):
        return key % len(self.hash_table)

    def insert(self, value):
        hash_key = self.hash(ord(value))
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
        hash_key = self.hash(ord(value))
        nested_list = self.hash_table[hash_key]
        for i, elem in enumerate(nested_list):
            if elem == value:
                return hash_key, i
        return -1


st = HashTable()
st.insert('a')
st.insert('b')
st.insert('5')
print(st.insert('5'))
print(st.search_position('a'))
print(st.hash_table)
