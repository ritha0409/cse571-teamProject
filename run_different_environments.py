import scipy.stats
import csv
from pacman import readCommand, runGames

def generateCommands():
	layouts = ["mediumMaze","bigMaze","contoursMaze","openMaze","smallMaze","tinyMaze"]#,["tinyCorners","mediumCorners","bigCorners"]
	layouts = layouts + [ f"bigMaze{i}" for i in range(1,11)]
	layouts = layouts + [f"contoursMaze{i}" for i in range(1,4)]
	function_types = ["bfs","dfs","ucs","astar","bi"]

	commands = []
	for l in layouts:
		for ft in function_types:
			if (ft == "astar" or ft == "bi") and "Corners" in l:
				command = f"-l {l} -p SearchAgent -a fn={ft},prob=CornersProblem,heuristic=cornersHeuristic -q"
				commands.append(command.split(" "))
			elif ft == "astar" or ft == "bi":
				command = f"-l {l} -p SearchAgent -a fn={ft},prob=FoodSearchProblem,heuristic=foodHeuristic -q"    #foodHeuristic      manhattanHeuristic
				commands.append(command.split(" "))
			elif not "Corners" in l:
				command = f"-l {l} -p SearchAgent -a fn={ft},prob=FoodSearchProblem -q"
				commands.append(command.split(" "))


	# print(commands)
	return commands
	#Fixed everything to be able to test bi with a heuristic and compare its efforts to the other search methods. Can be run via calling the run_different_environments.py file and writes to TestOutputs

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
		print(command)
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
		currentMapValues = testingResults.get(current_map)
		if currentMapValues == None:
			currentMapValues = []
		currentMapValues.append(currentMapRow)
		testingResults[current_map] = currentMapValues
		
	scores_by_function = dict()
	with open("TestingOutput.txt", "w") as Results:
		writer = csv.writer(Results, delimiter=',',quotechar = '*')

		for key in testingResults.keys():
			writer.writerow([key])
			for row in testingResults[key]:
				current_scores = scores_by_function.get(row[0].split(",")[0].replace("*",""))
				if current_scores == None:
					current_scores = []
				current_scores.append([row[1],row[2],row[3],row[4]])
				scores_by_function[row[0].split(",")[0].replace("*","")] = current_scores
				writer.writerow([f"Function: {row[0]}\tPath Cost: {row[1]}\tTime Taken: {row[2]}\tNodes Expanded: {row[3]}\tAverage Score: {row[4]}\tWin Rate: {row[5]}"])

	with open("TestingOutput.csv", "w") as Results:
		writer = csv.writer(Results, delimiter=',',quotechar = '*',lineterminator = '\n')
		writer.writerow(["Maps","bfs path cost","bfs time taken","bfs nodes expanded","bfs average score","dfs path cost","dfs time taken","dfs nodes expanded","dfs average score","ucs path cost","ucs time taken","ucs nodes expanded","ucs average score","astar path cost","astar time taken","astar nodes expanded","astar average score","bi path cost","bi time taken","bi nodes expanded","bi average score"])

		for index,key in enumerate(testingResults.keys()):
			writer.writerow([key]+scores_by_function["bfs"][index]+scores_by_function["dfs"][index]+scores_by_function["ucs"][index]+scores_by_function["astar"][index]+scores_by_function["bi"][index])

