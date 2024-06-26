# Etude comparative des différentes méthodes de résolution des sudokus :

|                                     **Sommaire**                                  | 
|-----------------------------------------------------------------------------------|
|                         **1. Backtracking récursif Méthode A**                    |
|   a. Présentation de la fonction                                                  |
|   b. Analyse théorique                                                            |
|         - Complexité temporelle                                                       |
|         - Complexité spatiale                                                         |
|   c. Analyse empirique                                                            |
|         - Mesure du temps d’exécution moyen en fonction du nombre d’essais            |
|         - Mesure du temps d’exécution moyen en fonction du nombre de cases vides      |
|         - Profilage                                                                   |                     
|   d. Comparaison de l'étude théorique et empirique                                |
|                             **2. Force Brute Méthode A**                          |
|   a. Présentation de la fonction                                                  |
|   b. Analyse théorique                                                            |
|         - Complexité temporelle                                                       |
|         - Complexité spatiale                                                         |
|   c. Analyse empirique                                                            |
|         - Mesure du temps d’exécution moyen en fonction du nombre d’essais            |
|         - Mesure du temps d’exécution moyen en fonction du nombre de cases vides      |
|         - Profilage                                                                   |                     
|   d. Comparaison de l'étude théorique et empirique                                |
|                               **3. Backtracking Méthode B**                       |
|         a. Présentation de la fonction                                                    |
|         b. Compléxité algorithmique                                                       |
|         d. Conclusion                                                                     |
|                             **4. Comparaison des méthodes**                       |
|           a. Comparaison Backtracking Méthode A, Force Brute Méthode A et Backtracking Méthode B          |     
|                              b. Utilisation du profilage                          |
|                                   c. Conclusion                                   |



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

**Pire cas :** O(9^m) (où m est le nombre d’appels récursifs nécessaires pour résoudre le Sudoku).

**Cas moyen :** O(9^m) (Idem que le pire cas, car le backtracking explore toutes les combinaisons possibles).

**Meilleur cas :** O(m) (où m est le nombre d’appels récursifs nécessaires pour résoudre le Sudoku).

