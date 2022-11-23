from Grammar import Grammar
from UI import UI


def parse_line(line):
    return [value.strip() for value in line.strip().split('=')[1].strip().split(',')]

def read_from_file():
    with open("g1.txt") as f:
        N = parse_line(f.readline())
        E = parse_line(f.readline())
        S = parse_line(f.readline())
        P = []
        for line in f:
            P.append(parse_productions_in_dictionary(line))
    return Grammar(N, E, P, S)

def parse_productions_in_dictionary(production_line):
    result = {}
    for rule in production_line:
        lhs, rhs = rule.split('->')
        lhs = lhs.strip()
        rhs = [value.strip() for value in rhs.split('|')]
        for value in rhs:
            if lhs in result.keys():
                result[lhs].append((value))
            else:
                result[lhs] = [(value)]
    return result

if __name__ == '__main__':

    grammar = read_from_file()
    ui = UI(grammar)
    ui.run()
