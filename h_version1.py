######## heurestique 
from sudoku import* 
# heurestique

 
def fill_grid_heurstique(grid):
    grid_result = grid #DICTIONNAIRE
    for s, d in grid.items():
        if d in '0.':
            digite_possible = getvalue_possible(grid_result,s)
            if len(digite_possible)== 1:
                grid_result.update({s: digite_possible[0]})
                fill_grid_heurstique(grid_result)
    return grid_result

# heurestique base sur calcul les possibilits d'une case.
def heurestique_case_possibilities (s,grid):
    count_possibilites = 0
    d = grid_values(grid)[s]
    #print 'd',d
    if d in '0.' :
        lst_possible = getvalue_possible(grid_values(grid),s)
        count_possibilites = len(lst_possible) 
    return count_possibilites


# heurestique base sur le nombre case vides qui restent
def heurestique_case_restant (s,sudoko):
    count_vide = 0
    lst_peers = peers[s]
    #print 'peers[s] : ', peers[s]
    for i in lst_peers:
        x = sudoko[i]
        if x in ['0', '.']:
            count_vide = count_vide +1
    return count_vide
            

# Heuristique qui compte le nombre de conflits pour sudoku aleatoire
def heurestique_nbr_conflit(s,sudoko):
    conflit = 0
    cols = units[s][0]
    rows = units[s][1]
    squares = units[s][2]
    d = sudoko[s]

    for i in range(9):
        c = sudoko[cols[i]]
        r = sudoko[rows[i]]
        z = sudoko[squares[i]]
        #print 'cols[i]',cols
        if d == c:
            conflit = conflit +1
        if d == r:
            conflit = conflit +1
        if d == z:
            conflit = conflit +1

    return conflit
        
    
#Retourne la liste des possibilites pour un case   
def getvalue_possible(sudoko,s):
    possibilite = ['1','2','3','4','5','6','7','8','9']
    cols = units[s][0]
    rows = units[s][1]
    squares = units[s][2]
    case_vide = 0
    

    for i in range(9):
        d = cols[i]
        if(sudoko[d] in possibilite):
            possibilite.remove(sudoko[d])
        else :
            case_vide += 1
                       
    for i in range(9):
        d = rows[i]
        if(sudoko[d] in possibilite):
            possibilite.remove(sudoko[d])
        else :
            case_vide += 1

    for i in range(9):
        d = squares[i]
        if(sudoko[d] in possibilite):
            possibilite.remove(sudoko[d])
        else :
            case_vide += 1
    return possibilite



###################### test  ######################
grid1  = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
grid2  = '483020600900305001001806400008102900700564008006708245002609500800203009005010382'

#sudoko = grid_values(grid2)

for s in grid_values(grid2):
    d = grid_values(grid2)[s]
    #print ('squers' ,units[s][2])
    #print ('rows' ,units[s][1])
    #print ('cols' ,units[s][0])
    print ('nbr_possibilitie:', heurestique_case_possibilities(s,grid2))
    print ('s : ',s)
    print ('d : ',d)
    #print ('heurestique_case_restant : ', heurestique_case_restant(s,sudoko))
    print (' ')
    #print 'heurestique_nbr_conflit(s) : ',  heurestique_nbr_conflit(s,sudoko)
display(fill_grid_heurstique(grid_values(grid2)))
print ('sudoko initial ---> ')
display(grid_values(grid2))
print ('')
print ('sudoko resultat ---> ')
display(parse_grid(grid2))
