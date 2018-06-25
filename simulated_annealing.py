######## SIMULATED ANNEALING 
from sudoku import*
import random
import math
import decimal


########## fonction de SIMULATED ANNEALING ############
def simulated_annealing(grid, t_0=3):
    empty_cells = []
    fixed_cells = []
    for s, d in grid_values(grid).items():
        if d in '0.':
            empty_cells.append(s)
        else:
            fixed_cells.append(s)
    grid_result = random_fill(grid)
    cooling_rate = 0.99
    t = t_0
    while(True):
        if t==0 :
            return grid_result
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
            return grid_result
        if(cost_after_swap > cost_before_swap):
            probability_accept = math.exp(-(cost_after_swap - cost_before_swap) / t)
            # calculer tir de bernoulli pour accepter nouveau etat
            if (0.5 < probability_accept):
                # probability < probability_accept don't accept
                swap(grid_result, random_cell_1, random_cell_2)
        t *= cooling_rate
        print(t)
    return grid_result

        
###################### test  ######################
grid1  = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'

#print ("grid inital")
#display (grid_values(grid1))
#print ("result")
#display(parse_grid(grid1))
#print ('grid aleatoire')
#display(random_fill(grid1))
#print ("cost grid: ", cost(grid_values(grid1)))
print ('simulated annealing')
display(simulated_annealing(grid1))

#display({'I6': '7', 'H9': '9', 'I2': '9', 'E8': '3', 'H3': '4', 'H7': '7', 'I7': '3', 'I4': '4', 'H5': '5', 'F9': '5', 'G7': '5', 'G6': '9', 'G5': '8', 'E1': '7', 'G3': '2', 'G2': '7', 'G1': '3', 'I1': '6', 'C8': '9', 'I3': '5', 'E5': '6', 'I5': '1', 'C9': '3', 'G9': '4', 'G8': '1', 'A1': '4', 'A3': '3', 'A2': '8', 'A5': '2', 'A4': '9', 'A7': '6', 'A6': '1', 'C3': '1', 'C2': '5', 'C1': '2', 'E6': '4', 'C7': '4', 'C6': '6', 'C5': '7', 'C4': '8', 'I9': '2', 'D8': '7', 'I8': '8', 'E4': '5', 'D9': '6', 'H8': '6', 'F6': '8', 'A9': '7', 'G4': '6', 'A8': '5', 'E7': '1', 'E3': '9', 'F1': '1', 'F2': '3', 'F3': '6', 'F4': '7', 'F5': '9', 'E2': '2', 'F7': '2', 'F8': '4', 'D2': '4', 'H1': '8', 'H6': '3', 'H2': '1', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8', 'E9': '8', 'B1': '9', 'B2': '6', 'B3': '7', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '3', 'B8': '2', 'B9': '1', 'D1': '5'})






