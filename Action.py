class Action:
    def __init__(self, name, positive_preconditions, negative_preconditions, add_list, delete_list):
        self.name = name
        self.positive_preconditions = positive_preconditions
        self.negative_preconditions = negative_preconditions
        self.add_list = add_list
        self.delete_list = delete_list

    def regress(self, state):
        state - add_list + positive_preconditions
        return

    def is_relevant(self, state):
        if not self.is_unified(state):
            return False

        if self.is_conflicting(state):
            return False

        return True

    def is_unified(self, state):
    #ایا با این اکشن میتوینم بهش برسیم یا نه
    # add list should be in positive and delete list in negative
        #write your code
        return

    def is_conflicting(self, state):
        #پازتیو اینو با دیلیت لیست(نگاتیو) اون چک میکنه
        #write your code
        return

    def to_string(self):
        return f'action, name: {self.name}, positive preconditions: {self.positive_preconditions}, negative preconditions: {self.negative_preconditions}, add list: {self.add_list}, delete list: {self.delete_list}'