#matrix prgm
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


def print_mat():
    for row in mat:
        print(row)

# to print the matrix with out the arrays


def print_plain_mat():
    for row in mat:
        sttr = ''
        for elemnt in row:
            sttr = sttr + elemnt
        print(sttr)


# for drawing the individual co-ordinates.
def draw_mat(ch):
    for x, y in ch:
        mat[x+1][y+1] = '*'
    print_plain_mat()
    print_mat()


# change the given charector to the co-ord in matrix
# a charector is represented using 5 rows and 4 columns.
def name_to_mat(ltr):
    ltr = ltr.upper()
    if('A' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),  (2, 1),
                (0, 2), (2, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3))  # column wise is done here
    elif('B' == ltr):
        return ((0,0), (1,0),())


matrix_code = name_to_mat("a")

draw_mat(matrix_code)
