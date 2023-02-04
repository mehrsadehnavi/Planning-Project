from Action import Action
from State import State


def depot_domain_problem():
    initial_state = State(None, None, positive_literals=["atP0D0", "clearC0", "atP1D0", "clearC3", "atP2D1", "clearC2",
                                                         "atT0D0", "atT1D0", "atH0D0", "availableH0", "atH1D0", "availableH1",
                                                         "atH2D1", "availableH2", "atC0D0", "onC0P0", "atC1D1", "onC1P1",
                                                         "atC2D1", "onC2C1", "atC3D0", "onC3P1"],
                          negative_literals=["clearD0", "clearD1", "clearP0", "clearP1"])
    goal_state = State(None, None, positive_literals=["onC0P2", "onC1P3", "onC2P0", "onC3P1"], negative_literals=["clearD0", "clearD1", "clearP0", "clearP1"])

    actions = []
    Depot = ["D0", "D1"]
    #   Distributor = ["distributor0", "distributor1"]
    Truck = ["T0", "T1"]
    Pallet = ["P0", "P1", "P2"]
    Crate = ["C0", "C1", "C2", "C3"]
    Hoist = ["H0", "H1", "H2"]
    Surface = ["S0", "S1", "S2"]

    # Drive
    for t in Truck:
        for d1 in Depot:
            for d2 in Depot:
                for p in Pallet:
                    for c in Crate:
                        if d1 != d2:
                            drive_action = Action(name="drive" + t + d1 + d2 + c + p,
                                                  positive_preconditions=["at" + c + d1, "at" + t + d1, "clear" + d2,
                                                                          "at" + p + d1, "on" + c + p],
                                                  negative_preconditions=[],
                                                  add_list=["at" + c + d2, "at" + p + d2],
                                                  delete_list=["clear" + d2, "at" + c + d1, "at" + p + d1])
                            actions.append(drive_action)

    # Load
    for h in Hoist:
        for c in Crate:
            for t in Truck:
                for d in Depot:
                    for p in Pallet:
                        load_action = Action(name="load" + h + c + t + d + p,
                                             positive_preconditions=["at" + h + d, "at" + t + d, "lifting" + h + c,
                                                                     "at" + c + d, "clear" + t, "at" + p + d,
                                                                     "on" + c + p],
                                             negative_preconditions=[],
                                             add_list=["in" + c + t, "available" + h, "dropping" + h + c, "in" + p + t],
                                             delete_list=["at" + c + d, "lifting" + h + c, "at" + p + d])
                        actions.append(load_action)

    # Unload
    for h in Hoist:
        for c in Crate:
            for t in Truck:
                for d in Depot:
                    for p in Pallet:
                        unload_action = Action(name="unload" + h + c + t + d + p,
                                               positive_preconditions=["at" + h + d, "at" + t + d,
                                                                       "available" + h, "in" + c + t, "in" + p + t,
                                                                       "on" + c + p],
                                               negative_preconditions=[],
                                               add_list=["at" + c + d, "lifting" + h + c, "at" + p + d],
                                               delete_list=["in" + c + t, "available" + h])
                        actions.append(unload_action)

    # Lift
    for h in Hoist:
        for c in Crate:
            for p in Pallet:
                for d in Depot:
                    for s in Surface:
                        lift_action = Action(name="lift" + h + c + p + d,
                                             positive_preconditions=["at" + h + d, "available" + h, "at" + c + d,
                                                                     "at" + p + d, "on" + c + s, "on" + p + s],
                                             negative_preconditions=[],
                                             add_list=["lifting" + h + c, "lifting" + h + p, "on" + c + h, "on" + p + h,
                                                       "clear" + s],
                                             delete_list=["at" + p + d, "at" + c + d, "on" + c + s, "clear" + p + s])
                        actions.append(lift_action)

    # Drop
    for h in Hoist:
        for c in Crate:
            for s in Surface:
                for p in Pallet:
                    for d in Depot:
                        drop_action = Action(name="drop" + h + c + s + p + d,
                                             positive_preconditions=["at" + h + d, "at" + s + d, "clear" + s,
                                                                     "lifting" + h + c],
                                             negative_preconditions=[],
                                             add_list=["available" + h, "dropping" + h + c, "at" + c + d, "at" + p + d,
                                                       "clear" + c, "clear" + p, "on" + c + s, "on" + p + s],
                                             delete_list=["clear" + s, "lifting" + h + c])
                        actions.append(drop_action)
    return [initial_state, goal_state, actions]
