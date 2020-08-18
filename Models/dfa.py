class DFA:
    def __init__(self, alphabet, states, initial_state, accepting_states, transitions):
        self.alphabet = alphabet
        self.states = states
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.transitions = transitions
        
    def dfa_evaluate(self, expression):
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
            # print(current_state, current_char, next_state) This format can be used to return the evaluation process in the automata
            current_state = next_state

        # If the transition exists and the current state is an accepting state, then the expression belongs to the automata
        return (transition_exists and current_state in accepting_states)