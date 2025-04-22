def odd_magic_square(size):
    square = [[0] * size for _ in range(size)]
    row, col = 0, size // 2
    value = 1

    while value <= size * size:
        square[row][col] = value
        value += 1
        new_row, new_col = (row - 1) % size, (col + 1) % size
        if square[new_row][new_col]:
            row = (row + 1) % size
        else:
            row, col = new_row, new_col

    return square

def doubly_even_magic_square(size):
    grid = [[(size * r) + c + 1 for c in range(size)] for r in range(size)]

    for row in range(size):
        for col in range(size):
            if (row % 4 == col % 4) or ((row + col) % 4 == 3):
                grid[row][col] = size * size + 1 - grid[row][col]

    return grid

def singly_even_magic_square(size):
    half = size // 2
    base = odd_magic_square(half)
    grid = [[0] * size for _ in range(size)]
    add = [0, 2 * half * half, 3 * half * half, half * half]

    for row in range(half):
        for col in range(half):
            for block in range(4):
                r = row + (block // 2) * half
                c = col + (block % 2) * half
                grid[r][c] = base[row][col] + add[block]

    swap_count = (size - 2) // 4

    for row in range(size):
        for col in range(swap_count):
            if row < half:
                grid[row][col], grid[row + half][col] = grid[row + half][col], grid[row][col]

        for col in range(size - swap_count + 1, size):
            if row < half:
                grid[row][col], grid[row + half][col] = grid[row + half][col], grid[row][col]

    grid[half][0], grid[size - 1][0] = grid[size - 1][0], grid[half][0]

    return grid

def print_square(grid):
    for row in grid:
        print('  '.join(str(val).rjust(3) for val in row))
    print('\n')

for dimension in [4, 5, 6, 7, 8]:
    print(f"\nMagic Square of size {dimension}:")

    if dimension % 2 == 1:
        magic = odd_magic_square(dimension)
    elif dimension % 4 == 0:
        magic = doubly_even_magic_square(dimension)
    else:
        magic = singly_even_magic_square(dimension)

    print_square(magic)