import time
import json

def one_letter_off(word_one, word_two):
    if len(word_one) != len(word_two):
        return False
    difference_count = 0
    for i in range(len(word_one)):
        if word_one[i] != word_two[i]:
            difference_count += 1
        if difference_count > 1:
            return False
    return difference_count == 1

if __name__ == "__main__":

    f = open('five_letter_words.txt')

    words = [word.strip() for word in f]

    t1 = time.time()
    graph = {}

    for word in words:
        if word not in graph:
            graph[word] = []
        for other_word in words:
            if word != other_word and one_letter_off(word, other_word):
                graph[word].append(other_word)
    t2 = time.time()

    print(f'this took {(t2 - t1):.5f} seconds to create')

    with open('words5.json', 'w') as outfile:
        json.dump(graph, outfile)

