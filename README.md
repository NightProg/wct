# smwct
### Présentation
*Smwct*, pour "*Search and Moderation Wizard for the Computer Tree*", ou "*Assistant de recherche et de modération pour l'arborescence d'un ordinateur*",
est comme son nom l'indique un programme ayant pour mission d'aider l'homme dans la recherche et la modération de l'arborescance de son ordinateur. Plus
exactement, *Smwct* permet deux choses : rechercher à partir d'un des endroits pré-suggéré une suite de caractère dans tous les dossiers, sous-dossiers et 
fichier issuent du répertoire initial, choisis par l'utilisateur, **ou**, rechercher et supprimer après confirmation tous les dossiers, sous-dossiers et
fichier issuent du répertoire initial (toujours choisis par l'utilisateur). C'est un logiciel codé uniquement en Python et uniquement dédié aux utilisateurs
Linux.
### Cause
*Smwct* a été imaginé pour rendre plus facile la trouvaille d'un élément dans un répertoire pré-suggéré tels que `/` ou `/home/username/`, nottament pour
se débarasser de tous les fichiers/dossiers restants après la désinstallation d'un logiciel. Il se veut aussi remplacer `grep` qui est un outil à mon sens
trop embigü.
## Technique
### Mise en place de Smwct sur Linux
Avant d'effectuer ce qui suit, assurez vous d'avoit correctement installé Python et Git.

Une fois que vous avez Python sur votre distribution Linux, lancez la commande suivante suivante à la "racine" (`/home/username/`) pour éviter les 
complications lors de l'utilisation de *smwct* :
```
git clone https://github.com/b4-b4/smwct.git
```
La mise en place du logiciel est terminé.
### Rechercher
Théoriquement, si vous avez installé *smwct* à la racine de votre arborescance (`/home/username/`), la procédure devrait être la suivante :
```
cd
python smwct/run.py -s --starting your_character_string
```
En entrant `python smwct/run.py` vous demandez à l'interpréteur python d'exécuter le programme `run.py` qui se trouve dans le répertoire `smwct/`. Ensuite, 
le premier drapeau `-s` signifi que vous avez envie d'effectuer une recherche. Le second drapeau `--starting` **doit** être remplacé par, au choix, les
dreapeaux suivants :
- `--root` : informe que vous souhaitez effectuer la recherche à la racine absolue de votre ordinateur, à savoir `/`.
- `--session` : informe que vous souhaitez effectuer la recherche à la racine de votre "séssion", soit `/home/username/`.
- `--anywhere` : effectue la recherche à la racine absolue et la racine de votre session (`--root` + `--session`). Cette commande peut nécessiter un temps considérable, vraiment.

Ensuite, `your_character_string` **doit** être remplacé par l'élément que vous voulez rechercher dans le second drapeau (`--session`, `--root` or `--anywhere`). Attention, `your_character_string` n'est pas l'élément qui est cherché à proprement parler, c'est l'élément recherché dans les différents dossiers, sous-dossiers et fichier du deuxième drapeau. Par exemple, cette ligne de commande
```
python smwct/run.py -s --root a
```
retournera peut être
```
/etc/gra.o
/var/
/var/test/allocation/
```
car `etc/gra.o` contient un `a` dans `gra.o`, `/var/` car `var` contient `a`, etc.
