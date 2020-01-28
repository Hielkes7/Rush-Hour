def state_space1(D, N):
    """
        Method 1: Een auto kan nooit van baan wisselen. Dus een auto kan op 5 plekken
        staan in een 6x6 grid. Hier houden we geen rekening met het blokkeren door andere
        auto's. Elke auto kan op elke plek van zijn baan staan. De state space van deze
        redenering is dus:
        S = (D - 1)^N
        Met S de state space, D dimensie van de grid, N het aantal auto's
    """
    S = (D - 1)**N
    return S
def state_space2_6x6(A, B, C, D, E):
    """
        Methode 2 - Recognizing rows:
        * A: 6x6 row with 1 car:           S = 5 states
        * B: 6x6 row with 2 cars:          S = 6
        * C: 6x6 row with 1 truck & 1 car: S = 3
        * D: 6x6 row with 1 truck:         S = 4
        * E: no car of truck:              S = 1

        The state space of a 6x6 grid a combination of any of the above options.
        Sidenote: when a horizontal row has a vertical car in it, I won't count
        that car, as it can be moved away.
        Sidenote2: A + B + C + D + E = all rows = 6 + 6 = 12 (for a 6x6 grid)
    """
    state_space = 5**A * 6**B * 3**C * 4**D
    number_of_cars = A*1 + B*2 + C*2 + D*1
    if A + B + C + D + E == 12:
        return state_space, number_of_cars
    else:
        return "Error, not all rows are included"
def state_space2_9x9(A, B, C, D, E, F, G, H, I):
    """
        Methode 2 - Recognizing rows in 9x9 grid:
        * A: row with 1 car:            S = 8 states
        * B: row with 2 cars:           S = 21
        * C: row with 3 cars:           S = 20
        * D: row with 4 cars:           S = 5
        * E: row with 1 truck:          S = 7
        * F: row with 2 trucks:         S = 10
        * G: row with 2 cars, 1 truck:  S = 10
        * H: row with 1 car, 1 truck:   S = 15
        * I: empty row:                 S = 1

        The state space of a 9x9 grid a combination of any of the above options.
        Sidenote: when a horizontal row has a vertical car in it, I won't count
        that car, as it can be moved away.
        Sidenote2: A + B + C + D + E + F + G + H + I = 18 (all lanes)
    """
    state_space = 8**A * 21**B * 20**C * 5**D * 7**E * 10**F * 10**G * 15**H
    number_of_cars = A*1 + B*2 + C*3 + D*4 + E*1 + F*2 + G*3 + H*2
    if A + B + C + D + E + F + G + H + I == 18:
        return state_space, number_of_cars
    else:
        return "Error, not all rows are included"
def state_space2_12x12(A, B, C, D, E, F, G, H, I, J):
    """
        Methode 2 - Recognizing rows in 12x12 grid:
        * A: row with 1 car:            S = 11 states
        * B: row with 2 cars:           S = 45
        * C: row with 3 cars:           S = 84
        * D: row with 1 truck:          S = 10
        * E: row with 2 truck:          S = 28
        * F: row with 1 cars, 1 truck:  S = 36
        * G: row with 2 cars, 1 truck:  S = 56
        * H: row with 1 car, 2 trucks:  S = 35
        * I: row with 3 trucks, 1 car:  S = 5
        * J: empty row                  S = 1

        The state space of a 9x9 grid a combination of any of the above options.
        Sidenote: when a horizontal row has a vertical car in it, I won't count
        that car, as it can be moved away.
        Sidenote2: A + B + C + D + E + F + G + H + I + J= 24 (all lanes)
    """
    state_space = 11**A * 45**B * 84**C * 10**D * 28**E * 36**F * 56**G * 35**H * I**5
    number_of_cars = A*1 + B*2 + C*3 + D*1 + E*2 + F*2 + G*3 + H*3 + I*4
    if A + B + C + D + E + F + G + H + I + J == 24:
        return state_space, number_of_cars
    else:
        return "Error, not all rows are included"


# method 1, game 1
dimentions = 12
cars = 44
# print(state_space1(dimentions, cars))

# method 2, game 1
A = 5
B = 4
C = 0
D = 0
E = 3
# print(state_space2_6x6(A, B, C, D, E))

# method 2, game 2
A = 6
B = 3
C = 0
D = 1
E = 2
# print(state_space2_6x6(A, B, C, D, E))

# method 2, game 3
A = 6
B = 0
C = 0
D = 3
E = 3
# print(state_space2_6x6(A, B, C, D, E))

# method 3, game 4
A = 2
B = 1
C = 1
D = 0
E = 5
F = 1
G = 2
H = 1
I = 5
# print(state_space2_9x9(A, B, C, D, E, F, G, H, I))

# method 3, game 5
A = 6
B = 4
C = 0
D = 0
E = 2
F = 0
G = 0
H = 4
I = 2
# print(state_space2_9x9(A, B, C, D, E, F, G, H, I))

# method 3, game 6
A = 5
B = 4
C = 0
D = 0
E = 4
F = 0
G = 1
H = 3
I = 1
# print(state_space2_9x9(A, B, C, D, E, F, G, H, I))

# method 3, game 6
A = 5
B = 2
C = 2
D = 1
E = 1
F = 5
G = 3
H = 1
I = 1
J = 3
print(state_space2_12x12(A, B, C, D, E, F, G, H, I, J))
