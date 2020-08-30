from Models.automata import Automata
from Models.nfa import NFA

class ENFA(Automata):
    def __init__(self, dbAutomata, accepting_states, transitions):
        super().__init__(dbAutomata, accepting_states, transitions)

    # evaluate transforms ENFA to NFA
    def evaluate(self, expression):
        dbAutomata = dict()
        dbAutomata["alphabet"] = self.alphabet
        dbAutomata["states"] = self.states
        dbAutomata["initial_state"] = self.initial_state
        newNFA = NFA(dbAutomata, self.accepting_states, self.transitions)
        newNFA.transitions = dict()

        alphabetList = self.alphabet
        alphabetList.remove('Ɛ')
        newNFA.alphabet = alphabetList
        
        # Define equivalent NFA transitions
        for state in self.states:
            for aElement in newNFA.alphabet:
                nextState = self.getNextState(state, aElement)
                if nextState != []:
                    newNFA.transitions[(state, aElement)] = nextState 

        # Equal automata elements
        newNFA.states = self.states
        
        newNFA.accepting_states = self.accepting_states
        

        return newNFA

    def getNextState(self, state, aElement):
        # Get epsilon enclosure per next state
        firstEnclosureList = self.getEpsilonEnclosure(state)

        # Get the states you get to in base of the alphabet element and the enclosure element
        stateFromEnclosureList = list()
        for firstEnclosureElement in firstEnclosureList:
            # Get a list of all transitions in base of the firstEnclosureElements
            for transition in self.transitions:
                transitionTupleElements = list(transition)
                if(transitionTupleElements[1] == aElement and firstEnclosureElement == transitionTupleElements[0]):
                    stateFromEnclosureList.extend(self.transitions[transition].split(','))
                    break
        # Second for end

        # Get epsilon enclosure per states from the first enclosure
        if(len(stateFromEnclosureList) > 0):
            nextStates = list()
            for stateFromEnclosure in stateFromEnclosureList:
                nextStates.extend(self.getEpsilonEnclosure(stateFromEnclosure))
            return nextStates
        else:
            return list()

    def getEpsilonEnclosure(self, state):
        firstEnclosureList = list()
        firstEnclosureList.append(state)
        for transition in self.transitions:
            transitionTupleElements = list(transition)
            if transitionTupleElements[1] == 'Ɛ' and transitionTupleElements[0] == state:
                splitTransition = self.transitions[transition].split(',')
                if(len(splitTransition) > 1):
                    for split in splitTransition:
                        firstEnclosureList = firstEnclosureList+self.getEpsilonEnclosure(split)
                else:
                    firstEnclosureList = firstEnclosureList+splitTransition
        return firstEnclosureList