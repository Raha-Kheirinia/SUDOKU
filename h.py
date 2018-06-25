######## HEURESTIQUE ########
from sudoku import* 

# Heurestique base sur calcul les possibilits d'une case.    
# Input : dictionnaire de grid inital avec des case vides
# Output: dictionnaire de grid complet   
def fill_grid_heurstique(grid):
    grid_result = grid #DICTIONNAIRE
    for s, d in grid.items():
        if d in '0.':
            digite_possible = getvalue_possible(grid_result,s)
            if len(digite_possible)== 1:
                grid_result.update({s: digite_possible[0]})
                fill_grid_heurstique(grid_result)
    return grid_result                      
#Retourne la liste des possibilites pour un case   
def getvalue_possible(sudoko,s):
    possibilite = ['1','2','3','4','5','6','7','8','9']
    cols = units[s][0]
    rows = units[s][1]
    squares = units[s][2]
    # check colone
    for i in range(9):
        d = cols[i]
        if(sudoko[d] in possibilite):
            possibilite.remove(sudoko[d])

    #check row                  
    for i in range(9):
        d = rows[i]
        if(sudoko[d] in possibilite):
            possibilite.remove(sudoko[d])

    #check square
    for i in range(9):
        d = squares[i]
        if(sudoko[d] in possibilite):
            possibilite.remove(sudoko[d])
    return possibilite

###################### test  ######################
grid1  = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
grid_simple  = '483020600900305001001806400008102900700564008006708245002609500800203009005010382'

print ('\n ----sudoko initial---- ')
display(grid_values(grid_simple))

print ('\n -----resultat par heurestique------ ')
display(fill_grid_heurstique(grid_values(grid_simple)))

print ('\n---result par parse_grid --- ')
display(parse_grid(grid_simple))
