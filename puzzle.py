'''Check whether the board given is suitable for the puzzle game'''
def validate_board(board:list)->bool:
    '''
    Checks for matche in the board and returns it's validity in bool type

    >>> validate_board([ "**** ****", "***1 ****", "**  3****", "* 4 7****", \
"     9 5 ", " 6  83  *", "3   0  **", "  8  2***", "  2  ****"])
    True
    '''
    # Check colums
    for i in range(9):
        memory_list=[]
        for j in range(9):
            if board[j][i] !='*'and board[j][i] !=' ':
                memory_list.append(board[j][i])
                if board[j][i] in memory_list[:-1]:
                    return False
    # Check rows
    for i in board:
        memory_list=[]
        for j in i:
            if j !='*' and j!=' ':
                memory_list.append(j)
                if j in  memory_list[:-1]:
                    return False
    # Check colors
    minus_colum=4
    for i in range(5):
        memory_list=[]
        for colum in range(5):
            if board[colum+minus_colum][i] !='*'and board[colum+minus_colum][i] !=' ':
                memory_list.append(board[colum+minus_colum][i])
                if board[colum+minus_colum][i] in memory_list[:-1]:
                    return False
if __name__=='__main__':
    import doctest
    print(doctest.testmod())
