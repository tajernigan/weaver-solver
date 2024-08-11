# Weaver Solver

Welcome to the Weaver Solver repository! This project is dedicated to solving the optimal solution for the online game ["Weaver"](https://wordwormdormdork.com/).

## Demo
![output](https://github.com/user-attachments/assets/bb4a32ca-df31-4329-afbc-31b17595fe94)

## Overview

This project looks to optimize an algorithm to solver the word game "Weaver". The current fastest algorithm is a Bi-Direction BFS which solves 10000 cases in about 2 seconds. There is also a webWeaver module which automates the daily weaver through selenium.

## How to use weaver-solver

1. Clone the repository:
    ```sh
    git clone https://github.com/tajernigan/weaver-solver.git
    cd weaver-solver
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Running testing for weaverSolverBDBFS:
    ```sh
    python -m unittest discover tests
    ```

4. Running webWeaver:
    ```sh
    python src/webWeaver.py
    ```

## Issues

Check the docs directory for documentation or if anything in the program doesn't work as planned.

## Contributing 

There is a TODO.md file in the docs directory which are things im looking to fix / improve in the project. If there are other things you see or think can be improved feel free to submit a pull request or report it in the issues tab, I appreciate any feedback :)
