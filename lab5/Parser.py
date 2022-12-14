from utils import flatten
import itertools

class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.state = 'q'
        self.index = 0
        self.working_stack = []
        self.input_stack = self.grammar.S

    def expand(self):
        head = self.input_stack.pop(0)
        self.working_stack.append((head, 0))
        production = self.grammar.P[head][0]
        self.input_stack.insert(0, production)
        self.input_stack = flatten(self.input_stack)

    def advance(self):
        self.index += 1
        head = self.input_stack.pop(0)
        self.working_stack.append(head)

    def momentary_insuccess(self):
        self.state = 'b'

    def back(self):
        self.index -= 1
        head = self.working_stack.pop()
        self.input_stack.insert(0, head)

    def success(self):
        self.state = 'f'

    def another_try(self):
        nonterminal, prod_index = self.working_stack.pop()
        if prod_index + 1 < len(self.grammar.P[nonterminal]):
            prod_index += 1
            self.working_stack.append((nonterminal, prod_index))
            new_production = self.grammar.P[nonterminal][prod_index]
            del self.input_stack[:len(self.grammar.P[nonterminal][prod_index - 1])]
            self.input_stack.insert(0, new_production)
            self.input_stack = flatten(self.input_stack)
            self.state = 'q'
        elif self.index == 0 and self.input_stack[-1] == self.grammar.S:
            self.state = 'e'
        else:
            del self.input_stack[:len(self.grammar.P[nonterminal][prod_index])]
            self.input_stack.insert(0, nonterminal)
            self.input_stack = flatten(self.input_stack)

    def parse(self, word):
        while self.state != 'f' and self.state != 'e':
            if self.state == 'q':
                if len(self.input_stack) == 0 and self.index == len(word):
                    self.success()
                elif len(self.input_stack) == 0:
                    self.momentary_insuccess()
                elif self.input_stack[0] in self.grammar.get_nonterminals():
                    self.expand()

                elif self.index < len(word) and self.input_stack[0] == word[self.index]:
                    self.advance()
                else:
                    self.momentary_insuccess()

            elif self.state == 'b':
                if self.working_stack[-1] in self.grammar.get_terminals():
                    self.back()
                else:
                    self.another_try()

