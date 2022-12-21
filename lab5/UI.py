from Parser import Parser
from ParserOutput import ParserOutput


class UI:
    def __init__(self, grammar):
        self.grammar = grammar
        self.parser = Parser(grammar)
        self.parserOutput = ParserOutput(self.parser)

    def run(self):
        while True:
            print("1. Print nonterminals")
            print("2. Print terminals")
            print("3. Print set of productions")
            print("4. Print productions for a given nonterminal")
            print("5. Check if grammar is a CFG")
            print("6. Parse a given word")
            print("0. Exit")
            command = input("Enter command: ")
            if command == "1":
                print(self.grammar.get_nonterminals())
            elif command == "2":
                print(self.grammar.get_terminals())
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
            elif command == "6":
                word = input("Enter word: ")
                S = self.grammar.S[:]  # making a copy so that I can run the function multiple times
                # parser = Parser(self.grammar)
                self.parser.parse([*word])
                self.grammar.S = S
                self.parserOutput.build_tree()
                print(self.parserOutput.print_parsing_tree())
                if self.parser.state == 'f':
                    print("The word is accepted")
                else:
                    print("The word is not accepted")
            elif command == "0":
                break
            else:
                print("Invalid command")


