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
        state.positive_literals = list(set(state.positive_literals.extend(self.positive_preconditions)))
        state.negative_literals = list(set(state.negative_literals.extend(self.negative_preconditions)))
        #state - add_list + positive_preconditions (or preconditions)
        return


    def progress(self, state):
        state.positive_literals = list(set(state.positive_literals.extend(self.add_list)))
        state.negative_literals = list(set(state.positive_literals.extend(self.delete_list)))
        for positive_literal in state.positive_literals:
            if positive_literal in state.negative_literals:
                state.positive_literals.remove(positive_literal)
        #state + add_list - delete_list
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
        # ایا با این اکشن میتوینم بهش برسیم یا نه
        # add list should be in positive and delete list in negative
        return not (set(state.positive_literals).isdisjoint(self.add_list) and set(state.negative_literals).isdisjoint(self.delete_list))

    def is_conflicting(self, state):
        # پازتیو اینو با دیلیت لیست(نگاتیو) اون چک میکنه
        return not set(state.positive_literals).isdisjoint(self.delete_list)

    def to_string(self):
        return f'action, name: {self.name}, positive preconditions: {self.positive_preconditions}, negative preconditions: {self.negative_preconditions}, add list: {self.add_list}, delete list: {self.delete_list}'
