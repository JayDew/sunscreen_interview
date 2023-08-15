#    TODO:
#       1. Find center, or the highest number closest to it
#       2. Set carrot_count to 0, increment count accordingly
#       3. Find the square next to it with the highest number
#       4. Repeat step 2 until it there are no adjacent squares other than 0's
#       5. Break loop, return carrot_count

def hungry_rabbit_util(garden, row, col):
    """
    This recursive method returns the number of carrots along a valid path
    that the rabbit can eat following the 'immediate' highest value path:
    at each iteration, the rabbit chooses to move in the direction that
    maximizes the immediate profit.
    :param garden: N x M matrix
    :param row: current row
    :param col: current column
    :return: number of carrots eaten following the 'immediate' highest value path
    """
    max = 0
    next_row = None
    next_col = None

    for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if row + r >= 0 and row + r < len(garden) and \
                col + c >= 0 and col + c < len(garden[row]):
            if garden[row + r][col + c] > max:
                max = garden[row + r][col + c]
                next_row = row + r
                next_col = col + c

    carrots = garden[row][col]
    garden[row][col] = 0  # the rabbit consumes the carrot, prevents infinite loops

    if max > 0 and next_row is not None and next_col is not None:
        carrots += hungry_rabbit_util(garden, next_row, next_col)

    return carrots


def find_center(garden):
    """
    Finds the center, or the highest number closest to it, in the garden matrix.
    :param garden: N x M matrix
    :return: coordinates of the best starting point
    """
    row_options = [len(garden) // 2, len(garden) // 2]
    col_options = [len(garden[0]) // 2, len(garden[0]) // 2]

    # Adjust options if the matrix dimensions are even
    if len(garden) % 2 == 0:
        row_options[0] -= 1

    if len(garden[0]) % 2 == 0:
        col_options[0] -= 1

    max = 0
    row = None
    col = None

    for r_option in row_options:
        for c_option in col_options:
            if garden[r_option][c_option] > max:
                max = garden[r_option][c_option]
                row = r_option
                col = c_option

    return row, col


def hungry_rabbit(garden):
    """
    Solve the hungry rabbit problem.
    :param garden: rectangular N x M 2D matrix with positive values
    :return:  number of carrots eaten by the rabbit choosing the square that has the most carrots
    """
    if len(garden) == 0 or len(garden[0]) == 0:
        return 0

    # create a copy of the garden
    copy = [g_row[:] for g_row in garden]
    row, col = find_center(copy)

    if row is None or col is None:
        return 0

    return hungry_rabbit_util(copy, row, col)


if __name__ == "__main__":
    garden = [
        [5, 7, 8, 6, 3],
        [0, 0, 7, 0, 4],
        [4, 6, 3, 4, 9],
        [3, 1, 0, 5, 8]
    ]

    print("ANSWER:", hungry_rabbit(garden))
    print("Thanks Ravital for an amazing problem !!! <3")
