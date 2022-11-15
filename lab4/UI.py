from FiniteAutomata import FiniteAutomata


def read_file():
    with open('FA.in') as f:
        Q = f.readline().strip().split(' ')[2:]
        E = f.readline().strip().split(' ')[2:]
        q0 = f.readline().strip().split(' ')[2]
        F = f.readline().strip().split(' ')[2:]
        S = {}
        for line in f:
            line = line.strip().split('->')
            source = line[0].strip().replace('(', '').replace(')', '').split(',')[0]
            route = line[0].strip().replace('(', '').replace(')', '').split(',')[1]
            destination = line[1].strip()

            if (source, route) in S.keys():
                S[(source, route)].append(destination)
            else:
                S[(source, route)] = [destination]
        return Q, E, q0, F, S


class UI:
    def __init__(self):
        Q, E, q0, F, S = read_file()
        self.fa = FiniteAutomata(Q, E, q0, F, S)

    def run(self):
        while True:
            print('1.Display the set of states')
            print('2.Display the alphabet')
            print('3.Display the initial state')
            print('4.Display the set of final states')
            print('5.Display the transition function')
            print('6.Check if a sequence is accepted')
            print('7.Exit')

            command = input('Enter command: ')
            if command == '1':
                print(self.fa.Q)
            elif command == '2':
                print(self.fa.E)
            elif command == '3':
                print(self.fa.q0)
            elif command == '4':
                print(self.fa.F)
            elif command == '5':
                print(self.fa.S)
            elif command == '6':
                w = input('Enter sequence: ')
                try:
                    print(self.fa.is_accepted(w))
                except:
                    print('Invalid sequence')
            elif command == '7':
                break
            else:
                print('Invalid command')
