import time
import json
import statistics

def check_sets(small, large): # used to check if a word from one set is in another
    for word in small:
        if word in large:
            return True
    return False

'''this function recursively checks branches at n depth until it finds a branch where the start and end word share a equal word or have words that are one letter of using 
the "one_letter_off" function, then the function call the "split_path" function which helps split the branches and then calls this function again, this function and "split_path"
call each other back and forth until each nodes is found, thus returning a list of words of the optimal solution'''
def find_shortest_path(start_word, goal, explored):
    start_word, goal = set(start_word), set(goal) # make sure input is correct
    if start_word == set() or goal == set():
        return 'no solution found'
    if (len(start_word) <= len(goal)): # find smaller set
        if check_sets(start_word, goal): 
            pass
    else:
        if check_sets(goal, start_word):
            pass
    return 


#this code loads in a graph with every four letter word as a key with its values being the next possible nodes (words that are one letter off)
with open('graph.json', 'r') as infile:
    graph = json.load(infile)
graph['explored'] = set()

#this block of code takes user input and then gives the solution and how long it took to find it
# print("This is a program that can solve the optimal solution to the online game weaver, if you have never heard of this game the url is https://wordwormdormdork.com/")
# print()
# start_word = input('Enter the start word: ')
# end_word = input('Enter the end word: ')
# t1 = time.time()
# solution = find_shortest_path(start_word, end_word, 1)
# t2 = time.time()
# print(f'optimal solution = {len(solution) - 1}')
# print(solution)
# print(f'this took {(t2 - t1):.5f} seconds to solve')
# print()

# t1 = time.time()
# solution = find_shortest_path('tilt', 'tilt', 1) # optimal = 0
# solution = find_shortest_path('hilt', 'tilt', 1) # optimal = 1
# solution = find_shortest_path('hill', 'tilt', 1) # optimal = 2
# solution = find_shortest_path('hall', 'tilt', 1) # optimal = 3
# solution = find_shortest_path('plat', 'form', 1) # optimal = 4
# solution= find_shortest_path('left', 'turn', 1) #optimal = 5
# solution = find_shortest_path('very', 'much', 1) # optimal = 6
# solution= find_shortest_path('swan', 'lake', 1) #optimal = 7
# solution = find_shortest_path('anta', 'unau', 1) # optimal = 8
# solution = find_shortest_path('acta', 'unau', 1) # optimal = 9
# solution = find_shortest_path('abas', 'unau', 1) # optimal = 10
# solution = find_shortest_path('aahs', 'odic', 1) # optimal = 11
# solution = find_shortest_path('aahs', 'unau', 1) #optimal = 12
# solution = find_shortest_path('plat', 'unau', 1) #optimal = 13
# solution = find_shortest_path('star', 'unau', 1) #optimal = 14
# solution = find_shortest_path('ahem', 'unau', 1) #optimal = 15
# solution = find_shortest_path('eddo', 'unau', 1) #optimal = 16
# solution = find_shortest_path('atap', 'unau', 1) #optimal = 17
# solution = find_shortest_path('chef', 'cook', 1) #optimal = ?
# t2 = time.time()

# print(f'this took {(t2 - t1):.5f} seconds to solve')