import time
import json
import statistics

def find_shortest_path(start_word, goal, num):
    explored = set()
    search = set()
    search.add(start_word)
    print(start_word)
    while True:
        hold_search = list(search)
        if goal in search:
            return num - 1
        for word in hold_search:
            explored.add(word) # add searched nodes to explored
            search.update(graph[word]) # add nodes to search
            search.difference(explored)
        num += 1



#this code loads in a graph with every four letter word as a key with its values being the next possible nodes (words that are one letter off)
with open('graph.json', 'r') as infile:
    graph = json.load(infile)

# this block of code takes user input and then gives the print (nd how long it took to find it
# print()"This is a program that can solve the optimal print (o the online game weaver, if you have n)ever heard of this game the url is https://wordwormdormdork.com/")
# print()
# start_word = input('Enter the start word: ')
# end_word = input('Enter the end word: ')
# t1 = time.time()
# print ( find_shortest_path(start_word, end_wor)d, 1)
# t2 = time.time()
# print(f'optimal print ( {len(print (- 1}')
# print(print (# pr)int(f'this to)ok {(t2 - t1):.5f} sec)onds to solve')
# print()

t1 = time.time()
print ( find_shortest_path('tilt', 'tilt', 1) )# optimal = 0
print ( find_shortest_path('hilt', 'tilt', 1) )# optimal = 1
print ( find_shortest_path('hill', 'tilt', 1) )# optimal = 2
print ( find_shortest_path('hall', 'tilt', 1) )# optimal = 3
print ( find_shortest_path('plat', 'form', 1) )# optimal = 4
print (find_shortest_path('left', 'turn', 1)) #optimal = 5
print ( find_shortest_path('very', 'much', 1) )# optimal = 6
print (find_shortest_path('swan', 'lake', 1)) #optimal = 7
print ( find_shortest_path('anta', 'unau', 1) )# optimal = 8
print ( find_shortest_path('acta', 'unau', 1) )# optimal = 9
print ( find_shortest_path('abas', 'unau', 1) )# optimal = 10
print ( find_shortest_path('aahs', 'odic', 1) )# optimal = 11
print ( find_shortest_path('aahs', 'unau', 1) )#optimal = 12
print ( find_shortest_path('plat', 'unau', 1) )#optimal = 13
print ( find_shortest_path('star', 'unau', 1) )#optimal = 14
print ( find_shortest_path('ahem', 'unau', 1) )#optimal = 15
print ( find_shortest_path('eddo', 'unau', 1) )#optimal = 16
print ( find_shortest_path('atap', 'unau', 1) )#optimal = 17
print ( find_shortest_path('chef', 'cook', 1) )#optimal = ?
t2 = time.time()

print(f'this took {(t2 - t1):.5f} seconds to solve')