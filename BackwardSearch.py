import copy
import math

from State import State


def backward_search(goal_state, initial_state, actions, is_original_problem):
    fringe = [goal_state]
    in_fringe = [goal_state.hash()]
    explored = []
    node_checked_counter = 0

    while fringe:
        if is_original_problem:
            fringe.sort(key=lambda node: ignore_preconditions_heuristic(node, initial_state, actions))
            # fringe.sort(key=lambda node: ignore_delete_lists(node, initial_state, actions))

        current_state = fringe.pop(0)
        in_fringe.pop(0)
        explored.append(current_state.hash())
        predecessor = get_predecessor(current_state, actions)

        for predecessor in predecessor:
            node_checked_counter += 1
            if goal_test(predecessor, initial_state):
                if is_original_problem:
                    print_solution(predecessor)
                    return
                else:
                    return node_checked_counter
            else:
                if predecessor.hash() not in in_fringe and predecessor.hash() not in explored:
                    fringe.append(predecessor)
                    in_fringe.append(predecessor.hash())


def get_predecessor(state, actions):
    result = []
    for action in actions:
        if action.is_relevant(state):
            predecessor = State(state, action, state.positive_literals, state.negative_literals)
            action.regress(predecessor)
            result.append(predecessor)

    return result


def goal_test(state, initial_state):
    for positive_literal in initial_state.positive_literals:
        if positive_literal not in state.positive_literals:
            return False

    for positive_literal in initial_state.positive_literals:
        if positive_literal in state.negative_literals:
            return False

    for negative_literal in initial_state.negative_literals:
        if negative_literal in state.positive_literals:
            return False

    return True


def print_solution(state):
    while True:
        if state.action is None or state.parent is None:
            break
        print(state.action.to_string())
        state = state.parent


def ignore_preconditions_heuristic(initial_state, goal_state, actions):
    no_precondition_actions = copy.deepcopy(actions)
    for action in no_precondition_actions:
        action.negative_preconditions = []
        action.positive_preconditions = []
    relaxed_planning_problem = backward_search(copy.deepcopy(goal_state), copy.deepcopy(initial_state), no_precondition_actions, False)
    if relaxed_planning_problem is not None:
        return relaxed_planning_problem
    else:
        return math.inf


def ignore_delete_lists(initial_state, goal_state, actions):
    no_delete_list_actions = copy.deepcopy(actions)
    for action in no_delete_list_actions:
        action.delete_list = []
    relaxed_planning_problem = backward_search(copy.deepcopy(goal_state), copy.deepcopy(initial_state), no_delete_list_actions, False)
    if relaxed_planning_problem is not None:
        return relaxed_planning_problem
    else:
        return math.inf
