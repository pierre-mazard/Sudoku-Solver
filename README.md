# Etude comparative des différentes méthodes de résolution des sudokus :

## Sommaire

## 1 Backtracking récursif méthode A.

**1. Analyse théorique.**

_1\.1. Complexité temporelle._

_1\.2. Complexité spatiale._

**2. Analyse empirique.** 

_2\.1. Mesure du temps d’exécution moyen en fonction du nombre d’essais._

_2\.2. Mesure du temps d’exécution moyen en fonction du nombre de cases vides._

_2\.3 Profilage._

**3. Comparaison de l’étude théorique et empirique.**

## 2 Force Brute méthode B.

**1. Analyse théorique.**

_1\.1. Complexité temporelle._

_1\.2. Complexité spatiale._

**2. Analyse empirique.** 

_2\.1. Mesure du temps d’exécution moyen en fonction du nombre d’essais._

_2\.2. Mesure du temps d’exécution moyen en fonction du nombre de cases vides._

_2\.3 Profilage._

**3. Comparaison de l’étude théorique et empirique.**

## 3 Comparaison des méthodes.




# 1 Backtracking récursif méthode A.


    def solve_sudoku(self): # Solve Sudoku using backtracking method 
        for row in range(9): # Find an empty cell to place a number
            for col in range(9): # Try placing numbers from 1 to 9 in the empty cell
                if self.grid[row][col] == 0: # If the number is valid, place it in the cell
                    for num in range(1, 10): # If the number is not valid, backtrack and try a different number
                        if self.is_valid_move(row, col, num): # If all numbers are tried and none are valid, backtrack to the previous cell
                            self.grid[row][col] = num # If the number is valid, place it in the cell
                            if self.solve_sudoku(): # Recursively solve the Sudoku grid
                                return True # If the Sudoku is solved, return True
                            self.grid[row][col] = 0 # If the Sudoku is not solved, backtrack and try a different number
                    return False # If all numbers are tried and none are valid, return False
        return True # If all cells are filled, return True 


**Fonctionnement de la méthode:**

Elle parcourt chaque cellule de la grille.

Si la cellule est vide (contient 0), elle essaie de placer les chiffres de 1 à 9 dans cette cellule.
Pour chaque chiffre, elle vérifie s’il est valide en appelant la fonction is_valid_move(row, col, num).

Si le chiffre est valide, elle le place dans la cellule et récursivement continue à résoudre le reste de la grille.

Si la grille est résolue, elle renvoie True.

Sinon, elle revient en arrière (backtrack) en réinitialisant la cellule et en essayant un autre chiffre.

Si aucun chiffre ne convient, elle renvoie False.

L’approche de backtracking permet d’explorer efficacement les différentes combinaisons tout en évitant les configurations invalides.


### 1. Analyse théorique.

#### 1.1. Complexité temporelle.

La complexité temporelle de la méthode A a été évaluée à **O(9^M)**

La complexité temporelle du backtracking est généralement de l’ordre de **O(N^M)** il s’agit d’une **complexité exponentielle**.

*où **N** = nombre de possibilités pour chaque cellule (dans le cas du Sudoku, N=9).*

*et **M** = nombre de cellules vides à remplir.*

Dans le pire des cas elle est équivalente à **O(9^81)**

