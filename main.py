
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


def print_plain_mat():
    for row in mat:
        for element in row:
            print(element)
        print('/n')

# for drawing the individual co-ordinates.


def draw_mat(ch):
    for x, y in ch:
        mat[x][y] = '@'
    print_plain_mat()

# change the given charector to the co-ord in matrix
# a charector is represented useing 5 rows and 4 columns.


def name_to_mat(ltr):
    if('A' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),  (2, 1),
                (0, 2), (2, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3))  # column wise is done here


draw_mat(((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),  (2, 1),
          (0, 2), (2, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3)))
