from State import State
from Test import PlanningProblem


def forward_search(goal_state, initial_state, actions):
    fringe = [initial_state]
    in_fringe = [initial_state.hash()]
    explored = []

    i = 0
    while fringe:
        current_state = fringe.pop(0)
        in_fringe.pop(0)
        explored.append(current_state.hash())
        successors = get_successors(current_state, actions)

        for successor in successors:
            if goal_test(successor, goal_state):
                print_solution(successor)
                return i
            else:
                if successor.hash() not in in_fringe and successor.hash() not in explored:
                    fringe.append(successor)
                    in_fringe.append(successor.hash())
        i += 1


def get_successors(state, actions):
    result = []
    for action in actions:
        if action.is_executable(state):
            successors = State(state, action, state.positive_literals, state.negative_literals)
            action.progress(successors)
            result.append(successors)

    return result


def goal_test(state, goal_state):  # should be checked
    for positive_literal in goal_state.positive_literals:
        if positive_literal not in state.positive_literals:
            return False

    for positive_literal in goal_state.positive_literals:
        if positive_literal in state.negative_literals:
            return False

    for negative_literal in goal_state.negative_literals:
        if negative_literal in state.positive_literals:
            return False
    return True


def print_solution(state):
    while True:
        if state.action == None or state.parent == None:
            break
        print(state.action.to_string())
        state = state.parent


def ignore_preconditions_heuristic(state, goal_state, actions):
    relaxed_planning_problem = PlanningProblem(initial_state=state.state,
                                               goal_state=goal_state,
                                               actions=[action.relaxed_1(state, actions) for action in actions])
    try:
        return len(relaxed_planning_problem.test())
    except:
        return float('inf')


def ignore_delete_lists(state, goal_state, actions):
    relaxed_planning_problem = PlanningProblem(initial_state=state.state,
                                               goal_state=goal_state,
                                               actions=[action.relaxed_2() for action in actions])
    try:
        return len(relaxed_planning_problem.test())
    except:
        return float('inf')
