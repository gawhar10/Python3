"""
Full version of parenthesis checking program.
It checks round, square, curly parenthesis and also counts them.
"""


def check_para(mystr):
    """
    method to check parenthesis.
    """
    open_round = []
    close_round = []
    open_curly = []
    close_curly = []
    open_square = []
    close_square = []
    for i in range(0, len(mystr)):
        mylist = mystr[i]
        if mylist == '(':
            open_round = open_round + ['(']
        elif mylist == ')':
            close_round = close_round + [')']
        elif mylist == '{':
            open_curly = open_curly + ['{']
        elif mylist == '}':
            close_curly = close_curly + ['}']
        elif mylist == '[':
            open_square = open_square + ['[']
        elif mylist == ']':
            close_square = close_square + [']']
        else:
            return (open_round, close_round, open_curly, close_curly, open_square, close_square)

    if len(open_round) == len(close_round) and len(open_curly) == len(close_curly):
        print('paired\n',
              'Round Pair: ', len(open_round), '\n',
              'Curly Pair: ', len(open_curly), '\n',
              'Square Pair: ', len(open_square))
    else:
        print('Result: Unpaired\n',
              'Open Round: ', len(open_round), '\n',
              'Close Round: ', len(close_round), '\n',
              'Open Curly: ', len(open_curly), '\n',
              'Close curly: ', len(close_curly), '\n',
              'Open Square: ', len(open_square), '\n',
              'Close Square: ', len(close_square))


# my_str = ['(', ')', '(', ')', ')', '{', '}', '[', '[']
my_str = str(input('Enter: '))
check_para(my_str)
