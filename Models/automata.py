class Automata:
    def __init__(self, dbAutomata, accepting_states, transitions):
        self.alphabet = dbAutomata["alphabet"]
        self.states = dbAutomata["states"]
        self.initial_state = dbAutomata["initial_state"]
        self.accepting_states = accepting_states
        self.transitions = transitions
    
    def __init__(self):
        self.alphabet = list()
        self.states = list()
        self.initial_state = ""
        self.accepting_states = set()
        self.transitions = dict()

    def evaluate(self, expression):
        pass
