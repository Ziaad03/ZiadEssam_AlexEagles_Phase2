from MazeGenerator import MazeGenerator
from MazeToGraph import MazeToGraph
from MazeSolver import MazeSolver


def main():
    # Define the dimensions of the maze
    row = 8
    col = 8

    # Generate the maze
    mazeGenerator = MazeGenerator(row, col)
    maze,start,goal = mazeGenerator.generateMaze()
    #Print the maze
    print("Generated Maze:")
    mazeGenerator.printMaze()
    
    #convert the maze to a graph, so it can be easier to solve
    mazeToGraph = MazeToGraph()
    graph = mazeToGraph.convertMazeToGraph(maze)

    mazeSolver = MazeSolver()
    # Solve the maze using A* algorithm
    path = mazeSolver.aStarSolution(graph, start, goal)
    if path is None:
        print("No path found, the maze is not solvable")
    else:
        print("Path from start to goal:", path)

main()

   