![Complexité temporelle backtracking methode récursive](https://github.com/pierre-mazard/Sudoku-Solver/blob/README.md/Pictures/Backtracking%20Method%20A%20(Recursiv)/Big%20O%20Backtracking%20Method%20A.png "Complexité temporelle backtracking methode récursive")

![Diverses complexités temporelles](https://github.com/pierre-mazard/Sudoku-Solver/blob/README.md/Pictures/Backtracking%20Method%20A%20(Recursiv)/big%20o.png "Diverses complexités temporelles")

**Conclusion :** 

La complexité temporelle ne reflète pas toujours le temps d’exécution réel. 

Le backtracking est une méthode très efficace pour résoudre le Sudoku car il élimine rapidement de nombreuses combinaisons invalides. 

De plus, la plupart des grilles de Sudoku sont conçues pour avoir une solution unique, ce qui signifie que l’algorithme n’a pas besoin d’explorer l’ensemble de l’espace de recherche.

#### 1.2. Complexité spatiale.

La complexité spatiale est de l’ordre de **O(n)** il s’agit d’une **complexité linéaire.**

*où **n** = nombre de cellules dans la grille.* 

![Complexité spatiale backtracking methode récursive](https://github.com/pierre-mazard/Sudoku-Solver/blob/README.md/Pictures/Backtracking%20Method%20A%20(Recursiv)/Spatial%20Complexity%20Backtracking%20Method%20A.png "Complexité spatiale backtracking methode récursive")

**Conclusion :** 

La **complexité est linéaire** car l’algorithme utilise de l’espace supplémentaire pour stocker la grille de Sudoku et effectuer le backtracking. 

Dans le cas d’une grille de Sudoku standard de 9x9, la complexité spatiale serait donc de **O(81)**, soit **O(1)** en termes de complexité spatiale asymptotique.

### 2. Analyse empirique.

#### 2.1. Mesure du temps d’exécution moyen en fonction du nombre d’essais.

![Temps d'exécution moyen en fonction du nombre d'essais](https://github.com/pierre-mazard/Sudoku-Solver/blob/README.md/Pictures/Backtracking%20Method%20A%20(Recursiv)/Execution%20time%20versus%20Trials%20number%20Backtracking%20Method%20A.png "Temps d'exécution moyen en fonction du nombre d'essais")

On observe que plus on augmente le nombre d'essais, plus la moyenne du temps d'exécution diminue et la disparité en temps d'exécution entre les différentes grilles diminue également, ce qui peut être expliqué par les points suivants : 

**_=> Variabilité :_** 

Lorsqu'un seul essaie est effectué, il peut y avoir des fluctuations aléatoires dans le temps d'exécution.

Ces variations peuvent être dues à des facteurs tels que la charge du processeur, les interruptions système, la gestion de la mémoire etc.

**_=> Effet de la Moyenne :_** 

Lorsque plusieurs essais sont effectués, la moyenne des temps d'exécution lisse ces fluctuations aléatoires.

En prenant la moyenne, on obtient une meilleure estimation du temps d'exécution moyen réel.

**_=> Amortissement des Coûts Fixes :_**

Certains coûts fixes (comme l'initialisation, la lecture du fichier etc.) sont associés au démarrage du processus de résolution du Sudoku.

Lorsque plusieurs essais sont effectués, ces coûts fixes sont amortis sur l'ensemble des essais.

Cela réduit le temps moyen par essai.

**_=> Optimisation du Cache et de la Mémoire :_** 

Le cache et la mémoire peuvent jouer un rôle.

Lorsque plusieurs essais sont effectués, les données sont souvent déjà en cache ou en mémoire, ce qui accélère les accès.


**Conclusion :**

L'observation selon laquelle la moyenne du temps d'exécution diminue avec les nombre d'essais est normale et attendue. 

Cela démontre que le code est efficace et que les fluctuations aléatoires sont compensées par la moyenne. 

#### 2.2. Mesure du temps d’exécution moyen en fonction du nombre de cases vides.

![Temps d'exécution moyen en fonction du nombre de cases vides](https://github.com/pierre-mazard/Sudoku-Solver/blob/README.md/Pictures/Backtracking%20Method%20A%20(Recursiv)/Execution%20Time%20versus%20Empty%20cases%20Number%20Backtracking%20Method%20A.png "Temps d'exécution moyen en fonction du nombre de cases vides")

On observe qu’il réside lors d’un faible nombre d’essais une disparité en temps d’exécution du programme selon les Sudokus, moins il y à de cases vides à résoudre plus le temps d’exécution du programme est rapide en général, il réside quelques exceptions comme pour le sudoku4 car le temps d'exécution et la difficulté d'une grille ne dépend pas seulement du nombre de cases à remplir.

Plus on augmente le nombre d'essais, plus on observe un temps d’exécution moyen quasiment similaire par Sudoku pour les mêmes raisons que mentionnées ci-dessus.  

On observe également que le sudoku4 est dans tous les cas celui qui demande le temps d’exécution le plus long, probablement induit par le fait qu’il s’agisse du plus difficile/long à résoudre pour le programme.


**Conclusion :**

L’observation démontre que le programme est rapide et efficace pour la résolution des différentes grilles de Sudoku et permet d’établir sommairement un premier classement de difficulté des grilles (en fonction de la rapidité que le programme prend pour résoudre les grilles).

**1 Sudoku 3** avec 43 cases à résoudre.

**2 Sudoku 1** avec 45 cases à résoudre.

**3 Sudoku 2** avec 52 cases à résoudre.

**4 Sudoku 5** à 58 cases à résoudre.

**5 Sudoku 4** à 57 cases à résoudre. 


#### 2.3 Profilage.

![Profilage](https://github.com/pierre-mazard/Sudoku-Solver/blob/README.md/Pictures/Backtracking%20Method%20A%20(Recursiv)/Backtracking%20Method%20A%20Profiling%20Results.png "Profilage")

On observe lors du profilage que le nombre de fonctions appelées lors de la résolution des grilles diffère d’une grille à l’autre.  

**Conclusion :**

L’observation vient corroborer le classement de difficulté établi ci-dessus. 

Le temps d’exécution moyen du programme à résoudre chaque grilles dépend du nombre de fonctions appelées lors de l’exécution. 

### 3. Comparaison de l’étude théorique et empirique.

![Complexité temporelle backtracking methode récursive](https://github.com/pierre-mazard/Sudoku-Solver/blob/README.md/Pictures/Backtracking%20Method%20A%20(Recursiv)/Big%20O%20Backtracking%20Method%20A.png "Complexité temporelle backtracking methode récursive")

![Temps d'exécution moyen en fonction du nombre de cases vides](https://github.com/pierre-mazard/Sudoku-Solver/blob/README.md/Pictures/Backtracking%20Method%20A%20(Recursiv)/Execution%20Time%20versus%20Empty%20cases%20Number%20Backtracking%20Method%20A.png "Temps d'exécution moyen en fonction du nombre de cases vides")

Le temps moyen d’exécution du programme mesuré est quasiment linéaire, constant, et équivalent d’un sudoku à l’autre pour une moyenne effectuée pour de nombreux essais (1000000), ce qui fait de ce programme une méthode rapide et efficace dans la quasi-totalité des cas. 

L’étude théorique de la complexité en temps démontre une tendance exponentielle dans le pire des cas (si la grille est entièrement vide) ce qui s’explique par le fait que dans ce cas le programme ne peut tout simplement pas résoudre le sudoku, mais pour les autres cas, la tendance reste linéaire et constante également. 

On observe les mêmes tendances entre l’étude théorique et les mesures ce qui démontre que le programme est bel et bien opérationnel et rapide dans la plupart des cas.

Il est également possible d'effectuer un premier classement de difficulté des grilles en fonction du temps d’exécution du programme et du nombre de fonctions appelées pour la résolution de chaques grilles :  

**1 Sudoku 3** avec 43 cases à résoudre et 1215 fonctions appelées.

**2 Sudoku 1** avec 45 cases à résoudre et 2585 fonctions appelées. 

**3 Sudoku 2** avec 52 cases à résoudre et 13723 fonctions appelées.

**4 Sudoku 5** avec 58 cases à résoudre et 42629 fonctions appelées.

**5 Sudoku 4** avec 57 cases à résoudre et 71928 fonctions appelées. 







# 2 Force Brute méthode B.

    def brute_force_solve(self):
        numbers = list(range(1, 10))  # Numbers to fill the grid
        for row in range(9):
            if 0 in self.grid[row]:  # If the row contains empty cells
                permutations = itertools.permutations(numbers)  # Generate all permutations of numbers
                for permutation in permutations:
                    # Try to fill the row with the permutation
                    for col in range(9):
                        if self.grid[row][col] == 0:
                            self.grid[row][col] = permutation[col]
                    # If the grid is valid, move to the next row
                    if self.is_valid_grid():
                        break
                    # If the grid is not valid, reset the row and try the next permutation
                    else:
                        self.grid[row] = self.original_grid[row]
        return self.grid

**Fonctionnement de la méthode:**

Génération complète des permutations :

La méthode commence par créer une liste de chiffres de 1 à 9.

Pour chaque ligne dans la grille, elle génère toutes les permutations possibles de ces chiffres.

Elle remplit ensuite la ligne avec chaque permutation et vérifie si la grille est valide en appelant la fonction is_valid_grid().

Évaluation des contraintes après la génération :

La méthode génère toutes les permutations avant de vérifier si la grille est valide.

Elle ne tient pas compte des contraintes implicites (par exemple, la relation entre les chiffres dans la même colonne ou le même carré).

Pas d’abandon anticipé :

Si une permutation ne donne pas une grille valide, la méthode réinitialise la ligne et essaie la permutation suivante.

Elle ne vérifie pas les contraintes implicites avant de générer toutes les solutions possibles.

En résumé, la méthode explore toutes les combinaisons possibles de chiffres pour chaque ligne sans évaluer les contraintes implicites plus tôt dans le processus.
# ! A faire !

**1. Analyse théorique.**

1\.1. Complexité temporelle.

1\.2. Complexité spatiale.

**2. Analyse empirique.** 

2\.1. Mesure du temps d’exécution moyen en fonction du nombre d’essais.

2\.2. Mesure du temps d’exécution moyen en fonction du nombre de cases vides.

2\.3 Profilage.

**3. Comparaison de l’étude théorique et empirique.**

**3 Comparaison des méthodes.**
















































































































[ref1]: Aspose.Words.9aec35a6-4671-493c-a8a4-1ee359cb6563.001.png
[ref2]: Aspose.Words.9aec35a6-4671-493c-a8a4-1ee359cb6563.005.png
[ref3]: Aspose.Words.9aec35a6-4671-493c-a8a4-1ee359cb6563.006.png
