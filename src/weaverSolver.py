import time
from graphcreation import load_graph

class WeaverSolver:

    def __init__(self, word_length):
        self.word_length = word_length
        self.G = load_graph(word_length=word_length)

    def backTrack(self, prevStart, prevEnd, middle):
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

    def find_shortest_path(self, start, end):
        
        if len(start) != len(end): # if words not of the same length solution is not possible
            return None

        if len(start) != self.word_length:
            print(f"weaver solver is for words of length: {self.word_length}")
            return None

        prevStart, prevEnd = {start: ""}, {end: ""}
        startMap, endMap = {start}, {end}
        startExplored, endExplored = set(), set()
        while startMap and endMap:
            nextStart, nextEnd = set(), set()

            for word in startMap:
                startExplored.add(word)
                if word in endMap:
                    return self.backTrack(prevStart, prevEnd, word)
                for neighbor in self.G.neighbors(word):
                    if neighbor not in startExplored and neighbor not in startMap:
                        prevStart[neighbor] = word
                        nextStart.add(neighbor)
            startMap = nextStart

            for word in endMap:
                endExplored.add(word)
                if word in startMap:
                    return self.backTrack(prevStart, prevEnd, word)
                for neighbor in self.G.neighbors(word):
                    if neighbor not in endExplored and neighbor not in endMap:
                        prevEnd[neighbor] = word
                        nextEnd.add(neighbor)
            endMap = nextEnd

        return None

#this code loads in a graph with every four letter word as a key with its values being the next possible nodes (words that are one letter off)
if __name__ == '__main__':
    
    solver = WeaverSolver(word_length=4)

    t1 = time.time()
    print ( solver.find_shortest_path('tilt', 'tilt') )# optimal = 0
    print ( solver.find_shortest_path('hilt', 'tilt') )# optimal = 1
    print ( solver.find_shortest_path('hill', 'tilt') )# optimal = 2
    print ( solver.find_shortest_path('hall', 'tilt') )# optimal = 3
    print ( solver.find_shortest_path('plat', 'form') )# optimal = 4
    print (solver.find_shortest_path('left', 'turn')) #optimal = 5
    print ( solver.find_shortest_path('very', 'much') )# optimal = 6
    print (solver.find_shortest_path('swan', 'lake')) #optimal = 7
    print ( solver.find_shortest_path('anta', 'unau') )# optimal = 8
    print ( solver.find_shortest_path('acta', 'unau') )# optimal = 9
    print ( solver.find_shortest_path('abas', 'unau') )# optimal = 10
    print ( solver.find_shortest_path('aahs', 'odic') )# optimal = 11
    print ( solver.find_shortest_path('aahs', 'unau') )#optimal = 12
    print ( solver.find_shortest_path('plat', 'unau') )#optimal = 13
    print ( solver.find_shortest_path('star', 'unau') )#optimal = 14
    print ( solver.find_shortest_path('ahem', 'unau') )#optimal = 15
    print ( solver.find_shortest_path('eddo', 'unau') )#optimal = 16
    print ( solver.find_shortest_path('atap', 'unau') )#optimal = 17
    print ( solver.find_shortest_path('chef', 'cook') )#optimal = ?
    t2 = time.time()

    print(f'this took {(t2 - t1):.5f} seconds to solve')