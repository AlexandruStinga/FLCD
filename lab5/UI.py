class UI:
    def __init__(self, grammar):
        self.grammar = grammar

    def run(self):
        while True:
            print("1. Print nonterminals")
            print("2. Print terminals")
            print("3. Print set of productions")
            print("4. Print productions for a given nonterminal")
            print("5. Check if grammar is a CFG")
            print("0. Exit")
            command = input("Enter command: ")
            if command == "1":
                self.grammar.print_nonterminals()
            elif command == "2":
                self.grammar.print_terminals()
            elif command == "3":
                self.grammar.print_set_of_productions()
            elif command == "4":
                n = input("Enter nonterminal: ")
                self.grammar.print_productions_for_non_terminal(n)
            elif command == "5":
                if self.grammar.check_if_context_free_grammar():
                    print("The grammar is a CFG")
                else:
                    print("The grammar is not a CFG")
            elif command == "0":
                break
            else:
                print("Invalid command")


