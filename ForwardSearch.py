import copy
import math

from State import State


def forward_search(goal_state, initial_state, actions, is_original_problem):
    fringe = [initial_state]
    in_fringe = [initial_state.hash()]
    explored = []
    node_checked_counter = 0

    while fringe:
        # if is_original_problem:
        #     fringe.sort(key=lambda node: ignore_preconditions_heuristic(node, initial_state, actions))
        #     fringe.sort(key=lambda node: ignore_delete_lists(node, initial_state, actions))

        current_state = fringe.pop(0)
        in_fringe.pop(0)
        explored.append(current_state.hash())
        successors = get_successors(current_state, actions)

        for successor in successors:
            node_checked_counter += 1
            if goal_test(successor, goal_state):
                if is_original_problem:
                    print_solution(successor)
                    return
                else:
                    return node_checked_counter
            else:
                if successor.hash() not in in_fringe and successor.hash() not in explored:
                    fringe.append(successor)
                    in_fringe.append(successor.hash())


def get_successors(state, actions):
    result = []
    for action in actions:
        if action.is_executable(state):
            successors = State(state, action, state.positive_literals, state.negative_literals)
            action.progress(successors)
            result.append(successors)
    return result


def goal_test(state, goal_state):
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
        if state.action is None or state.parent is None:
            break
        print(state.action.to_string())
        state = state.parent


def ignore_preconditions_heuristic(initial_state, goal_state, actions):
    no_precondition_actions = copy.deepcopy(actions)
    for action in no_precondition_actions:
        action.negative_preconditions = []
        action.positive_preconditions = []
    relaxed_planning_problem = forward_search(copy.deepcopy(goal_state), copy.deepcopy(initial_state), no_precondition_actions, False)
    if relaxed_planning_problem is not None:
        return relaxed_planning_problem
    else:
        return math.inf


def ignore_delete_lists(initial_state, goal_state, actions):
    no_delete_list_actions = copy.deepcopy(actions)
    for action in no_delete_list_actions:
        action.delete_list = []
    relaxed_planning_problem = forward_search(copy.deepcopy(goal_state), copy.deepcopy(initial_state), no_delete_list_actions, False)
    if relaxed_planning_problem is not None:
        return relaxed_planning_problem
    else:
        return math.inf
