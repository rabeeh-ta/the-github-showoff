"""
     i will start from z you come from A we meet at middle
"""
col = 10

col1 = [" " for i in range(1, col)]
col2 = [" " for i in range(1, col)]
col3 = [" " for i in range(1, col)]
col4 = [" " for i in range(1, col)]
col5 = [" " for i in range(1, col)]
col6 = [" " for i in range(1, col)]
col7 = [" " for i in range(1, col)]

mat = [col1, col2, col3, col4, col5, col6, col7]

# will print the matrix


def display_mat():
    for row in mat:
        print(row)


# to print the matrix with out the arrays
def display():
    for row in mat:
        sttr = ''
        for elemnt in row:
            sttr = sttr + elemnt
        print(sttr)


# for drawing the individual co-ordinates.
def draw_mat(ch):
    for x, y in ch:
        mat[x+1][y+1] = '*'
    display()
    # display_mat()


# change the given charector to the co-ord in matrix
# a charector is represented using 5 rows and 4 columns.
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
                (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 1), (4, 3), (4, 2))
    elif('E' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),
                (0, 2), (0, 3), (2, 1), (2, 2), (2, 3), (4, 1), (4, 3), (4, 2))
    elif('F' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),
                (0, 2), (0, 3), (2, 1), (2, 2), (2, 3))
    elif('G' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),
                (0, 2), (0, 3), (2, 2), (2, 3), (4, 1), (4, 2), (4, 3))
    elif('H' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 3), (2, 2),
                (2, 3), (4, 3), (2, 1), (3, 3), (1, 3))
    elif('I' == ltr):
        return ((0, 0), (0, 2), (0, 3), (4, 0), (0, 1),
                (1, 2), (2, 2), (3, 2), (4, 1), (4, 2), (4, 3))
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
        return ((0, 0), (1, 0), (2, 0), (3, 0), (0, 4),
                (0, 3), (1, 3), (1, 1), (2, 3), (2, 2), (3, 3), (4, 3))
    elif('N' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0),
                (0, 3), (1, 3), (1, 1), (2, 2), (2, 3), (3, 3))
    elif('O' == ltr):
        return ((1, 0), (2, 0), (3, 0), (0, 1),
                (0, 2), (1, 3), (2, 3), (3, 3), (4, 1), (4, 2))
    elif('P' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
                (0, 1), (0, 2), (0, 3), (1, 3), (2, 1), (2, 2), (2, 3))


char_code = char_to_coords("c")
draw_mat(char_code)
