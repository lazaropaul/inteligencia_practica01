#!/bin/bash

# Simple benchmark script for search algorithms

echo "Starting benchmark..."
echo "Problem,Algorithm,N_Queens,Seed,Output" > results.csv

# Algorithms to test
ALGORITHMS=(
    "hlog-graph-ucs"
    "hlog-graph-bfs"
    "hlog-graph-dfs"
    "hlog-tree-ucs"
    "hlog-tree-bfs"
    "hlog-tree-dfs"
    "hlog-tree-astar -hr RepairHeuristic"
    "hlog-graph-astar -hr RepairHeuristic"
)

# N-Queens: 4 to 10, seeds 1 to 5
for n in 4 5 6 7 8 9 10; do
    for seed in 1 2 3 4 5; do
        for algo in "${ALGORITHMS[@]}"; do
            algo_name=$(echo $algo | cut -d' ' -f1)
            echo "Running N-Queens n=$n seed=$seed with $algo_name..."
            output=$(timeout 10 hlogedu-search run -a $algo -o pygame -p NQueensIR -pp n_queens=$n -pp seed=$seed 2>&1)
            echo "NQueens,$algo_name,$n,$seed,\"$output\"" >> results.csv
        done
    done
done

# Kiwis-and-Dogs
for algo in "${ALGORITHMS[@]}"; do
    algo_name=$(echo $algo | cut -d' ' -f1)
    echo "Running Kiwis-and-Dogs with $algo_name..."
    output=$(timeout 10 hlogedu-search run -a $algo -o graphviz -op file="hola.png" -p kiwis-and-dogs 2>&1)
    echo "Kiwis,$algo_name,N/A,N/A,\"$output\"" >> results.csv
done

echo "Done! Results saved to results.csv"