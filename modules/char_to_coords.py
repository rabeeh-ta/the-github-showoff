# ? change the given charector to the co-ord in matrix. a charector is represented using 5 rows and 4 columns.
def char_to_coords(ltr):
    ltr = ltr.upper()
    if('A' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),  (2, 1),
                (0, 2), (2, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3))  # column wise is done here
    elif('B' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),  (2, 1),
                (0, 2), (2, 2), (0, 3),  (1, 3), (2, 3), (3, 3), (4, 1), (4, 3), (4, 2))
    elif('C' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),
                (0, 2), (0, 3), (4, 1), (4, 3), (4, 2))
    elif('D' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),
                (0, 2), (1, 3), (2, 3), (3, 3), (4, 1), (4, 2))
    elif('E' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),
                (0, 2), (0, 3), (2, 1), (2, 2), (2, 3), (4, 1), (4, 3), (4, 2))
    elif('F' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),
                (0, 2), (0, 3), (2, 1), (2, 2), (2, 3))
    elif('G' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),
                (0, 2), (0, 3), (2, 2), (2, 3), (4, 1), (4, 2), (4, 3), (3, 3))
    elif('H' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 3), (2, 2),
                (2, 3), (4, 3), (2, 1), (3, 3), (1, 3))
    elif('I' == ltr):
        return ((0, 0), (0, 2), (0, 3), (4, 0), (0, 1),
                (1, 2), (2, 2), (3, 2), (4, 1), (4, 2), (4, 3),
                (1, 1), (2, 1), (3, 1))
    elif('J' == ltr):
        return ((0, 0), (3, 0), (4, 0), (0, 1),
                (0, 2), (0, 3), (1, 2), (2, 2), (3, 2), (4, 1), (4, 2))
    elif('K' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 3), (1, 2), (2, 1),
                (4, 3), (3, 2))
    elif('L' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
                (4, 1), (4, 3), (4, 2))
    elif('M' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0),
                (0, 3), (1, 3), (1, 1), (2, 3), (1, 2), (3, 3),
                (4, 0), (4, 3))
    elif('N' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0),
                (0, 3), (1, 3), (1, 1), (2, 2), (2, 3), (3, 3))
    elif('O' == ltr):
        return ((1, 0), (2, 0), (3, 0), (0, 1),
                (0, 2), (1, 3), (2, 3), (3, 3), (4, 1), (4, 2))
    elif('P' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
                (0, 1), (0, 2), (0, 3), (1, 3), (2, 1), (2, 2), (2, 3))
    elif('Q' == ltr):
        return ((1, 0), (2, 0), (3, 0), (0, 1),
                (0, 2), (1, 3), (2, 3), (3, 3), (4, 1), (4, 3), (3, 2))
    elif('R' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
                (0, 1), (0, 2), (0, 3), (1, 3), (2, 1), (2, 2),
                (3, 3), (4, 3))
    elif('S' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 3), (4, 0), (0, 1),
                (0, 2), (0, 3), (2, 1), (2, 2), (2, 3), (4, 1), (4, 3), (4, 2))
    elif('T' == ltr):
        return ((0, 0), (0, 2), (0, 3), (0, 1),
                (1, 2), (2, 2), (3, 2), (4, 1), (4, 2),
                (1, 1), (2, 1), (3, 1))
    elif('U' == ltr):
        return ((1, 0), (2, 0), (3, 0), (4, 0),
                (1, 3), (2, 3), (3, 3), (4, 1), (4, 2),
                (4, 3), (0, 0), (0, 3))
    elif('V' == ltr):
        return ((1, 0), (2, 0), (3, 0),
                (1, 3), (2, 3), (3, 3), (4, 1), (4, 2),
                (0, 0), (0, 3))
    elif('W' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0),
                (0, 3), (1, 3), (3, 1), (2, 3), (3, 2),
                (4, 0), (4, 3), (3, 3))
    elif('X' == ltr):
        return ((0, 0), (1, 3), (2, 1),
                (0, 3), (2, 2), (3, 0),
                (4, 0), (4, 3), (1, 0), (3, 3))
    elif('Y' == ltr):
        return ((1, 0), (2, 1), (3, 1),
                (1, 3), (2, 2), (3, 2), (4, 1), (4, 2),
                (0, 0), (0, 3))
    elif('Z' == ltr):
        return ((0, 0), (1, 2), (3, 1), (4, 0), (0, 1),
                (0, 2), (0, 3), (2, 1), (2, 2), (4, 1), (4, 3), (4, 2))
