class FiniteAutomata:
    def __init__(self, Q, E, q0, F, S):
        self.Q = Q
        self.E = E
        self.q0 = q0
        self.F = F
        self.S = S

    def is_DFA(self):
        for key in self.S.keys():
            if len(self.S[key]) > 1:
                return False
        return True

    def is_accepted(self, sequence):
        if not self.is_DFA():
            return False
        q = self.q0
        for character in sequence:
            q = self.S[(q, character)][0]
        return q in self.F
