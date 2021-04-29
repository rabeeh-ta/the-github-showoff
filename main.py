
col1 = ["" for i in range(1, 53)]
col2 = ["" for i in range(1, 53)]
col3 = ["" for i in range(1, 53)]
col4 = ["" for i in range(1, 53)]
col5 = ["" for i in range(1, 53)]
col6 = ["" for i in range(1, 53)]
col7 = ["" for i in range(1, 53)]

mat = [col1, col2, col3, col4, col5, col6, col7]


def print_mat():
    for row in mat:
        print(row)


def draw_mat(x, y):
    print(f"row: {x} , column: {y}")
    mat[x][y] = "*"

    print_mat()


draw_mat(0, 0)
