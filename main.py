from modules.char_to_coords import char_to_coords


"""
        !ROADMAP!
    [*] complete the alphabets (refact to new file).
    [*] new func for printing at most 10 letters in the matrix.
    [ ] algorithm to generate the dates from the matrix.
    [ ] get the git commit library or make one.
    [ ] generate standalone folder with all the git stuff ready to push.
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
def draw_mat(ch, pos=1):  # if no poss passed then start from 1st co ord
    for x, y in ch:
        # pos will leave the required space so that letters will not get printed on top of each other
        mat[x + 1][pos + y] = "*"


string = "abcdefghijklmnop"
name = "rabeeh"

# ? PRINT => all char in one matrix
# if len(name) <= 10:
#     for indx, l in enumerate(name):
#         # finding where should the letter come on the matrix. 5 => 4 columns of letter + 1 space
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
char_code = char_to_coords("z")
draw_mat(char_code)
display()
