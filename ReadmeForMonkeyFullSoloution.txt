Definition
items = [monkey, banana, box]
positions = [0, 1, 2]
OPERATORS
Move(subject, x1, x2)
PC: monkeyAt(x1), monkeyLevelDown
A: monkeyAt(x2)
D: monkeyAt(x1)
PushBox(x1,x2)
PC: monkeyAt(x1), boxAt(x1), monkeyLevelDown
A: monkeyAt(x2), boxAt(x2)
D: monkeyAt(x1), boxAt(x1)
ClimbBox(x, direction={Up, Down})
PC: monkeyAt(x), boxAt(x), monkeyLevelDown
A: monkeyLevelUp
E: monkeyLevelDown
HaveBanana(x)
PC: monkeyAt(x), bananaAt(x), boxAt(x), monkeyLevelUp
A: GetBananaAt(x)
INITIAL STATE - Properties
monkeyAt0, monkeyLevelDown, bananaAt1, boxAt2
GOAL STATE - Properties
GetBanana(at 1)
