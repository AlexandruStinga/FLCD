from Grammar import Grammar
from Parser import Parser
from ParserOutput import ParserOutput
from UI import UI


def read_file():
    with open('g2.txt', "r") as f:
        N = parse_line(f.readline())
        E = parse_line(f.readline())
        S = parse_line(f.readline())
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
    parser = Parser(grammar)
    parserOutput = ParserOutput(parser)
    ui = UI(grammar)
    ui.run()
