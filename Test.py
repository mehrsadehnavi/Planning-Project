from State import State
from BackwardSearch import backward_search
from ForwardSearch import forward_search
from tireproblem import get_actions
import time


def main():
    print("Getting the set of all actions...")
    actions = get_actions()
    start_time = time.time()

    print("Planning...")
    initial_state = State(None, None, positive_literals=["atflataxle", "atsparetrunk"], negative_literals=['atflatground', 'atflattrunk', 'atspareground', 'atspareaxle'])
    goal_state = State(None, None, positive_literals=["atspareaxle"], negative_literals=[])
    # actions = [Action("Generic", positive_preconditions=["A", "B"], negative_preconditions=[], add_list=["C"], delete_list=[]), \
    # Action("Generic", positive_preconditions=["B", "C"], negative_preconditions=[], add_list=["D"], delete_list=[])]
    # backward_search(goal_state, initial_state, actions)
    print('Backward Search Answer:')
    backward_search(goal_state, initial_state, actions)
    print('Forward Search Answer:')
    forward_search(goal_state, initial_state, actions)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
