#!/usr/bin/python3

from functools import reduce
import csv
import sys
import os

basepath = os.path.dirname(os.path.abspath(__file__)) + '/'

def load_csv(path, hash):
    out = {}

    with open(basepath + path, 'r') as f:
        for line in csv.DictReader(f, delimiter="\t", quotechar='"'):
            out[line[hash]] = line

    return out

# Lexies
nodes = load_csv('lexical-system-fr/3/ls-fr-V1/01-lsnodes.csv', 'id')

# Vocables
entries = load_csv('lexical-system-fr/3/ls-fr-V1/02-lsentries.csv', 'id')

entry_nodes = {}

for node_id in nodes:
    e = nodes[node_id]['entry']
    
    if e not in entry_nodes:
        entry_nodes[e] = []
    
    entry_nodes[e].append(node_id)

# Noeuds associés à un mot
words = {}
with open(basepath + 'lexical-system-fr/3/ls-fr-V1/08-lswordforms.csv', 'r') as f:
    for line in csv.DictReader(f, delimiter="\t", quotechar='"'):
        w = line['signifier']

        if w not in words:
            words[w] = []
        
        words[w].append(line['id'])

# Liens entre les lexies
links = {}
with open(basepath + 'lexical-system-fr/3/ls-fr-V1/13-lslf-rel.csv', 'r') as f:
    for line in csv.DictReader(f, delimiter="\t", quotechar='"'):
        target = line['target']
        source = line['source']

        if target not in links:
            links[target] = []

        if source not in links:
            links[source] = []

        links[source].append(target)
        links[target].append(source)

def node_relations(node):
    return links[node]

def word_nodes(word):
    return words[word]

def node_word(n):
    entry = nodes[n]['entry']

    return entries[entry]['name']

def champs_lexicaux(mot):
    out = {}

    for node in word_nodes(mot):
        out[node] = set(node_relations(node))

    return out

def score(phrase, cible): # todo : contexte
    phrase = set(phrase)

    champs = champs_lexicaux(cible)

    scores = {}

    for node, relations in champs.items():
        scores[node] = len(relations.intersection(phrase).difference(set([cible])))
        
    return scores

if __name__ == '__main__':
    # cible = sys.argv[1]
    # phrase = sys.argv[2:]
    cible = input('Mot à désambiguiser : ').lower()
    phrase = set(filter(lambda x: x, input('Phrase de contexte : ')
                        .lower()
                        .replace('.', ' ')
                        .replace(',', ' ')
                        .replace("'", ' ')
                        .split(' ')))

    phrase_possible_nodes = []

    for w in phrase:
        if w in words:
            phrase_possible_nodes.extend(words[w])
    
    s = score(phrase_possible_nodes, cible)
    print("Champs lexicaux possibles pour " + cible + ":")
    for node, val in s.items():
        print("\t- " + ', '.join(set(map(node_word, node_relations(node)))))

    best = reduce(lambda acc, node: (s[node], node) if acc[0] < s[node] else acc, s, (float("-inf"), None))

    occurences, node = best

    print("Correspondance :")
    if occurences == 0:
        print("\tAmbigu, aucune conclusion")
    else:
        print('\tNoeud #' + node)
        print("\t" + ', '.join(set(map(node_word, node_relations(node)))))

