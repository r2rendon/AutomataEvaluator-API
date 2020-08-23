from Models.automata import Automata

class NFA(Automata):
    def __init__(self, dbAutomata, accepting_states, transitions):
        self.alphabet = dbAutomata["alphabet"]
        self.states = dbAutomata["states"]
        self.initial_state = dbAutomata["initial_state"]
        self.accepting_states = accepting_states
        self.transitions = transitions

    # NFA Evaluate method returns the equivalent DFA
    def evaluate(self, expression):
        pass
