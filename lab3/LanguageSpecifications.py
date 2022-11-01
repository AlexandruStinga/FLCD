separators = []
operators = []
reserved_words = []

def read_token():
    with open('Token.in', 'r') as token:
        for i in range(13):
            operators.append(token.readline().strip())
        for i in range(10):
            separator = token.readline().strip()
            if separator == 'space':
                separator = ' '
            separators.append(separator)
        for i in range(11):
            reserved_words.append(token.readline().strip())

