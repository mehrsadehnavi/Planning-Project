from State import State
from BackwardSearch import backward_search
from ForwardSearch import forward_search
from tireproblem import get_actions
import time


class PlanningProblem:
    def __init__(self, initial_state, goal_state, actions):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions

    def test(self):
        print("Getting the set of all actions...")

        self.actions = get_actions()
        start_time = time.time()

        print("Planning...")
        self.initial_state = State(None, None, positive_literals=["atflataxle", "atsparetrunk"], negative_literals=['atflatground', 'atflattrunk', 'atspareground', 'atspareaxle'])
        self.goal_state = State(None, None, positive_literals=["atspareaxle"], negative_literals=[])
        # actions = [Action("Generic", positive_preconditions=["A", "B"], negative_preconditions=[], add_list=["C"], delete_list=[]), \
        # Action("Generic", positive_preconditions=["B", "C"], negative_preconditions=[], add_list=["D"], delete_list=[])]
        # backward_search(goal_state, initial_state, actions)
        print('Backward Search Answer:')
        backward_search(self.goal_state, self.initial_state, self.actions)
        print('Forward Search Answer:')
        step = forward_search(self.goal_state, self.initial_state, self.actions)
        print("--- %s seconds ---" % (time.time() - start_time))
        return step



# def main():
#     print("Getting the set of all actions...")
#     actions = get_actions()
#     start_time = time.time()
#
#     print("Planning...")
#     initial_state = State(None, None, positive_literals=["atflataxle", "atsparetrunk"], negative_literals=['atflatground', 'atflattrunk', 'atspareground', 'atspareaxle'])
#     goal_state = State(None, None, positive_literals=["atspareaxle"], negative_literals=[])
#     # actions = [Action("Generic", positive_preconditions=["A", "B"], negative_preconditions=[], add_list=["C"], delete_list=[]), \
#     # Action("Generic", positive_preconditions=["B", "C"], negative_preconditions=[], add_list=["D"], delete_list=[])]
#     # backward_search(goal_state, initial_state, actions)
#     print('Backward Search Answer:')
#     backward_search(goal_state, initial_state, actions)
#     print('Forward Search Answer:')
#     forward_search(goal_state, initial_state, actions)
#     print("--- %s seconds ---" % (time.time() - start_time))


# if __name__ == "__main__":
#     main()
