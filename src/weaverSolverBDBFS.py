import time
import json

def backTrack(prevStart, prevEnd, middle):
    start = []
    end = [middle]
    word = middle
    while word != "":
        end.append(prevEnd[word])
        word = prevEnd[word]
    word = middle
    while word != "":
        start.insert(0, prevStart[word])
        word = prevStart[word]
    return start[1:] + end[:-1]

def find_shortest_path(start, end, graph):
    prevStart, prevEnd = {start: ""}, {end: ""}
    startMap, endMap = {start}, {end}
    startExplored, endExplored = set(), set()
    while startMap and endMap:
        nextStart, nextEnd = set(), set()

        for word in startMap:
            startExplored.add(word)
            if word in endMap:
                return backTrack(prevStart, prevEnd, word)
            for neighbor in graph[word]:
                if neighbor not in startExplored and neighbor not in startMap:
                    prevStart[neighbor] = word
                    nextStart.add(neighbor)
        startMap = nextStart

        for word in endMap:
            endExplored.add(word)
            if word in startMap:
                return backTrack(prevStart, prevEnd, word)
            for neighbor in graph[word]:
                if neighbor not in endExplored and neighbor not in endMap:
                    prevEnd[neighbor] = word
                    nextEnd.add(neighbor)
        endMap = nextEnd

    return None
        



'''this function recursively checks branches at n depth until it finds a branch where the start and end word share a equal word or have words that are one letter of using 
the "one_letter_off" function, then the function call the "split_path" function which helps split the branches and then calls this function again, this function and "split_path"
call each other back and forth until each nodes is found, thus returning a list of words of the optimal solution'''

#this code loads in a graph with every four letter word as a key with its values being the next possible nodes (words that are one letter off)
if __name__ == '__main__':
    with open('graph.json', 'r') as infile:
        map = json.load(infile)



    t1 = time.time()
    print ( find_shortest_path('tilt', 'tilt', map) )# optimal = 0
    print ( find_shortest_path('hilt', 'tilt', map) )# optimal = 1
    print ( find_shortest_path('hill', 'tilt', map) )# optimal = 2
    print ( find_shortest_path('hall', 'tilt', map) )# optimal = 3
    print ( find_shortest_path('plat', 'form', map) )# optimal = 4
    print (find_shortest_path('left', 'turn', map)) #optimal = 5
    print ( find_shortest_path('very', 'much', map) )# optimal = 6
    print (find_shortest_path('swan', 'lake', map)) #optimal = 7
    print ( find_shortest_path('anta', 'unau', map) )# optimal = 8
    print ( find_shortest_path('acta', 'unau', map) )# optimal = 9
    print ( find_shortest_path('abas', 'unau', map) )# optimal = 10
    print ( find_shortest_path('aahs', 'odic', map) )# optimal = 11
    print ( find_shortest_path('aahs', 'unau', map) )#optimal = 12
    print ( find_shortest_path('plat', 'unau', map) )#optimal = 13
    print ( find_shortest_path('star', 'unau', map) )#optimal = 14
    print ( find_shortest_path('ahem', 'unau', map) )#optimal = 15
    print ( find_shortest_path('eddo', 'unau', map) )#optimal = 16
    print ( find_shortest_path('atap', 'unau', map) )#optimal = 17
    print ( find_shortest_path('chef', 'cook', map) )#optimal = ?
    t2 = time.time()

    print(f'this took {(t2 - t1):.5f} seconds to solve')