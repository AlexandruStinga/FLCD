import re

from LanguageSpecifications import operators, separators, reserved_words, read_token


class Scanner:
    def is_operator(self, char):
        for operator in operators:
            if char in operator and char != '!':
                return True
        return False

    def get_string_token(self, line, index):
        token = ''
        quoteCount = 0

        while index < len(line) and quoteCount < 2:
            if line[index] == '\'' and line[index - 1] != '\\':
                quoteCount += 1
            token += line[index]
            index += 1

        return token, index

    def tokenize(self, line):
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.is_operator(line[index]):
                if (index + 1) < len(line) and self.is_operator(line[index + 1]):
                    tokens.append(line[index] + line[index + 1])
                    index += 2
                    token = ''
                else:
                    tokens.append(line[index])
                    index += 1
                    token = ''
            elif line[index] == '\'':
                if token:
                    tokens.append(token)
                token, index = self.get_string_token(line, index)
                tokens.append(token)
                token = ''
            elif line[index] in separators:
                if token:
                    tokens.append(token)
                token = line[index]
                tokens.append(token)
                index += 1
                token = ''
            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens

    def is_identifier(self, token):
        return re.match(r'^[_a-zA-Z][_a-zA-Z0-9]*$', token)

    def is_constant(self, token):
        return re.match(r'^-?(([1-9][0-9]*)|(0))(?:\.[0-9]+)?$', token)
