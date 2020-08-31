from Models.automata import Automata
from Models.dfa import DFA

class NFA(Automata):
    def __init__(self, dbAutomata, accepting_states, transitions):
        super().__init__(dbAutomata, accepting_states, transitions)

    # NFA Evaluate method returns the equivalent DFA
    def evaluate(self, expression): 
        dbAutomata = dict()
        dbAutomata["alphabet"] = self.alphabet
        dbAutomata["states"] = self.states
        dbAutomata["initial_state"] = self.initial_state
        newDFA = DFA(dbAutomata, self.accepting_states, self.transitions)

        newDFA.alphabet = self.alphabet

        newDFA.initial_state = self.initial_state
        newDFA.accepting_states = self.accepting_states

        # Place the equivalent transitions per state on new DFA automata
        equivalentTransitions = self.getDFAEquivalence()
        newDFA.transitions = equivalentTransitions[1]
        newDFA.states = self.getCleanStates(equivalentTransitions[0])
        newDFA.accepting_states = set(self.getAcceptingStates(equivalentTransitions[0]))

        return newDFA

    def getDFAEquivalence(self):
        newStates = [[self.initial_state]]
        newTransitions = dict()
        for newState in newStates:
            for aElement in self.alphabet:
                if (newState[0], aElement) in self.transitions:
                    currentTransition = self.transitions[(newState[0], aElement)] 
                    if currentTransition not in newStates:
                        if len(currentTransition) > 1:
                            newStates.append(currentTransition)
                            for alph in self.alphabet:
                                res = ''
                                for transition in currentTransition:
                                    if(transition, alph) in self.transitions:
                                        res = res+(''.join(self.transitions[(transition, alph)]))
                                newTransitions[newState[0], alph] = res
                                newTransitions[''.join(currentTransition), alph] = res
                        else:
                            newStates.append(currentTransition)
                            newTransitions[(newState[0], aElement)] = currentTransition[0]

        return (newStates, newTransitions)

    def getAcceptingStates(self, states):
        acceptingStates = list()
        for state in states:
            for tmp in state:
                if tmp in self.accepting_states:
                    acceptingStates.append(''.join(state))

        return acceptingStates

    def getCleanStates(self, states):
        newStates = list()
        for state in states:
            if len(state) > 1:
                newStates.append(''.join(state))
            else:
                newStates.append(state[0])

        return newStates


