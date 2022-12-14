from Grammar import Grammar
from UI import UI


def read_file():
    with open('g1.txt', "r") as f:
        N = parse_line(f.readline())
        E = parse_line(f.readline())
        S = parse_line(f.readline())[0]
        P = {}
        for line in f:
            production = line.strip().split("->")
            key = production[0].strip()
            values = production[1].strip().split("|")
            for value in values:
                value = value.strip()
                if key not in P.keys():
                    P[key] = []
                P[key].append(value.split(" "))
    return Grammar(N, E, P, S)


def parse_line(line):
    return line.split("=")[1].strip().split(" ")


if __name__ == '__main__':
    grammar = read_file()
    ui = UI(grammar)
    ui.run()
