############### Hill-Climbing ###############
from sudoku import*

def hill_climbing(grid):
    fixed_cells = []
    empty_cells = []
    for s, d in grid_values(grid).items():
        if d in '0.':
            fixed_cells.append(s)
        else:
            empty_cells.append(s)
    grid_result = random_fill(grid)
    iteration = 0
    tries = 0
    while(iteration < 20):
        rand = random.randint(0, len(empty_cells) - 1)
        random_cell_1 = empty_cells[rand]
        square_random_cell = units[random_cell_1][2]
        while (True):
            rand = random.randint(0, 8)
            random_cell_2 = square_random_cell[rand]
            if random_cell_1 != random_cell_2 and random_cell_2 not in fixed_cells:
                break
        cost_before_swap = cost(grid_result)
        grid_result = swap(grid_result, random_cell_1, random_cell_2)
        cost_after_swap = cost(grid_result)
        if cost_after_swap == 0:
            print("tentatives: ", tries)
            print("solution found")
            return grid_result
        if(cost_after_swap > cost_before_swap):
            swap(grid_result, random_cell_1, random_cell_2)
        if (cost_after_swap < cost_before_swap):
            tries += 1
            iteration = 0
        if (cost_after_swap == cost_before_swap):
            iteration += 1
    print("tentatives: ", tries)
    print("solution not found after 20 tries without improve")
    return grid_result

if __name__ == '__main__':
    hill_climbing(grid1)