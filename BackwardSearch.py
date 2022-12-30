from State import State


def backward_search(goal_state, initial_state, actions):
    fringe = [goal_state]
    in_fringe = [goal_state.hash()]
    explored = []

    while fringe:
        current_state = fringe.pop(0)
        in_fringe.pop(0)
        explored.append(current_state.hash())
        predecessor = get_predecessor(current_state, actions)

        for predecessor in predecessor:
            if goal_test(predecessor, initial_state):
                print_solution(predecessor)
                return
            else:
                if predecessor.hash() not in in_fringe and predecessor.hash() not in explored:
                    fringe.append(predecessor)
                    in_fringe.append(predecessor.hash())


def get_predecessor(state, actions):
    result = []
    for action in actions:
        if action.is_relevant(state):
            predecessor = State(state, action, state.positive_literals)
            action.regress(predecessor)
            result.append(predecessor)

    return result


def goal_test(state, initial_state):
    for positive_literal in state.positive_literals:
        if positive_literal not in initial_state.positive_literals:
            return False

    for negative_literal in state.negative_literals:
        if negative_literal in initial_state.positive_literals:
            return False

    return True


def print_solution(state):
    while True:
        if state.action == None or state.parent == None:
            break
        print(state.action.to_string())
        state = state.parent