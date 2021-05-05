from datetime import date, timedelta
from modules.char_to_coords import char_to_coords
import os

"""
        !ROADMAP!
    [*] complete the alphabets (refact to new file).
    [*] new func for printing at most 10 letters in the matrix.
    [*] algorithm to generate the dates from the matrix.
    [*] get the git commit library or make one.
    [*] generate standalone folder with all the git stuff ready to push.
    [ ] write a good readme add some screenshots. 
"""


col = 52
#! this looks ugly should do some thing or take it to other file
matCol1 = [" " for i in range(0, col)]
matCol2 = [" " for i in range(0, col)]
matCol3 = [" " for i in range(0, col)]
matCol4 = [" " for i in range(0, col)]
matCol5 = [" " for i in range(0, col)]
matCol6 = [" " for i in range(0, col)]
matCol7 = [" " for i in range(0, col)]

mat_Date_Col1 = [" " for i in range(0, col)]
mat_Date_Col2 = [" " for i in range(0, col)]
mat_Date_Col3 = [" " for i in range(0, col)]
mat_Date_Col4 = [" " for i in range(0, col)]
mat_Date_Col5 = [" " for i in range(0, col)]
mat_Date_Col6 = [" " for i in range(0, col)]
mat_Date_Col7 = [" " for i in range(0, col)]

mat = [matCol1, matCol2, matCol3, matCol4, matCol5,
       matCol6, matCol7]  # mat for drawing the stars
matDates = [mat_Date_Col1, mat_Date_Col2, mat_Date_Col3,
            mat_Date_Col4, mat_Date_Col5, mat_Date_Col6, mat_Date_Col7]  # a reference calender
commitDates = []  # the final dates to do the commits


# ? to print the matrix with out the arrays
def display(mat):
    for row in mat:
        sttr = ""
        for elemnt in row:
            sttr = sttr + elemnt
        print(sttr)


# ? will print the matrix
def display_mat(mat):
    for row in mat:
        print(row)


# ? for clearing the display while printing many charector one by one
def clear_display(mat):
    for i in range(0, 7):
        for j in range(0, col):
            mat[i][j] = " "


# ? for drawing the individual co-ordinates.
def draw_mat(ch, pos=1):  # if no poss passed then start from 1st co ord
    for x, y in ch:
        # pos will leave the required space so that letters will not get printed on top of each other
        spaceInFront = 1
        # to add more space in front ie, number of row to leave at the start change the spaceInFront
        mat[x + 1][pos + y + spaceInFront] = "*"


# ? function takes a matrix and year => generates all the dates from JAN to DEC and returns the array
def mat_dates_gen(year, matDates):
    commitDate = date(year, 1, 1)

    # ! find the starting day of the week
    if commitDate.weekday() == 6:  # python-date-module week starts from monday. On github it starts from sunday so correcting
        weekStart = 0
    else:
        # monday will return 0 so plus 1 will make it in the second row
        weekStart = (commitDate.weekday() + 1)

    for y in range(0, 52):
        for x in range(weekStart, 7):
            matDates[x][y] = commitDate  # for testing purpose
            commitDate += timedelta(days=1)
            weekStart = 0  # reset for everyother week

    return matDates


# ? Func loops through the array and find for * if found then will take the co-ord and will get the corresponding date from the OTHER matrix
def get_dates(mat, matDates, commitDates):
    matDates = mat_dates_gen(2020, matDates)  # making the OTHER matrix

    for y in range(0, 52):
        for x in range(0, 7):
            if mat[x][y] == "*":  # check
                # get the corresponding date
                commitDates.append(matDates[x][y])
    return commitDates


# ? Will create a new folder and commit there with the passed dates
def doTheCommit(commitDates):
    workingDir = os.getcwd()

    os.system("mkdir showoff")
    os.chdir(workingDir+"/showoff")
    os.system("git init")
    for i in commitDates:
        txt = open("text.txt", "w")
        txt.write(f"{i}")
        txt.close()
        os.system("git add .")
        os.system(f"git commit -m {i} --date {i}")


string = "abcdefghijklmnopqrstuvwxyz"
name = "helloworld"


# ? PRINT => all char in one matrix
if len(name) <= 10:
    for indx, l in enumerate(name):
        # finding where should the letter come on the matrix. 5 => 4 columns of letter + 1 space
        pos = (indx * 5)
        char_code = char_to_coords(l)
        draw_mat(char_code, pos)
    display(mat)
else:
    print("string should be 10 or less")


# ? PRINT => all char diff matrix
# for l in string:
#     clear_display(mat)
#     char_code = char_to_coords(l)
#     draw_mat(char_code)
#     display(mat)


# ? PRINT => one letter in one matrix
# char_code = char_to_coords("z")
# draw_mat(char_code)
# display(mat)


# ? puting everything together
# commitDates array have the individual dates from all the * spots
commitDates = get_dates(mat, matDates, commitDates)
# print(len(commitDates))
# print(commitDates)
# doTheCommit(commitDates)
