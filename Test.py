import time
from ForwardSearch import forward_search
from BackwardSearch import backward_search
from tireproblem import tire_problem
from DepotDomain import depot_domain_problem
from BlockWorldProblem import block_world_problem
from monkeyAndBananas import monkey_bananas_problem


def main():
    print("Enter number of problem that you want.")
    print("1. Tire problem")
    print("2. Block world problem")
    print("3. Monkey bananas problem")
    print("4. Depot Domain Problem")

    n = int(input())
    if n == 1:
        initial_state, goal_state, actions = tire_problem()
    elif n == 2:
        initial_state, goal_state, actions = block_world_problem()
    elif n == 3:
        initial_state, goal_state, actions = monkey_bananas_problem()
    else:
        initial_state, goal_state, actions = depot_domain_problem()

    print("Choose between backward and forward search")
    print("1. Backward")
    print("2. Forward")

    n = int(input())
    if n == 1:
        start_time = time.time()
        print('Backward Search Answer:')
        backward_search(goal_state, initial_state, actions, True)
        print("--- %s seconds ---\n" % (time.time() - start_time))
    else:
        start_time = time.time()
        print('Forward Search Answer:')
        forward_search(goal_state, initial_state, actions, True)
        print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
