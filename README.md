# Désambiguiser un mot polysémique par son contexte

La désambiguisation se fait via le champ lexical du mot donné, tel quel calculé via les arcs entre les noeuds du graphe du système lexical RL-fr (voir attribution plus bas). Le système lexical utilisé est un projet en cours et est encore incomplet.

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
