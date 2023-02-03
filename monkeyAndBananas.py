from Action import Action
from State import State

initial_state = State(None, None, positive_literals=["atmonkeyA", "atbananasB", "atboxC", "hightmonkeylow",
                                                     "heightboxlow", "heigthbananashigh","pushablebox",
                                                     "climbablebox", "graspablebananas"],
                      negative_literals=["equalAB", "equalAC", "equalBA",
                                         "equalBC", "equalCA", "equalCB"])

goal_state = State(None, None, positive_literals=["havemonkeybananas"],
                   negative_literals=[])

def get_actions():
    actions = []
    locations = ["x", "y"]
    heights = ["low", "high"]
    bs = []

    for loc in locations:
        for loc2 in locations:
            if loc != loc2:
                go_action = Action(name="go" + loc + loc2,
                             positive_preconditions=["at" + "monkey" + loc,
                                                     "hight" + "monkey" + "low"],
                             negative_preconditions=[],
                             add_list=["at" + "monkey" + loc2],
                             delete_list=["at" + "monkey", + loc])
            actions.append(put_action)

    for loc in locations:
        for loc2 in locations:
            for b in bs:
                if loc != loc2:
                    push_action = Action(name="push" + b + loc + loc2,
                                                  positive_preconditions=["at" + "monkey" + loc,
                                                                          "height" + "monkey" + "low",
                                                                          "at" + b + loc,
                                                                          "pushable" + b,
                                                                          "height" + b + "low"],
                                                  negative_preconditions=["equal"+ loc + loc2],
                                                  add_list=["at" + "monkey" + loc,
                                                            "at" + "monkey" + loc2],
                                                  delete_list=["at" + b + loc,
                                                               "at" + "monkey" + loc])
                actions.append(move_to_table_action)

    for loc in locations:
        for b in bs:
            climb_action = Action(name="climb" + loc + b,
                                 positive_preconditions=["at" + "monkey" + loc,
                                                         "height" + "monkey" + "low",
                                                         "at" + b + loc,
                                                         "climbable" + b,
                                                         "height" + b + "low"],
                                 negative_preconditions=[],
                                 add_list=["on" + "monkey" + b,
                                           "height" + "monkey" + "high"],
                                 delete_list=["height" + "monkey" + "low"])
            actions.append(move_to_table_action)


    for loc in locations:
        for b in bs:
            for height in heights:
                grasp_action = Action(name = "grasp" + loc + b + height,
                                              positive_preconditions=["at" + "monkey" + loc,
                                                                      "height" + "monkey" + height,
                                                                      "at" + b + loc,
                                                                      "graspable" + b,
                                                                      "height" + b + height],
                                              negative_preconditions=[],
                                              add_list=["have" + "monkey" + b],
                                              delete_list=["at" + b + loc,
                                                           "height" + b + height])
                actions.append(move_to_table_action)



    return actions
