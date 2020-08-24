from Models.automata import Automata
from Models.dfa import DFA

class NFA(Automata):
    def __init__(self, dbAutomata, accepting_states, transitions):
        super().__init__(dbAutomata, accepting_states, transitions)
        
    def __init__(self, dbAutomata, accepting_states, transitions):
        super().__init__()

    # NFA Evaluate method returns the equivalent DFA
    def evaluate(self, expression): 
        # Place the equivalent transitions per state on new DFA automata
        
        pass

    def getDFATransitions(self):
        # Get all the equivalent transitions
        for transition in self.transitions:
            currentTransitionKeys = list(transition.keys)
            for aElement in self.alphabet:
                if(self.transitions[(currentTransitionKeys, aElement)] not in self.transitions):
                    pass
                pass
            pass
        pass

    def getNewState(self):
        lastState = self.states[len(self.states)-1]
        currentNumState = int(lastState[1])
        currentNumState += 1
        return "q"+currentNumState

