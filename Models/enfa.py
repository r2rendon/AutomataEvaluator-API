from Models.automata import Automata
from Models.nfa import NFA

class ENFA(Automata):
    def __init__(self, dbAutomata, accepting_states, transitions):
        super().__init__(dbAutomata, accepting_states, transitions)

    # evaluate transforms ENFA to NFA
    def evaluate(self, expression):
        newNFA = NFA()
        # Define equivalent NFA transitions
        for state in self.states:
            for aElement in self.alphabet:
                newNFA.transitions[(state, aElement)] = self.getNextState(state, aElement)

        # Equal automata elements
        newNFA.states = self.states
        
        newNFA.accepting_states = self.accepting_states
        
        alphabetList = self.alphabet
        alphabetList.remove('Ɛ')
        newNFA = alphabetList

        newNFA.accepting_states = self.accepting_states
        return newNFA

    def getNextState(self, state, aElement):
        # Get epsilon enclosure per next state
        firstEnclosureList = self.getEpsilonEnclosure(state)

        # Get the states you get to in base of the alphabet element and the enclosure element
        for firstEnclosureElement in firstEnclosureList:
            # Get a list of all transitions in base of the firstEnclosureElements
            stateFromEnclosureList = list()
            for transition in self.transitions:
                transitionTupleElements = list(transition.keys())
                if(transitionTupleElements[1] == aElement and firstEnclosureElement == transitionTupleElements[0]):
                    stateFromEnclosureList.append(transition)
                    break
        # Second for end

        # Get epsilon enclosure per states from the first enclosure
        if(stateFromEnclosureList.count() > 0):
            nextStates = list()
            for stateFromEnclosure in stateFromEnclosureList:
                nextStates.extend(self.getEpsilonEnclosure(stateFromEnclosure))
            return nextStates
        else:
            return list()

    def getEpsilonEnclosure(self, state):
        firstEnclosureList = list()
        nextState = state
        for transition in self.transitions:
            transitionTupleElements = list(transition.keys())
            if transitionTupleElements[1] == 'Ɛ' and transitionTupleElements[0] == nextState:
                firstEnclosureList.append(transition)
                nextState = transition
        return firstEnclosureList