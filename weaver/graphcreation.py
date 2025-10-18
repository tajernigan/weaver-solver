import time
import pickle as pkl
from pathlib import Path
from collections import defaultdict
import networkx as nx
import sys

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def words_list(word_length):
    word_list = []
    with (DATA_DIR / "dictionary.txt").open('r') as words:
        for word in words:
            word = word.strip()
            if len(word) == word_length: # return words of the corresponding length
                word_list.append(word)
    return word_list

# returns a networkx Graph of letters of the given word length as verticies with bidirectional edges between words that are one letter off
def load_graph(word_length):
    # check if the graph has already been created
    pickle_path = DATA_DIR / f'words{word_length}.pkl'
    if pickle_path.exists():
        # load and return graph if already exists
        with pickle_path.open('rb') as f:
            G = pkl.load(f)
            return G

    # if graph does not exist for that word length yet
    G = nx.Graph()
    words = words_list(word_length=word_length) # scrape all n letter words from dictionary
    buckets_dict = defaultdict(list) # init hashtable for buckets of words

    # add words into correct buckets
    for word in words:
        for i in range(len(word)):
            bucket = word[:i] + "*" + word[i+1:] # create bucket for each possible one letter of combination (i.e) "help" -> "*elp", "h*lp" etc.
            buckets_dict[bucket].append(word)
    
    # iterate and add edges for each word in the created buckets
    for word in words: 
        G.add_node(word) # add node initialy in case word has no neighbors
        for i in range(len(word)):
            bucket = word[:i] + "*" + word[i+1:] # create bucket for each possible one letter of combination (i.e) "help" -> "*elp", "h*lp" etc.
            for neighbor in buckets_dict[bucket]:
                if word != neighbor:
                    G.add_edge(word, neighbor) # add bidirection
    
    # load graph into 
    with pickle_path.open("wb") as f:
        pkl.dump(G, f)
    
    return G # return newly created graph
    
if __name__ == "__main__":

    args = sys.argv
    if len(args) < 2:
        print("need to specifiy word_length as command line arg")
        exit()
    
    word_length = int(args[1])

    t1 = time.time()
    
    G = load_graph(word_length=word_length)
    num_edges = G.size()
    print(f"Number of edges (size of graph): {num_edges}")
    print(f'Number of verticies: {len(G)}')

    t2 = time.time()

    print(f'load took {(t2 - t1):.5f} seconds')
