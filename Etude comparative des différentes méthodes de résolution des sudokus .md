**Etude comparative des différentes méthodes de résolution des sudokus :** 

**1 Backtracking.**

**1.A Backtracking récursif.**
**


**1. Analyse théorique.**

1\.1. Complexité temporelle.

1\.2. Complexité spatiale.

**2. Analyse empirique.** 

2\.1. Mesure du temps d’exécution moyen en fonction du nombre d’essais.

2\.2. Mesure du temps d’exécution moyen en fonction du nombre de cases vides.

2\.3 Profilage.

**3. Comparaison de l’étude théorique et empirique.**

**1.B Backtracking itératif** 



**1. Analyse théorique.**

1\.1. Complexité temporelle.

1\.2. Complexité spatiale.

**2. Analyse empirique.** 

2\.1. Mesure du temps d’exécution moyen en fonction du nombre d’essais.

2\.2. Mesure du temps d’exécution moyen en fonction du nombre de cases vides.

2\.3 Profilage.

**3. Comparaison de l’étude théorique et empirique.**

**2 Force Brute.**

**1. Analyse théorique.**

1\.1. Complexité temporelle.

1\.2. Complexité spatiale.

**2. Analyse empirique.** 

2\.1. Mesure du temps d’exécution moyen en fonction du nombre d’essais.

2\.2. Mesure du temps d’exécution moyen en fonction du nombre de cases vides.

2\.3 Profilage.

**3. Comparaison de l’étude théorique et empirique..**

**3 Comparaison des méthodes.**















**1 Backtracking.**

**1.A Backtracking récursif.**
**


**1. Analyse théorique.**

**1.1. Complexité temporelle.**

La complexité temporelle de la méthode A a été évaluée à **O(9^M)**

La complexité temporelle du backtracking est généralement de l’ordre de **O(N^M)** il s’agit d’une **complexité exponentielle**.

*où **N** = nombre de possibilités pour chaque cellule (dans le cas du Sudoku, N=9).*

*et **M** = nombre de cellules vides à remplir.*

Dans le pire des cas elle est équivalente à **O(9^81)**

![ref1]

![](Aspose.Words.9aec35a6-4671-493c-a8a4-1ee359cb6563.002.png)

**Conclusion :** 

La complexité temporelle ne reflète pas toujours le temps d’exécution réel. 

Le backtracking est une méthode très efficace pour résoudre le Sudoku car il élimine rapidement de nombreuses combinaisons invalides. 

De plus, la plupart des grilles de Sudoku sont conçues pour avoir une solution unique, ce qui signifie que l’algorithme n’a pas besoin d’explorer l’ensemble de l’espace de recherche.


**1.2. Complexité spatiale.**

La complexité spatiale est de l’ordre de **O(n)** il s’agit d’une **complexité linéaire.**

` `*où **n** = nombre de cellules dans la grille.* 

![](Aspose.Words.9aec35a6-4671-493c-a8a4-1ee359cb6563.003.png)

**Conclusion :** 

La **complexité est linéaire** car l’algorithme utilise de l’espace supplémentaire pour stocker la grille de Sudoku et effectuer le backtracking. 

Dans le cas d’une grille de Sudoku standard de 9x9, la complexité spatiale serait donc de **O(81)**, soit **O(1)** en termes de complexité spatiale asymptotique.
















**2. Analyse empirique.**
**


**2.1. Mesure du temps d’exécution moyen en fonction du nombre d’essais.**

![Graphique](Aspose.Words.9aec35a6-4671-493c-a8a4-1ee359cb6563.004.png)

On observe que plus on augmente le nombre d'essais, plus la moyenne du temps d'exécution diminue ce qui peut être expliqué par les points suivants : 

**=> Variabilité :** 

Lorsqu'un seul essaie est effectué, il peut y avoir des fluctuations aléatoires dans le temps d'exécution.

Ces variations peuvent être dues à des facteurs tels que la charge du processeur, les interruptions système, la gestion de la mémoire etc.

**=> Effet de la Moyenne** :

Lorsque plusieurs essais sont effectués, la moyenne des temps d'exécution lisse ces fluctuations aléatoires.

En prenant la moyenne, on obtient une meilleure estimation du temps d'exécution moyen réel.

**=> Amortissement des Coûts Fixes :**

