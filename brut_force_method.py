## Testing Brut_force ## Warning : absolutly not finished !

# À traduire en anglais une fois que c'est terminé

# TEST 1 
### Génération d'une grille aléatoire et validation si celle-ci est valide (génération 1 seule fois)
def random_sudoku():
    grid = []
    for _ in range(9):
        ligne = [random.randint(1, 9) for _ in range(9)]
        grid.append(ligne)
    return grid

# Vérification des lignes dans la grille
def verifier_lignes(grid):
    for ligne in grid:
        if len(set(ligne)) != 9 or 0 in ligne:
            return False
    return True

# Vérification des colonnes dans la grille
def verifier_colonnes(grid):
    for j in range(9):
        colonne = [grid[i][j] for i in range(9)]
        if len(set(colonne)) != 9 or 0 in colonne:
            return False
    return True

# Vérification des carrés dans la grille
def verifier_carres(grid):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            carre = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if len(set(carre)) != 9 or 0 in carre:
                return False
    return True

# Application des fonctions de vérification (lignes, colonnes, carrés)
def verifier_sudoku(grid):
    return (verifier_lignes(grid) and
            verifier_colonnes(grid) and
            verifier_carres(grid))

# Génération d'une grille aléatoire
grid = random_sudoku()

# Affichage de la grille générée
print("Grille de Sudoku générée aléatoirement :")
for ligne in grid:
    print(ligne)

# Vérification de la grille pour savoir si elle est valide
if verifier_sudoku(grid):
    print("La grille de Sudoku est valide.")
else:
    print("La grille de Sudoku n'est pas valide.")


# TEST 2 
### Génération d'une grille alétoirement jusqu'à ce qu'elle est correcte
# Fonction pour vérifier les positions 
# de mes chiffres dans le sudoku.
def est_valide(grille, num, ligne, colonne):
    # Vérification de la ligne
    if num in grille[ligne]:
        # si numéro dans ma ligne, me renvoie = nombre en doublon
        # ligne non valide
        # True = fonction continue de vérifier cette même condition
        # dans la colonne
        return False
    
    # Vérification de la colonne
    for i in range(9):
        if grille[i][colonne] == num:
            # si l'index [i](ligne) de ma colonne trouve un doublon, 
            # me renvoie = nombre en doublon dans la colonne
            # colonne non valide
            # True = fonction continue sur le carré
            return False
    
    # Vérification du carré 3x3
    # indice de la ligne
    debut_ligne = (ligne // 3) * 3
    # indice de la colonne
    debut_colonne = (colonne // 3) * 3
    # Pour toutes les lignes et les colonnes 
    for i in range(debut_ligne, debut_ligne + 3):
        for j in range(debut_colonne, debut_colonne + 3):
            # vérification si le numéro est présent dans la grille à i et j position
            if grille[i][j] == num:
                # si doublon trouvé: 
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
