
col = 10

col1 = [" " for i in range(1, col)]
col2 = [" " for i in range(1, col)]
col3 = [" " for i in range(1, col)]
col4 = [" " for i in range(1, col)]
col5 = [" " for i in range(1, col)]
col6 = [" " for i in range(1, col)]
col7 = [" " for i in range(1, col)]

mat = [col1, col2, col3, col4, col5, col6, col7]


def print_mat():
    for row in mat:
        print(row)


def draw_mat(ch):
    for (x, y) in ch:
        print(x, y)

    # print_mat()


def name_to_mat(ltr):
    if('A' == ltr):
        return


draw_mat((((0, 0), (1, 0), (2, 0), (3, 0), (4, 0)), ((0, 1), (), (2, 1), (), ()),
          ((0, 2), (), (2, 2), (), ()), ((0, 3), (1, 3), (2, 3), (3, 3), (4, 3))))
