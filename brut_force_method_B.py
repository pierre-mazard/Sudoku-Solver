## Testing Brut_force ## Warning : absolutly not finished !

# TEST 2 
### Generating a grid randomly until it's correct
def est_valide(grille, num, ligne, colonne):
    if num in grille[ligne]:
        return False
    
    for i in range(9):
        if grille[i][colonne] == num:
            return False
    
    for i in range(debut_ligne, debut_ligne + 3):
        for j in range(debut_colonne, debut_colonne + 3):
            if grille[i][j] == num:
                return False

    return True

def generer_sudoku():
    grille = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            nombre_aleatoire = random.randint(1, 9)
            while not est_valide(grille, nombre_aleatoire, i, j):
                nombre_aleatoire = random.randint(1, 9)
            grille[i][j] = nombre_aleatoire
    return grille

def verifier_sudoku(grille):
    for i in range(9):
        ligne = grille[i]
        colonne = [grille[j][i] for j in range(9)]
        carre = []
        debut_ligne = (i // 3) * 3
        debut_colonne = (i % 3) * 3
        for m in range(debut_ligne, debut_ligne + 3):
            for n in range(debut_colonne, debut_colonne + 3):
                carre.append(grille[m][n])
        if len(set(ligne)) != 9 or len(set(colonne)) != 9 or len(set(carre)) != 9:
            return False
    return True

def afficher_sudoku(grille):
    for ligne in grille:
        print(' '.join(map(str, ligne)))

def sudoku_brute_force():
    while True:
        grille = generer_sudoku()
        if verifier_sudoku(grille):
            print("Grille de Sudoku valide générée :")
            afficher_sudoku(grille)
            break

# Génération et vérification de grilles de Sudoku jusqu'à ce qu'une grille valide soit trouvée
sudoku_brute_force()
