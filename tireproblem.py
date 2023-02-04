from Action import Action
from State import State


def tire_problem():
    initial_state = State(None, None, positive_literals=["atflataxle", "atsparetrunk"],
                          negative_literals=['atflatground', 'atflattrunk', 'atspareground', 'atspareaxle'])
    goal_state = State(None, None, positive_literals=["atspareaxle", 'atflatground'],
                       negative_literals=['atspareground', 'atsparetrunk', 'atflataxle', 'atflattrunk'])
    actions = []
    tires = ["spare", "flat"]
    locations = ["axle", "trunk"]

    for tire in tires:
        put_action = Action(name="put" + tire + "axle", positive_preconditions=["at" + tire + "ground"], negative_preconditions=["atflataxle", "atspareaxle"],
                            add_list=["at" + tire + "axle"], delete_list=["at" + tire + "ground"])
        actions.append(put_action)
        for location in locations:
            remove_action = Action(name="rem" + tire + location, positive_preconditions=["at" + tire + location], negative_preconditions=[],
                                   add_list=["at" + tire + "ground"], delete_list=["at" + tire + location])
            actions.append(remove_action)

    return [initial_state, goal_state, actions]
