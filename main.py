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
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),  (2, 1),
               (0, 2), (2, 2), (0, 3),  (1, 3), (2, 3), (3, 3), (4, 1), (4, 3), (4, 2))
    elif('C' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),
               (0, 2), (0, 3), (4, 1), (4, 3), (4, 2))
    elif('D' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1),
               (0, 2), (0, 3), (1, 3), (2, 3), (3, 3),(4, 1), (4, 3), (4, 2))           
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
         (2, 3), (4, 3), (2, 1), (1, 3))  
    elif('I' == ltr):
        return ((0, 0), (0, 2), (0, 3), (4, 0), (0, 1),
                (1, 2), (2, 2), (3, 2), (4, 1), (4, 2), (4, 3))                           
    elif('J' == ltr):
        return ((0, 0), (3, 0), (4, 0), (0, 1),
               (0, 2), (0, 3),(1, 2), (2, 2), (3, 2), (4, 1), (4, 2))    
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
        return ( (1, 0), (2, 0), (3, 0), (0, 1),
               (0, 2), (1, 3), (2, 3), (3, 3),(4, 1), (4, 2))  
    elif('P' == ltr):
        return ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (0, 2), (0,3), (1, 3), (2, 1),(2, 2), (2, 3))               
                              
                                 



matrix_code = name_to_mat("a")
matrix_code = name_to_mat("b")
matrix_code = name_to_mat("c")
matrix_code = name_to_mat("o")
matrix_code = name_to_mat("e")
matrix_code = name_to_mat("f")
matrix_code = name_to_mat("g")
matrix_code = name_to_mat("h")
matrix_code = name_to_mat("i")
matrix_code = name_to_mat("j")
matrix_code = name_to_mat("k")
matrix_code = name_to_mat("l")
matrix_code = name_to_mat("m")
matrix_code = name_to_mat("n")
matrix_code = name_to_mat("o")
matrix_code = name_to_mat("p")





draw_mat(matrix_code)