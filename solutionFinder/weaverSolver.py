import time
import json

def one_letter_off(word_one, word_two): #this function checks if a word is only one letter out of place from another word
    counter = 0
    for i in range(len(word_one)):
        if word_one[i] == word_two[i]:
            counter += 1
    if counter == 3:
        return True 
    return False

'''after the two connecting branches are found between the start and end word, this function calls the start function 'find_shortest_path'
which then splits the path into two again and again until all the nodes are 1 node away, thus returning the entire path'''
def split_path(start, end, n):
    if n == 1:
        return [start, end]
    return find_shortest_path(start, end, 1)

#this recursive function returns a set of words that are at an n distance of nodes away from the intitial word, while removing the duplicates to avoid iterating over the same word multiple times
#this function also makes it easy to find solution of n length for a given word
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

'''this function recursively checks branches at n depth until it finds a branch where the start and end word share a equal word or have words that are one letter of using 
the "one_letter_off" function, then the function call the "split_path" function which helps split the branches and then calls this function again, this function and "split_path"
call each other back and forth until each nodes is found, thus returning a list of words of the optimal solution'''
def find_shortest_path(start_word, goal, branch_number):
    if start_word == goal:
        return [start_word]
    if one_letter_off(start_word, goal):
        return [start_word, goal]
    graph['explored'] = []
    current_start_branch = create_set_n_branches_away([start_word], branch_number)
    graph['explored'] = []
    current_goal_branch = create_set_n_branches_away([goal], branch_number)
    if current_start_branch == set() or current_goal_branch == set():
        return ['no solution']
    for words in current_start_branch:
        if words in current_goal_branch:
            path = split_path(start_word, words, branch_number) + split_path(words, goal, branch_number)
            return path[:branch_number] + path[branch_number+1:]
    for words in current_start_branch:
        for item in current_goal_branch:
            if one_letter_off(words, item):
                path = split_path(start_word, words, branch_number) + split_path(item, goal, branch_number)
                return path
    return find_shortest_path(start_word, goal, branch_number + 1)


#this code loads in a graph with every four letter word as a key with its values being the next possible nodes (words that are one letter off)
with open('graph.json', 'r') as infile:
    graph = json.load(infile)
graph['explored'] = []

#this block of code takes user input and then gives the solution and how long it took to find it
print("This is a program that can solve the optimal solution to the online game weaver, if you have never heard of this game the url is https://wordwormdormdork.com/")
print()
start_word = input('Enter the start word: ')
end_word = input('Enter the end word: ')
t1 = time.time()
solution = find_shortest_path(start_word, end_word, 1)
t2 = time.time()
print(f'optimal solution = {len(solution) - 1}')
print(solution)
print(f'this took {(t2 - t1):.5f} seconds to solve')
print()

'''
these are different test cases
#solution = find_shortest_path('tilt', 'tilt', 1) # optimal = 0
#solution = find_shortest_path('hilt', 'tilt', 1) # optimal = 1
#solution = find_shortest_path('hill', 'tilt', 1) # optimal = 2
#solution = find_shortest_path('hall', 'tilt', 1) # optimal = 3
#solution = find_shortest_path('plat', 'form', 1) # optimal = 4
#solution= find_shortest_path('left', 'turn', 1) #optimal = 5
#solution = find_shortest_path('very', 'much', 1) # optimal = 6
#solution= find_shortest_path('swan', 'lake', 1) #optimal = 7
#solution = find_shortest_path('anta', 'unau', 1) # optimal = 8
#solution = find_shortest_path('acta', 'unau', 1) # optimal = 9
#solution = find_shortest_path('abas', 'unau', 1) # optimal = 10
#solution = find_shortest_path('aahs', 'odic', 1) # optimal = 11
#solution = find_shortest_path('aahs', 'unau', 1) #optimal = 12
#solution = find_shortest_path('plat', 'unau', 1) #optimal = 13
#solution = find_shortest_path('star', 'unau', 1) #optimal = 14
#solution = find_shortest_path('ahem', 'unau', 1) #optimal = 15
#solution = find_shortest_path('eddo', 'unau', 1) #optimal = 16
#solution = find_shortest_path('atap', 'unau', 1) #optimal = 17
solution = find_shortest_path('chef', 'cook', 1) #optimal = ?
'''