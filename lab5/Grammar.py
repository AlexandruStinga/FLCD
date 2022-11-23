class Grammar:
    def __init__(self, N, E, P, S):
        self.N = N
        self.E = E
        self.P = P
        self.S = S

    def print_nonterminals(self):
        print("Nonterminals: ", end="")
        for n in self.N:
            print(n, end=" ")
        print()

    def print_terminals(self):
        print("Terminals: ", end="")
        for e in self.E:
            print(e, end=" ")
        print()

    def print_set_of_productions(self):
        print("Set of productions:")
        for p in self.P:
            print(p[0], end=" ")
            for i in range(1, len(p)):
                print(p[i], end=" ")
            print()

    def print_productions_for_non_terminal(self, n):
        print("Productions for non-terminal", n, ":")
        for p in self.P:
            if p[0] == n:
                print(p[0], end=" ")
                for i in range(1, len(p)):
                    print(p[i], end=" ")
                print()

    def check_if_context_free_grammar(self):
        for p in self.P:
            if len(p) == 1:
                return False
        return True