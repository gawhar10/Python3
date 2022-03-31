"""
Round parenthesis checking program.
"""


def check_para(mystr):
    """
    method to check parenthesis.
    """
    open_para = []
    close_para = []
    for i in range(0, len(mystr)):
        mylist = mystr[i]
        if mylist == '(':
            open_para = open_para + ['(']
        else:
            if mylist == ')':
                close_para = close_para + [')']
            else:
                return (open_para, close_para)

    if len(open_para) == len(close_para):
        print('pair:', len(open_para))
    else:
        print('unpair')


# my_str = ['(', ')', '(', ')', ')']
my_str = str(input('Enter: '))
check_para(my_str)
