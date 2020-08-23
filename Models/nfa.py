from Models.automata import Automata

class NFA(Automata):
    def __init__(self, dbAutomata, accepting_states, transitions):
        super().__init__(dbAutomata, accepting_states, transitions)

    # NFA Evaluate method returns the equivalent DFA
    def evaluate(self, expression): 
        # 
        pass
