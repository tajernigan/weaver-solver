import json
import time
def create_set_n_branches_away(word, n):
    graph['explored'] += word
    graph['explored'] = list(set(graph['explored']))
    if n == 0:
        return set(word)
    current_words = set()
    for words in word:
        for item in graph[words]:
            if item not in graph['explored']:
                current_words.add(item)
    return create_set_n_branches_away(current_words, n - 1)

with open('graph.json', 'r') as infile:
    graph = json.load(infile)

longestDistanceGraph = {}

with open("fourLettersDict.txt", "r") as f:
    word_list = [word.strip() for word in f]
t1 = time.time()
for word in word_list:
    t3 = time.time()
    for i in range(25):
        graph['explored'] = []
        if create_set_n_branches_away([word], i+1) == set():
            longestDistance = i
            break
    if longestDistance == 0:
        longestDistanceGraph[word] = ['no solution', 0]
    graph['explored'] = []
    longestDistanceGraph[word] = list(create_set_n_branches_away([word], longestDistance)) + [longestDistance]
    t4 = time.time()
    print(f'{word} took {t4-t3} seconds')
t2 = time.time()
print(f'this took {t2-t1} many seconds')
with open('longestDistanceGraph.json', 'w') as outfile:
   json.dump(longestDistanceGraph, outfile)