def show_case_1(x):
    if x > 0:
        print('x > 0')
    elif x == 0:
        print('x = 0')
    else:
        print('x < 0')


def show_case_2(x):
    if x > 0 and x < 10:
        print('x > 0 and x < 10')
    if 0 < x < 10:
        print('x > 0 and x < 10')


show_case_1(1)
show_case_1(-2)
show_case_1(0)
show_case_2(7)
