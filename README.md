# Désambiguïser des homonymes et mots polysémiques par le contexte

La désambiguïsation se fait via le champ lexical du mot donné, tel quel calculé via les arcs entre les noeuds du graphe du système lexical RL-fr (voir attribution plus bas). Le système lexical utilisé est un projet en cours et est encore incomplet.

## Exemples

    somme → Cette somme d'argent est considérable
    somme → Je n'ai pas assez dormi la nuit passée, je vais aller faire un petit somme
    somme → En additionnant deux nombres, on obtient une somme

    volume → Ce livre est divisé en 13 volumes
    volume → Le volume d'une sphère est calculable via une formule simple

    avocat → L'avocat est un fruit qui se mange bien
    avocat → Il me faut un bon avocat pour me représenter

## Attribution

L'algorithme utilise le graphe du Réseau Lexical du Français (RL-fr)

Veronika Lux-Pogodalla, Alain Polguère. Construction of a French Lexical Network: Methodological Issues. First International Workshop on Lexical Resources, WoLeR 2011, Aug 2011, Ljubljana, Slovenia. pp. 54-61, 2011. Analyse et traitement informatique de la langue française - UMR 7118 (ATILF) (2017). Réseau Lexical du Français (RL-fr) [Lexique]. ORTOLANG (Open Resources and TOols for LANGuage) - www.ortolang.fr, https://hdl.handle.net/11403/lexical-system-fr/v1.

Téléchargement ici : https://www.ortolang.fr/market/lexicons/lexical-system-fr/v1


## Bugs/Améliorations

- Les mots sont considérés un à un, les clichés linguistiques, expressions figées, etc. stockés dans le système lexical ne sont pas pris en compte

- Avec un peu plus de travail, le genre des mots pourrait être utilisé pour améliorer la désambiguïsation : "une somme" vs "un somme" aiderait à distinguer et le genre des entités du graphe est connu

- Le champ lexical pourrait être étendu pour considérer (avec un plus faible poid) les champs lexicaux des mots du champ lexical trouvé :

```
Contexte : Le son et l'avoine sont tous deux délicieux !

Champs lexicaux possibles pour son:
	- céréale
	- timbre, stridence, coup, vrombissement, cri, sonore, volume, canard, réverbération

Correspondance :
	Ambigu, aucune conclusion
```

Alors qu'on a :

```
Champs lexicaux possibles pour *céréale*:
	- avoine, flocon, son, mil, blé
```

`avoine` est donc connecté à `son` via un noeud intermédiaire, la désambiguisation pourrait être possible.
