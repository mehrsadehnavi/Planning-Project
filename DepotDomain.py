from Action import Action
from State import State

initial_state = State(None, None, positive_literals=["atP0D0", "clearC0", "atP1D0", "clearC3", "atP2D1", "clearC2",
                                                     "atT0D0", "atT1D0", "atH0D0", "availableH0", "atH1D0", "availableH1",
                                                     "atH2D1", "availableH2", "atC0D0", "onC0P0", "atC1D1", "onC1P1",
                                                     "atC2D1", "onC2C1", "atC3D0", "onC3P1"],
                      negative_literals=["clearP0", "clearD0", ""])
goal_state = State(None, None, positive_literals=["onC0P2", "onC1P3", "onC2P0", "onC3P1"])

def get_actions():
    actions = []
    Depot = ["depot"]
#   Distributor = ["distributor0", "distributor1"]
    Truck = ["truck0", "truck1"]
    Pallet = ["pallet0", "pallet1"]
    Crate = ["crate0", "crate1", "crate2", "crate3"]
    Hoist = ["hoist0", "hoist1", "hoist2"]
    Surface = ["surface"]

    #Drive
    for t in Truck:
        for d1 in Depot:
            for d2 in Depot:
                for p in Pallet:
                    for c in Crate:
                        if d1 != d2:
                            drive_action = Action(name="drive" + t + d1 + d2 + c + p,
                                                  positive_preconditions=["at" + d1 + c, "at" + d1 + t, "clear" + d2,
                                                                          "at" + d1 + p, "in" + c + p],
                                                  negative_preconditions=[],
                                                  add_list=["at" + d2 + c, "at" + d2 + p],
                                                  delete_list=["clear" + d2, "at" + d1 + c, "at" + d1 + p])
                        actions.append(put_action)


    #Load
    for h in Hoist:
        for c in Crate:
            for t in Truck:
                for d in Depot:
                    for p in Pallet:
                        load_action = Action(name="load" + h + c + t + d + p,
                                             positive_preconditions=["at" + d + h, "at" + d + t, "lifting" + h + c,
                                                                     "at" + d + c, "clear" + t, "at" + d + p,
                                                                     "in" + c + p],
                                             negative_preconditions=[],
                                             add_list=["in" + c + t, "available" + h, "dropping" + h + c, "in" + p + t],
                                             delete_list=["at" + d + c, "lifting" + h + c, "at" + d + p])
                        actions.append(put_action)


    #Unload
    for h in Hoist:
        for c in Crate:
            for t in Truck:
                for d in Depot:
                    for p in Pallet:
                        unload_action = Action(name="unload" + h + c + t + d + p,
                                               positive_preconditions=["at" + d + h, "at" + d + t,
                                                                       "available" + h, "in" + c + t, + "in" + p + t,
                                                                       "in" + c + p],
                                               negative_preconditions=[],
                                               add_list=["at" + d + c, "lifting" + h + c, "at" + d + p],
                                               delete_list=["in" + c + t, "available" + h])
                        actions.append(put_action)


    #Lift
    for h in Hoist:
        for c in Crate:
            for p in Pallet:
                for d in Depot:
                    for s in Surface:
                        lift_action = Action(name="lift" + h + c + p + d,
                                             positive_preconditions=["at" + d + h, "available" + h, "at" + d + c,
                                                                     "at" + d + p, "on" + c + s, "on" + p + s],
                                             negative_preconditions=[],
                                             add_list=["lifting" + h + c, "lifting" + h + p, "on" + c + h, "on" + p + h,
                                                       "clear" + s],
                                             delete_list=["at" + d + p, "at" + d + c, "on" + c + s, "clear" + p + s])
                        actions.append(put_action)


    #Drop
    for h in Hoist:
        for c in Crate:
            for s in Surface:
                for p in Pallet:
                    for d in Depot:
                        drop_action = Action(name="drop" + h + c + s + p + d,
                                             positive_preconditions=["at" + d + h,"at" + d + s, "clear" + s,
                                                                     "lifting" + h + c],
                                             negative_preconditions=[],
                                             add_list=["available" + h, "dropping" + h + c, "at" + d + c, "at" + d + p,
                                                       "clear" + c, "clear" + p, "on" + c + s, "on" + p + s],
                                             delete_list=["clear" + s, "lifting" + h + c])
                        actions.append(put_action)
