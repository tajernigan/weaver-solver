import time
import json

f = open('/Users/tajernigan/codingProjects/weaver-solver/longestDistanceGraph/fourLettersDict.txt')

words = [word for word in f]

def one_letter_off(word_one, word_two):
    return sum([word_one[i] == word_two[i] for i in range(4)]) == 3

t1 = time.time()
graph = {}
for word in words:
    word = word.strip()
    graph[word] = []
    for wordy in words:
        if one_letter_off(word, wordy):
            graph[word].append(wordy.strip())
t2 = time.time()

print(f'this took {(t2 - t1):.5f} seconds to create')

with open('set.json', 'w') as outfile:
   json.dump(graph, outfile)

