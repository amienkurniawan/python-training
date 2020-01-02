number_of_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

def function_get_row():
    for row in number_of_grid :
        print(row)

def function_get_col():
    for row in number_of_grid :
        for col in row:
            print(col)

function_get_row()
function_get_col()