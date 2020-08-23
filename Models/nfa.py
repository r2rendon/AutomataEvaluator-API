from Models.automata import Automata
from Models.dfa import DFA

class NFA(Automata):
    def __init__(self, dbAutomata, accepting_states, transitions):
        super().__init__(dbAutomata, accepting_states, transitions)
        
    def __init__(self, dbAutomata, accepting_states, transitions):
        super().__init__()

    # NFA Evaluate method returns the equivalent DFA
    def evaluate(self, expression): 
        # 
        pass
