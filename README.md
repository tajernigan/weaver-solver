# Weaver Solver

Welcome to the Weaver Solver repository! This project consists of two parts both is seperate folders.

## Overview

The Weaver Solver project focuses on solving the optimal solution to the online game "Weaver".

## Folders

### `solutionFinder`

**Description**: 
- This folder contains the Python file that finds the optimal solution to weaver as well as the graph the programs uses in a json file.

**Usage**:
- Inorder to run this Python file to get the desired results make sure that the "graph.json" file is in the directory you are running the python file in.

### `longestDistanceGraph`

**Description**: 
- This folder contains the graph of all four letters words with there longest solutions, meaning the nodes furthest away in terms of the game weaver. 
- It contains the entire 4 letter word dictionary and the code I used to make the graph which requires the "graph.json" file.
- I wouldn't recommend running the python file as the "longestDistanceGraph.json" took about 4 hours to make, so I already did the dirty work of running the program for 4 hours so all you need is the graph.
  

**Usage**: 
- If you would like to look up items in the graph I would recommend using a python file and importing the graph from the json file into the python file. 
- If you have the dictionary of 4 letter words in your directory you can parse through all of them if your interested in getting the statistics of all the longest solutions.
