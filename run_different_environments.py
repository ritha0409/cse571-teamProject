import scipy.stats
import csv
from pacman import readCommand, runGames

def generateCommands():
	layouts = ["mediumMaze","bigMaze","contoursMaze","openMaze","smallMaze", "testMaze","tinyMaze","tinyCorners","mediumCorners","bigCorners"]
	function_types = ["bfs","dfs","ucs","astar"]#bi

	commands = []
	for l in layouts:
		for ft in function_types:
			if (ft == "astar" or ft == "bi") and "Corners" in l:
				command = f"-l {l} -p SearchAgent -a fn={ft},prob=CornersProblem,heuristic=cornersHeuristic -q"
				commands.append(command.split(" "))
			elif ft == "astar" or ft == "bi":
				command = f"-l {l} -p SearchAgent -a fn={ft},heuristic=manhattanHeuristic -q"
				commands.append(command.split(" "))
			elif not "Corners" in l:
				command = f"-l {l} -p SearchAgent -a fn={ft} -q"
				commands.append(command.split(" "))
				# command = f"-l {l} -p SearchAgent -a fn={ft},prob=CornersProblem -q"
				# commands.append(command.split(" "))

	# print(commands)
	return commands

if __name__ == '__main__':
	run_commands = generateCommands()

	with open('Results.csv', 'w') as Results:
		writer = csv.writer(Results, delimiter=',', quotechar = '|')
		writer.writerow(["Testing"])


	for command in run_commands:
		with open('Results.csv', 'a') as Results:
			writer = csv.writer(Results, delimiter=',')
			writer.writerow(["Layout",command[1],"function",command[5][3:]])
		args = readCommand( command ) # Get game components based on input
		runGames( **args )
		# print("\n\n")

	testingResults = dict()
	with open('Results.csv') as testData:
		testRows = list(csv.reader(testData, delimiter=',')) 

		current_map = ""
		currentMapRow = []
		for row in testRows:
			if len(row) > 1:
				if row[0] == "Layout":
					if not currentMapRow == []:
						currentMapValues = testingResults.get(current_map)
						if currentMapValues == None:
							currentMapValues = []
						currentMapValues.append(currentMapRow)
						testingResults[current_map] = currentMapValues
					current_map = row[1]
					currentMapRow = [row[3]]
				else:
					currentMapRow.append(row[1])

		
	with open("TestingOutput.txt", "w") as Results:
		writer = csv.writer(Results, delimiter=',',quotechar = '*')

		for key in testingResults.keys():
			writer.writerow([key])
			for row in testingResults[key]:
				writer.writerow([f"Function: {row[0]}\tPath Cost: {row[1]}\tTime Taken: {row[2]}\tNodes Expanded: {row[3]}\tAverage Score: {row[4]}\tWin Rate: {row[5]}"])
