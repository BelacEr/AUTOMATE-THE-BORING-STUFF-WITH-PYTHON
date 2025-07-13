grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def picture_grid(grid):
    first_row = len(grid) # 9
    second_row = len(grid[0]) # 6

    for second in range(second_row): # 6
        for first in range(first_row): # 9
                print(grid[first][second], end='')
        print()

picture_grid(grid)

'''
Copy the previous grid value, and write code that uses it to print
the image.
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
'''