from Models.automata import Automata
from Models.dfa import DFA

class NFA(Automata):
    def __init__(self, dbAutomata, accepting_states, transitions):
        super().__init__(dbAutomata, accepting_states, transitions)
        
    def __init__(self):
        super().__init__()

    # NFA Evaluate method returns the equivalent DFA
    def evaluate(self, expression): 
        newDFA = DFA()

        newDFA.alphabet = self.alphabet
        newDFA.states = self.states

        newDFA.initial_state = self.initial_state
        newDFA.accepting_states = self.accepting_states

        # Place the equivalent transitions per state on new DFA automata
        equivalentTransitions = self.getDFATransitions()
        newDFA.transitions = equivalentTransitions[0]
        if(equivalentTransitions[1] != ""):
            newDFA.states.append(equivalentTransitions[1])

        return newDFA

    def getDFATransitions(self):
        # Get all the equivalent transitions
        eqTransitionsDict = dict()
        newDeadState = ""
        for transition in self.transitions:
            currentTransitionKeys = list(transition.keys)
            for aElement in self.alphabet:
                if(self.transitions[(currentTransitionKeys[0], aElement)] not in self.transitions):
                    if(newDeadState==""):
                        newDeadState = getNewState()
                    eqTransitionsDict[(newDeadState, aElement)] = newDeadState
                else:
                    eqTransitionsDict[(currentTransitionKeys[0], aElement)] = self.transitions[(currentTransitionKeys[0], aElement)]
        
        return (eqTransitionsDict, newDeadState)


    def getNewState(self):
        lastState = self.states[len(self.states)-1]
        currentNumState = int(lastState[1])
        currentNumState += 1
        return "q"+currentNumState

