from Action import Action
from State import State


def monkey_bananas_problem():
    initial_state = State(None, None,
                          positive_literals=["atmonkeyA", "atbananasB", "atboxC", "heightmonkeylow", "heightboxlow",
                                             "heigthbananashigh", "pushablebox", "climbablebox", "graspablebananas"],

                          negative_literals=["equalAB", "equalAC", "equalBA", "equalBC", "equalCA", "equalCB"])

    goal_state = State(None, None, positive_literals=["havemonkeybananas"], negative_literals=[])

    actions = []
    locations = ["x", "y"]
    heights = ["low", "high"]
    objects = ["monkey", "bananas"]

    for loc in locations:
        for loc2 in locations:
            if loc != loc2:
                go_action = Action(name="go" + loc + loc2,
                                   positive_preconditions=["at" + "monkey" + loc, "height" + "monkey" + "low"],
                                   negative_preconditions=[],
                                   add_list=["at" + "monkey" + loc2],
                                   delete_list=["at" + "monkey" + loc])
                actions.append(go_action)

    for loc in locations:
        for loc2 in locations:
            for obj in objects:
                if loc != loc2:
                    push_action = Action(name="push" + obj + loc + loc2,
                                         positive_preconditions=["at" + "monkey" + loc, "height" + "monkey" + "low",
                                                                 "at" + obj + loc, "pushable" + obj, "height" + obj + "low"],
                                         negative_preconditions=["equal" + loc + loc2],
                                         add_list=["at" + "monkey" + loc, "at" + "monkey" + loc2],
                                         delete_list=["at" + obj + loc, "at" + "monkey" + loc])
                    actions.append(push_action)

    for loc in locations:
        for obj in objects:
            climb_action = Action(name="climb" + loc + obj,
                                  positive_preconditions=["at" + "monkey" + loc, "height" + "monkey" + "low",
                                                          "at" + obj + loc, "climbable" + obj, "height" + obj + "low"],
                                  negative_preconditions=[],
                                  add_list=["on" + "monkey" + obj, "height" + "monkey" + "high"],
                                  delete_list=["height" + "monkey" + "low"])
            actions.append(climb_action)

    for loc in locations:
        for obj in objects:
            for height in heights:
                grasp_action = Action(name="grasp" + loc + obj + height,
                                      positive_preconditions=["at" + "monkey" + loc, "height" + "monkey" + height,
                                                              "at" + obj + loc, "graspable" + obj, "height" + obj + height],
                                      negative_preconditions=[],
                                      add_list=["have" + "monkey" + obj],
                                      delete_list=["at" + obj + loc, "height" + obj + height])
                actions.append(grasp_action)

    return [initial_state, goal_state, actions]
