

#!/bin/bash

for instance_file in ./problems/layouts/* ./problems/layouts/wc3/*; do
    [ -f "$instance_file" ] || continue
    
    echo "========================================="
    echo "Running $instance_file"
    echo "========================================="
    
    echo "Running: hlog-tree-bfs"
    hlogedu-search run -a hlog-tree-bfs -p Pacman -pp file=$instance_file -o graphviz -op file=$instance_file
    
    echo "Running: hlog-graph-bfs"
    hlogedu-search run -a hlog-graph-bfs -p Pacman -pp file=$instance_file -o graphviz -op file=$instance_file
    
    echo "Running: hlog-tree-dfs"
    hlogedu-search run -a hlog-tree-dfs -p Pacman -pp file=$instance_file -o graphviz -op file=$instance_file
    
    echo "Running: hlog-graph-dfs"
    hlogedu-search run -a hlog-graph-dfs -p Pacman -pp file=$instance_file -o graphviz -op file=$instance_file
    
    echo "Running: hlog-tree-ucs"
    hlogedu-search run -a hlog-tree-ucs -p Pacman -pp file=$instance_file -o graphviz -op file=$instance_file
    
    echo "Running: hlog-graph-ucs"
    hlogedu-search run -a hlog-graph-ucs -p Pacman -pp file=$instance_file -o graphviz -op file=$instance_file
    
    echo "Running: hlog-graph-astar (EuclideanHeuristic)"
    hlogedu-search run -a hlog-graph-astar -p Pacman -pp file=$instance_file -hr EuclideanHeuristic -o graphviz -op file=$instance_file
    
    echo "Running: hlog-graph-astar (ManhattanHeuristic)"
    hlogedu-search run -a hlog-graph-astar -p Pacman -pp file=$instance_file -hr ManhattanHeuristic -o graphviz -op file=$instance_file
    
    echo "Running: hlog-tree-astar (EuclideanHeuristic)"
    hlogedu-search run -a hlog-tree-astar -p Pacman -pp file=$instance_file -hr EuclideanHeuristic -o graphviz -op file=$instance_file
    
    echo "Running: hlog-tree-astar (ManhattanHeuristic)"-o graphviz -op file=$instance_file
    hlogedu-search run -a hlog-tree-astar -p Pacman -pp file=$instance_file -hr ManhattanHeuristic -o graphviz -op file=$instance_file
    
    echo ""
done

echo "Done!"