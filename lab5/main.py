from Grammar import Grammar
from UI import UI


def parse_line(line):
    return [value.strip() for value in line.strip().split('=')[1].strip().split(',')]

def read_from_file():
    with open("g2.txt") as f:
        N = parse_line(f.readline())
        E = parse_line(f.readline())
        S = parse_line(f.readline())
        P = {}
        for line in f:
            line = line.strip().split('->')
            P[line[0].strip()] = [value.strip() for value in line[1].split('|')]
    return Grammar(N, E, P, S)

if __name__ == '__main__':

    grammar = read_from_file()
    ui = UI(grammar)
    ui.run()
