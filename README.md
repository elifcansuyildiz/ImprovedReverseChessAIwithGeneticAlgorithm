# Improved Reverse Chess AI with Genetic Algorithm

**Date: December 2017**

   * [Improved Reverse Chess AI with Genetic Algorithm](#improved-reverse-chess-ai-with-genetic-algorithm)
      * [1. Introduction](#1-introduction)
         * [1.1. Genetic Algorithm](#11-genetic-algorithm)
         * [1.2. Chess AI](#12-chess-ai)
         * [1.3. Goal of This Project](#13-goal-of-this-project)
      * [2. Installation](#2-installation)
      * [3. How to Run](#3-how-to-run)
      * [4. Parameters](#4-parameters)
      * [5. Results](#5-results)
      * [6. References](#6-references)




## 1. Introduction

The aim of this project is; ***beating hard AI by using easy AI with the support of heuristic algorithms***. Key-words used in this project are summarized in these three topics: `Genetic Algorithm`, `Chess AI` and `Goal of This Project`. 

### 1.1. Genetic Algorithm

A genetic algorithm is a search heuristic that is inspired by Charles Darwin’s theory of natural evolution. This algorithm reflects the process of natural selection where the fittest individuals are selected for reproduction in order to produce offspring of the next generation.

Five phases are considered in a genetic algorithm.

1. Initial population
2. Fitness function
3. Selection
4. Crossover
5. Mutation

### 1.2. Chess AI

- Reverse Chess Game
- Alpha-Beta Pruning
- Minimax
- Simple Evaluation Function
- Piece Square Table
- Automated Tuning

### 1.3. Goal of This Project

Finding best piece-square-table and using the table with easy AI against hard AI.



## 2. Installation

```bash
$ sudo apt install python3 python3-pip
$ pip3 install python-chess==0.25.1 numpy --user
```



## 3. How to Run

There are various options to train AI and play with different scenarios.

```bash
$ cd reverse_chess_ai
$ python3 start_game.py
```



## 4. Results

Some results are presented in the `results.md` file.



## 5. References

- Genetic Algorithm: https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3
- Minimax & Alpha-Beta Pruning: https://medium.freecodecamp.org/simple-chess-ai-step-by-step-1d55a9266977
- Evaluation Function: https://chessprogramming.wikispaces.com/Simplified+evaluation+function
- https://python-chess.readthedocs.io/en/v0.22.0/uci.html
- Piece Square Table: http://www.chessbin.com/post/Piece-Square-Table
- https://chessprogramming.wikispaces.com/Automated+Tuning
- Python Multiprocessing: https://docs.python.org/2/library/multiprocessing.html