![Diverses complexités temporelles](https://github.com/pierre-mazard/Sudoku-Solver/blob/README.md/Pictures/Backtracking%20Method%20A%20(Recursiv)/big%20o.png "Diverses complexités temporelles")

**Conclusion :** 

La complexité temporelle ne reflète pas toujours le temps d’exécution réel. 

Le backtracking est une méthode très efficace pour résoudre le Sudoku car il élimine rapidement de nombreuses combinaisons invalides. 

De plus, la plupart des grilles de Sudoku sont conçues pour avoir une solution unique, ce qui signifie que l’algorithme n’a pas besoin d’explorer l’ensemble de l’espace de recherche.

#### 1.2. Complexité spatiale.

La complexité spatiale dépend de la profondeur de la récursion.

Chaque appel récursif crée une nouvelle pile d’appels avec des variables locales.

Dans le pire des cas, lorsque l’arbre de recherche est profond (par exemple, pour un Sudoku difficile), la complexité spatiale peut être O(9^m), où m est le nombre d’appels récursifs nécessaires pour résoudre le Sudoku.

**Conclusion :** 

En général, la complexité spatiale est linéaire par rapport au nombre d’appels récursifs.

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



# 2 Force Brute méthode méthode A.

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

### 1. Analyse théorique.**

#### 1\.1. Complexité temporelle.

**Pire cas :** O(9^81) (où 81 est le nombre total de cellules dans un Sudoku standard).

**Cas moyen :** O(9^81) (même que le pire cas, car elle génère toutes les permutations possibles).

**Meilleur cas :** O(1) (si la grille est déjà complète et valide).

![Diverses complexités temporelles](https://github.com/pierre-mazard/Sudoku-Solver/blob/README.md/Pictures/Backtracking%20Method%20A%20(Recursiv)/big%20o.png "Diverses complexités temporelles")

**Conclusion :** 

La méthode de force brute génère toutes les permutations possibles sans évaluer les contraintes implicites avant de construire la configuration complète.

#### 1\.2. Complexité spatiale.

La complexité spatiale dépend du stockage des permutations.

La méthode génère toutes les permutations possibles des chiffres de 1 à 9 pour chaque ligne.

Le nombre total de permutations est 9! = 362,880.

Ensuite, le programme stocke ces permutations en mémoire, ce qui nécessite un espace proportionnel à O(9!).

**Conclusion :** 

Cela peut être considéré comme une complexité spatiale constante car le nombre de permutations est fixe.

**2. Analyse empirique.** 

2\.1. Mesure du temps d’exécution moyen en fonction du nombre d’essais.

2\.2. Mesure du temps d’exécution moyen en fonction du nombre de cases vides.

**2\.3 Profilage.**

![Profilage](https://github.com/pierre-mazard/Sudoku-Solver/blob/main/Pictures/Backtracking%20Method%20A%20(Recursiv)/profiling%20force%20brute%20method%20A.png "Profilage")

**3. Comparaison de l’étude théorique et empirique.**

# 3. Backtracking méthode B
## a. Présentation de la fonction
### Code :
    def solve_sudoku(self):
        def is_valid(num, row, col):
            for i in range(9):
                if self.grid[row][i] == num or self.grid[i][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if self.grid[start_row + i][start_col + j] == num:
                        return False
            return True
        def solve_next_empty(row, col):
            if row == 8 and col == 9:
                return True
            if col == 9:
                row += 1
                col = 0
            if self.grid[row][col] != 0:
                return solve_next_empty(row, col + 1)
            for num in range(1, 10):
                if is_valid(num, row, col):
                    self.grid[row][col] = num
                    if solve_next_empty(row, col + 1):
                        return True
                    self.grid[row][col] = 0
            return False
        return solve_next_empty(0, 0)
        
### Explications: 

*def is_valid(num, row, col)* prends 3 arguments (num: nombre à vérifier, row: la ligne dans la grille, col: la colonne dans la grille). 

Avec 'start_row, start_col = 3 * (row // 3), 3 * (col // 3)' : calcul des coordonnées de la cellule en les divisants en neuf blocs de 3x3. 

Cette fonction examine si un nombre n'est pas déjà présent dans une ligne et colonne. S'il est présent : il retourne 'False' à la position identifiée. S'il n'est pas présent : True. 

*def solve_next_empty(row, col)* prends 2 arguments (row : la ligne, col : la colonne). 
C'est ici que la récursivité opérera en essayant de remplir les cases vides. 

Pour chaque nombre valide, il place dans la case le nombre et appelle la fonction 'solve_next_empty' pour continuer avec n+1.

Si une solution est valide : True et retourne la grille complétée.
Si aucune solution n'est valide : False et elle réinitialise la case à 0. Elle continue de chercher avec les autres nombres à disposition. Si aucun nombre ne correspond, la fonction revient en arrière : False, les choix précédents étaient incorrects et elle revient en arrière. 

Avec *return solve_next_empty(0, 0)* on appel la fonction pour commencer à la première ligne, première colonne. 

## b. Compléxité algorithmique

### La forme : 
Il existe deux formes en backtracking : itérative et récursive. 
Dans le cas de cette méthode, **le code utilise la forme récursive.**

*Toutes les possibilités sont explorées et il y a retour en arrière si l'exploration ne mène pas à une solution.*

La récursivité est utilisée pour exploiter toutes les possibilités de 1 à 9, et le backtracking est utilisé pour revenir en arrière si le numéro ne correspond pas à la ligne et colonne. 

### Les temps d'exécutions : 

| **Nb essais = 1** | Nombre cases vides |Moyenne exécution (ms.)
|---------------|-----------|-----------|
| Fichier 1     |    45       |    3,17      |
| Fichier 2     |    52       |    15,61      |
| **Fichier 3**     |    **43**       |    **1,54**      |
| Fichier 4     |    57       |    50,26      |
| Fichier 5     |    58       |    35,62      |

| **Nb essais = 100** | Nombre cases vides |Moyenne exécution (ms.)
|---------------|-----------|-----------|
| Fichier 1     |    45       |    0,0497    |
| Fichier 2     |    52       |    0,1594    |
| Fichier 3     |    43       |    0,0448    |
| Fichier 4     |    57       |    0,5462    |
| **Fichier 5**     |    **58**       |    **0,0241**    |

| **Nb essais = 1000** | Nombre cases vides |Moyenne exécution (ms.)
|---------------|-----------|-----------|
| Fichier 1     |    45       |    0,01994     |
| Fichier 2     |    52       |    0,16549     |
| **Fichier 3**     |    **43**       |    **0,01758**     |
| Fichier 4     |    57       |    0,06088     |
| Fichier 5     |    58       |    0,04642     |

| **Nb essais = 1000000** | Nombre cases vides |Moyenne exécution (ms.)
|---------------|-----------|-----------|
| Fichier 1     |    45       |    0,008552    |
| **Fichier 2**     |    **52**       |    **0,008460**    |
| Fichier 3     |    43       |    0,008488    |
| Fichier 4     |    57       |    0,008512    |
| Fichier 5     |    58       |    0,008477    |

## d.Conclusion

En prenant en compte le nombre de cases vides à remplir et la moyenne d'exécution de l'algorithme, le sudoku ayant le nombre de cases le plus bas (*n=43, sudoku 3*) obtient une moyenne de temps plus courte que les autres. 

Lorsqu'il s'agit de comparer le temps moyen de résolution selon le nombre de tests réalisés, les résultats deviennent intéressants : 
pour N=100 essais, le sudoku ayant une moyenne de temps la plus réduite rest le sudoku le plus difficile soit le sudoku 5 (*58 cases vides, 0,0000241 secondes*). 

Plus on ira dans les N = X essais, plus la moyenne de temps de résolution du sudoku vascillera entre: le sudoku 2, le sudoku 3 et le sudoku 5.


# 4. Comparaison des méthodes 3 méthodes
## a. Comparaison des méthodes.

La méthode de backtracking est plus efficace que la méthode de force brute, car elle optimise le processus en évaluant les contraintes plus tôt et en abandonnant les configurations invalides dès qu’elles sont détectées. 

Les deux méthodes possèdent une complexité temporelle exponentielle dans le pire des cas, mais on observe que dans la majorité des cas rencontrés pour des grilles classiques, la complexité temporelle reste constante ou linéaire pour les deux méthodes, en revanche, la méthode de backtracking reste plus rapide et plus optimale pour la résolution de grilles par rapport à la méthode de force brute. 

La complexité temporelle exacte dépend du Sudoku initial et du nombre d’opérations nécessaires pour remplir la grille. 

La méthode de backtracking a une complexité spatiale linéaire par rapport au nombre d’appels récursifs, tandis que la méthode de force brute stocke toutes les permutations possibles en mémoire. 

La complexité spatiale exacte dépend du Sudoku initial et de la manière dont les données sont stockées pendant l’exécution.

**Profilage Backtracking methode A** 

![Profilage](https://github.com/pierre-mazard/Sudoku-Solver/blob/main/Pictures/Backtracking%20Method%20A%20(Recursiv)/profiling%20backtracking%20A%20with%20executing%20time.png "Profilage")

**Profilage Force brute méthode A**

![Profilage](https://github.com/pierre-mazard/Sudoku-Solver/blob/main/Pictures/Backtracking%20Method%20A%20(Recursiv)/profiling%20force%20brut%20method%20A%20with%20executing%20time.png "Profilage")

Grace au profilage et à la relève du temps d'exécution des deux méthodes pour chaque grilles, on constate que le backtracking est plus performant et plus rapide que la force brute. 
## b. Comparaison Backtracking Méthode A, Force Brute Méthode A et Backtracking Méthode B 
### Moyenne de temps d'execution (exprimé en ms.)

| **Nb essais = 1** | Backtracking Méthode A |Force Brute Méthode A |Backtracking Méthode B |
|---------------|-----------|-----------|-----------|
| Fichier 1     |    10,07       |    8,91 |    3,17      |
| Fichier 2     |    36,47       |    37,20|    15,61      |
| **Fichier 3**     |    **5,62**       |   **5,65**|    **1,54**      |
| Fichier 4     |    151,93       |    152,75|    50,26      |
| Fichier 5     |    94,99       |    93,35 |    35,62      |

| **Nb essais = 100** |Backtracking Méthode A |Force Brute Méthode A |Backtracking Méthode B |
|---------------|-----------|-----------|-----------|
| Fichier 1     |    0,1171 |   0,1205|    0,0497    |
| Fichier 2     |    0,3710 |    0,3407|    0,1594    |
| Fichier 3     |    **0,0768** |    **0,0897**|    0,0448    |
| Fichier 4     |    1,6413 |    1,5216|    0,5462    |
| Fichier 5     |    0,9354 |    0,8923|    **0,0241**    |

| **Nb essais = 1000** |Backtracking Méthode A |Force Brute Méthode A |Backtracking Méthode B |
|---------------|-----------|-----------|-----------|
| Fichier 1     |    0,02594|    0,0269|    0,01994     |
| Fichier 2     |    0,04969|    0,0493|    0,16549     |
| Fichier 3     |    **0,02325**|    **0,0224**|    **0,01758**     |
| Fichier 4     |    0,16092|    0,1639|    0,06088     |
| Fichier 5     |    0,10333|    0,1034|    0,04642     |

| **Nb essais = 1000000** |Backtracking Méthode A |Force Brute Méthode A |Backtracking Méthode B |
|---------------|-----------|-----------|-----------|
| Fichier 1     |    0,010223|    0,010214|    0,008552    |
| Fichier 2     |    **0,010191**|    0,010205|    **0,008460**    |
| Fichier 3     |    0,010204|    **0,010168**|    0,008488    |
| Fichier 4     |    0,010338|   0,010360|    0,008512    |
| Fichier 5     |    0,010272|    0,010261|    0,008477    |

### Conclusion 

La vitesse d'exécution dépendra du nombre d'essais et du nombre de cases vides. 
La méthode B semble être plus rapide en matière d'exécution sur quasiment la totalité des test N=X .
Toutefois, pour nombres de test = 100, la méthode A fait apparaître une différence dans la moyenne de temps d'exécution. La méthode semble plus rapidement gérer le sudoku 3 alors que la méthode B semble gérer, à 100 tests, plus rapidement le sudoku 5. 

La force brute semble être un peu plus lente. 

## c. Utilisation du profilage


## d. Conclusion      

















































































[ref1]: Aspose.Words.9aec35a6-4671-493c-a8a4-1ee359cb6563.001.png
[ref2]: Aspose.Words.9aec35a6-4671-493c-a8a4-1ee359cb6563.005.png
[ref3]: Aspose.Words.9aec35a6-4671-493c-a8a4-1ee359cb6563.006.png
