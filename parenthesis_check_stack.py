"""
parenthesis check using stack.
checks pair
checks count of parenthesis.
"""


def check_para(mystr):
    """
    method to check parenthesis.
    """
    mylist = []
    pair = 0
    for i in mystr:
        if i == "(":
            mylist.append(i)
        elif i == ")":
            mycount = mylist.count('(')
            if mycount > 0:
                mylist.pop()
                pair += 1
    print('Pair of Parenthesis: ', pair)
    max_len_parenthesis = pair * 2
    print('Max Length of parenthesis:', max_len_parenthesis)


# my_str = ['(', ')', '(', ')', ')']
# my_str = [')', '(', ')']
# my_str = ['(', '(', ')', ')', ')', '(']
# my_str = ['(', ')', ')', '(']
my_str = str(input('Enter: '))
check_para(my_str)
