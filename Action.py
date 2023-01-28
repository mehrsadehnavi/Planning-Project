class Action:
    def __init__(self, name, positive_preconditions, negative_preconditions, add_list, delete_list):
        self.name = name
        self.positive_preconditions = positive_preconditions
        self.negative_preconditions = negative_preconditions
        self.add_list = add_list
        self.delete_list = delete_list

    def regress(self, state):
        for positive_literal in state.positive_literals:
            if positive_literal in self.add_list:
                state.positive_literals.remove(positive_literal)

        for negative_literal in state.negative_literals:
            if negative_literal in self.delete_list:
                state.negative_literals.remove(negative_literal)

        state.positive_literals.extend(self.positive_preconditions)
        state.negative_literals.extend(self.negative_preconditions)
        state.positive_literals = list(set(state.positive_literals))
        state.negative_literals = list(set(state.negative_literals))
        return

    def progress(self, state):
        state.positive_literals.extend(self.add_list)
        state.negative_literals.extend(self.delete_list)
        state.positive_literals = list(set(state.positive_literals))
        state.negative_literals = list(set(state.negative_literals))

        for positive_literal in state.positive_literals:
            for negative_effect in self.delete_list:
                if negative_effect == positive_literal:
                    state.positive_literals.remove(positive_literal)

        for negative_literal in state.negative_literals:
            for positive_effect in self.add_list:
                if positive_effect == negative_literal:
                    state.negative_literals.remove(negative_literal)
        return

    def is_relevant(self, state):
        if not self.is_unified(state):
            return False

        if self.is_conflicting(state):
            return False

        return True

    def is_executable(self, state):
        for positive_preconditions in self.positive_preconditions:
            if positive_preconditions not in state.positive_literals:
                return False

        for negative_preconditions in self.negative_preconditions:
            if negative_preconditions not in state.negative_literals:
                return False

        return True

    def is_unified(self, state):
        return not (set(state.positive_literals).isdisjoint(self.add_list) and set(state.negative_literals).isdisjoint(self.delete_list))

    def is_conflicting(self, state):
        return not (set(state.positive_literals).isdisjoint(self.delete_list) or set(state.negative_literals).isdisjoint(self.add_list))

    def to_string(self):
        return f'action, name: {self.name}, positive preconditions: {self.positive_preconditions}, negative preconditions: {self.negative_preconditions}, add list: {self.add_list}, delete list: {self.delete_list}'

    def relaxed_1(self, state, actions):
        for action in actions:
            state.positive_literals.remove(action.positive_preconditions)
            state.negative_literals.remove(action.negative_preconditions)

    def relaxed_2(self):
        self.delete_list = []