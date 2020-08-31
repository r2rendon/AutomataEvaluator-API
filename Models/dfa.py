from Models.automata import Automata

class DFA(Automata):
    def __init__(self, dbAutomata, accepting_states, transitions):
        super().__init__(dbAutomata, accepting_states, transitions)
        
    def evaluate(self, expression):
        initial_state = self.initial_state
        accepting_states = self.accepting_states
        transitions = self.transitions

        current_state = initial_state

        transition_exists = True

        for char_index in range(len(expression)):
            current_char = expression[char_index]

            if ((current_state, current_char) not in transitions):
                transition_exists = False
                break
            next_state = transitions[(current_state, current_char)]
            current_state = next_state

        # If the transition exists and the current state is an accepting state, then the expression belongs to the automata
        return (transition_exists and current_state in accepting_states)