Certains coûts fixes (comme l'initialisation, la lecture du fichier etc.) sont associés au démarrage du processus de résolution du Sudoku.

Lorsque plusieurs essais sont effectués, ces coûts fixes sont amortis sur l'ensemble des essais.

Cela réduit le temps moyen par essai.

**=> Optimisation du Cache et de la Mémoire** :

Le cache et la mémoire peuvent jouer un rôle.

Lorsque plusieurs essais sont effectués, les données sont souvent déjà en cache ou en mémoire, ce qui accélère les accès.


**Conclusion :**

L'observation selon laquelle la moyenne du temps d'exécution diminue avec les nombre d'essais est normale et attendue. 

Cela démontre que le code est efficace et que les fluctuations aléatoires sont compensées par la moyenne. 

**2.2. Mesure du temps d’exécution moyen en fonction du nombre de cases vides.**

![ref2]

On observe qu’il réside lors d’un faible nombre d’essais une disparité en temps d’exécution du programme selon les Sudokus, moins il y à de cases vides à résoudre plus le temps d’exécution du programme est rapide.

Plus on augmente le nombre d'essais, plus on observe un temps d’exécution moyen quasiment similaire par Sudoku pour les mêmes raisons que mentionnées ci-dessus.  

On observe également que le sudoku4 est dans tous les cas celui qui demande un temps d’exécution le plus long, probablement induit par le fait qu’il s’agisse du plus difficile/long à résoudre pour le programme


**Conclusion :**

L’observation démontre que le programme est rapide et efficace pour la résolution des différentes grilles de Sudoku et permet d’établir sommairement un premier classement de difficulté des grilles (en fonction de la rapidité du programme à résoudre les grilles).

**1 Sudoku 3** à 43 cases à résoudre.

**2 Sudoku 1** à 45 cases à résoudre.

**3 Sudoku 2** à 52 cases à résoudre.

**4 Sudoku 5** à 58 cases à résoudre.

**5 Sudoku 4** à 57 cases à résoudre. 


**2.3 Profilage.**

|Sudoku name|Profiling results : number of functions called|
| :- | :- |
|sudoku3.txt|1215|
|sudoku1.txt|2587|
|sudoku2.txt|13723|
|sudoku5.txt|42629|
|sudoku4.txt|71928|

On observe lors du profilage que le nombre de fonctions appelées lors de la résolution des grilles diffère d’une grille à l’autre.  

**Conclusion :**

L’observation vient corroborer le classement de difficulté établi ci-dessus. 

Le temps d’exécution moyen du programme à résoudre chaque grilles dépend du nombre de fonctions appelées lors de l’exécution. 






**3. Comparaison de l’étude théorique et empirique.**

![ref2]

![ref3]

Le temps moyen d’exécution du programme mesuré est quasiment linéaire, constant, et équivalent d’un sudoku à l’autre pour une moyenne effectuée pour de nombreux essais (1000000), ce qui fait de ce programme une méthode rapide et efficace dans la quasi-totalité des cas. 

L’étude théorique de la complexité en temps démontre une tendance exponentielle dans le pire des cas (si la grille est entièrement vide) ce qui s’explique par le fait que dans ce cas le programme ne peut tout simplement pas résoudre le sudoku, mais pour les autres cas, la tendance reste linéaire et constante également. 

On observe les mêmes tendances entre l’étude théorique et les mesures ce qui démontre que le programme est bel et bien opérationnel et rapide dans la plupart des cas.

Il est également possible d'effectuer un premier classement de difficulté des grilles en fonction du temps d’exécution du programme et du nombre de fonctions appelées pour la résolution de chaques grilles :  

**1 Sudoku 3** à 43 cases à résoudre et 1215 fonctions appelées.

**2 Sudoku 1** à 45 cases à résoudre et 2585 fonctions appelées. 

**3 Sudoku 2** à 52 cases à résoudre et 13723 fonctions appelées.

**4 Sudoku 5** à 58 cases à résoudre et 42629 fonctions appelées.

**5 Sudoku 4** à 57 cases à résoudre et 71928 fonctions appelées. 





**! A faire !**

**1.B Backtracking itératif** 



**1. Analyse théorique.**

1\.1. Complexité temporelle.

1\.2. Complexité spatiale.

**2. Analyse empirique.** 

2\.1. Mesure du temps d’exécution moyen en fonction du nombre d’essais.

2\.2. Mesure du temps d’exécution moyen en fonction du nombre de cases vides.

2\.3 Profilage.

**3. Comparaison de l’étude théorique et empirique.**

**2 Force Brute.**

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
