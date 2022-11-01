from LanguageSpecifications import separators, read_token, reserved_words, operators
from ProgramInternalForm import ProgramInternalForm
from Scanner import Scanner
from SymbolTable import SymbolTable

class Main:
    def __init__(self, st, pif, scanner):
        self.st = st
        self.pif = pif
        self.scanner = scanner
        read_token()

    def run(self):
        with open('program.txt', 'r') as program:
            line_number = 0
            ok = 1
            for line in program:
                tokens = self.scanner.tokenize(line.strip())
                line_number += 1
                for token in tokens:
                    if token in separators + reserved_words + operators and token != ' ':
                        self.pif.insert(token, -1)
                    elif token == ' ':
                        continue
                    elif self.scanner.is_identifier(token):
                        self.st.insert(token)
                        self.pif.insert('id', self.st.search_position(token))
                    elif self.scanner.is_constant(token):
                        self.st.insert(token)
                        self.pif.insert('const', self.st.search_position(token))
                    else:
                        print('Lexical error at token ' + token + ', at line ' + str(line_number))
                        ok = 0
        if ok == 1:
            print('Lexically correct')
            with open('ST.out', 'w') as st_out:
                st_out.write(str(self.st))
            with open('PIF.out', 'w') as pif_out:
                pif_out.write(str(self.pif))


st = SymbolTable()
pif = ProgramInternalForm()
scanner = Scanner()
main = Main(st, pif, scanner)
main.run()
