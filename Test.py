from State import State
from BackwardSearch import backward_search
from ForwardSearch import forward_search
# from tireproblem import get_actions
from BlockWorldProblem import get_actions
import time


def main():
    print("Getting the set of all actions...")
    actions = get_actions()
    # print(actions)

    print("Planning...")

    # initial_state = State(None, None, positive_literals=["atflataxle", "atsparetrunk"],
    #                       negative_literals=['atflatground', 'atflattrunk', 'atspareground', 'atspareaxle'])
    # goal_state = State(None, None, positive_literals=["atspareaxle", 'atflatground'],
    #                    negative_literals=['atspareground', 'atsparetrunk', 'atflataxle', 'atflattrunk'])

    initial_state = State(None, None,
                          positive_literals=["onAtable", "onCA", "onBtable", "clearB", "clearC", "cleartable", "blockB",
                                             "blockC", "blockA"],
                          negative_literals=["clearA", "onBA", "onBC", "onAB", "onAC", "onAB", "onCB"])

    goal_state = State(None, None, positive_literals=["onAB", "onBC"],
                       negative_literals=['onAB', 'onAC', 'onBC', 'onCA', "clearB", "clearC"])
    # Action("Generic", positive_preconditions=["B", "C"], negative_preconditions=[], add_list=["D"], delete_list=[])]
    start_time = time.time()
    print('Backward Search Answer:')
    backward_search(goal_state, initial_state, actions, True)
    print("--- %s seconds ---" % (time.time() - start_time))
    # start_time = time.time()
    # print('Forward Search Answer:')
    # forward_search(goal_state, initial_state, actions, True)
    # print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()