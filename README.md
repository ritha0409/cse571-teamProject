Bases Mazes = mediumMaze, bigMaze, contoursMaze, openMaze, smallMaze, tinyMaze

New Mazes = bigMaze1, bigMaze2, bigMaze3, bigMaze4, bigMaze5, bigMaze6, bigMaze7, bigMaze8, bigMaze9, bigMaze10, contoursMaze1, contoursMaze2, contoursMaze3

The new mazes have the same layout as the base mazes they are named after, but have different food positions, pacman positions or both.


#######################################
For using the bidirectional search on a base maze use the command:
python pacman.py -l bigMaze -p SearchAgent -a fn=bi,heuristic=manhattanHeuristic -z 0.5

This will visually show the expanded nodes and the path the pacman takes.


#######################################
For using the bidirectional search on a new maze use the command:
python pacman.py -l bigMaze5 -p SearchAgent -a fn=bi,heuristic=manhattanHeuristicSingle,prob=SingleFoodSearchProblem -z 0.5

For using another search method on a new maze use the command:
python pacman.py -l bigMaze5 -p SearchAgent -a fn=bfs,prob=SingleFoodSearchProblem -z 0.5

Astar should be ran like the bi with fn=astar and not fn=bi. 
The nodes expanded are not shown here, but the path is still shown.


#######################################
For aquiring the TestingOutput.txt and TestingOutput.csv, run the command:
python run_different_environments.py

This runs bfs, dfs, ucs, astar, and the bidirectional searches on the base maps, additionally created maps, and the corners maps (only for astar and bidirectional search).
Looking inside of TestingOutput.txt or TestingOutput.csv shows the nodes expanded, time taken, and path costs of the algorithms.


 
