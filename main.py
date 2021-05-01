"""
    !ROADMAP!
     complete the alphabets (refact to new file).
     new func for printing at most 10 letters in the matrix.
     algorithm to generate the dates from the matrix.
     get the git commit library or make one.
     generate standalone folder with all the git stuff ready to push.
"""
col = 52

col2 = [" " for i in range(0, col)]
col1 = [" " for i in range(0, col)]
col3 = [" " for i in range(0, col)]
col4 = [" " for i in range(0, col)]
col5 = [" " for i in range(0, col)]
col6 = [" " for i in range(0, col)]
col7 = [" " for i in range(0, col)]

mat = [col1, col2, col3, col4, col5, col6, col7]


# ? will print the matrix
def display_mat():
    for row in mat:
        print(row)


# ? for clearing the display while printing many charector one by one
def clear_display():
    for i in range(0, 7):
        for j in range(0, col):
            mat[i][j] = " "


# ? to print the matrix with out the arrays
def display():
    for row in mat:
        sttr = ""
        for elemnt in row:
            sttr = sttr + elemnt
        print(sttr)


# ? for drawing the individual co-ordinates.
def draw_mat(ch, pos=1):  # pos for which co-ord to start the letter
    # clear the display for each latter print > this is only for testing the letter
    # clear_display()
    for x, y in ch:
        mat[x + 1][pos + y] = "*"  # pos will leave the required space
    # display()  # display the matrix without arrays and quotes
    # display_mat()  # display the arrays which is the matrix


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
                (1,1), (2,1), (3,1))
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
                (0, 3), (1, 3), (1, 1), (2, 3), (1, 2), (3, 3))
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
                (0, 2), (1, 3), (2, 3), (3, 3), (4, 1), (4, 3), (3,2))
    elif('R' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
                (0, 1), (0, 2), (0, 3), (1, 3), (2, 1), (2, 2),
                (3,3), (4,3))
    elif('S' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 3), (4, 0), (0, 1),
                (0, 2), (0, 3), (2, 1), (2, 2), (2, 3), (4, 1), (4, 3), (4, 2))
    elif('T' == ltr):
        return ((0, 0), (0, 2), (0, 3), (0, 1),
                (1, 2), (2, 2), (3, 2), (4, 1), (4, 2),
                (1,1), (2,1), (3,1))
    elif('U' == ltr):
        return ((1, 0), (2, 0), (3, 0), (4,0),
                (1, 3), (2, 3), (3, 3), (4, 1), (4, 2),
                (4,3), (0,0), (0,3))
    elif('V' == ltr):
        return ((1, 0), (2, 0), (3, 0),
                (1, 3), (2, 3), (3, 3), (4, 1), (4, 2),
                (0,0), (0,3))
    elif('W' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0),
                (0, 3), (1, 3), (3, 1), (2, 3), (3, 2),
                (4,0), (4,3), (3, 3))
    elif('X' == ltr):
        return ((0, 0), (1, 3), (2, 1),
                (0, 3), (2, 2), (3,0),
                (4,0), (4,3), (1,0), (3,3))
    elif('Y' == ltr):
        return ((1, 0), (2, 1), (3, 1),
                (1, 3), (2, 2), (3, 2), (4, 1), (4, 2),
                (0,0), (0,3))
    elif('Z' == ltr):
        return ((0, 0), (1, 2),(3, 1), (4, 0), (0, 1),
                (0, 2), (0, 3), (2, 1), (2, 2), (4, 1), (4, 3), (4, 2))


string = "abcdefghijklmnop"

# loop though the string and print every letter
for l in string:
    char_code = char_to_coords(l)
    draw_mat(char_code)

#char_code = char_to_coords("z")
#draw_mat(char_code)
name = "DOG"

# ? PRINT => all char in one matrix
# if len(name) <= 10:
#     for indx, l in enumerate(name):
#         pos = (indx * 5)
#         char_code = char_to_coords(l)
#         draw_mat(char_code, pos)
#     display()
# else:
#     print("string should be 10 or less")

# ? PRINT => all char diff matrix
# for l in string:
#     clear_display()
#     char_code = char_to_coords(l)
#     draw_mat(char_code)
#     display()

# ? PRINT => one letter in one matrix
char_code = char_to_coords("d")
draw_mat(char_code)
display()
