# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
	"""
	This class outlines the structure of a search problem, but doesn't implement
	any of the methods (in object-oriented terminology: an abstract class).

	You do not need to change anything in this class, ever.
	"""

	def getStartState(self):
		"""
		Returns the start state for the search problem.
		"""
		util.raiseNotDefined()

	def isGoalState(self, state):
		"""
		  state: Search state

		Returns True if and only if the state is a valid goal state.
		"""
		util.raiseNotDefined()

	def getSuccessors(self, state):
		"""
		  state: Search state

		For a given state, this should return a list of triples, (successor,
		action, stepCost), where 'successor' is a successor to the current
		state, 'action' is the action required to get there, and 'stepCost' is
		the incremental cost of expanding to that successor.
		"""
		util.raiseNotDefined()

	def getCostOfActions(self, actions):
		"""
		 actions: A list of actions to take

		This method returns the total cost of a particular sequence of actions.
		The sequence must be composed of legal moves.
		"""
		util.raiseNotDefined()


def tinyMazeSearch(problem):
	"""
	Returns a sequence of moves that solves tinyMaze.  For any other maze, the
	sequence of moves will be incorrect, so only use this for tinyMaze.
	"""
	from game import Directions
	s = Directions.SOUTH
	w = Directions.WEST
	return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
	"""
	Search the deepest nodes in the search tree first.

	Your search algorithm needs to return a list of actions that reaches the
	goal. Make sure to implement a graph search algorithm.

	To get started, you might want to try some of these simple commands to
	understand the search problem that is being passed in:

	print("Start:", problem.getStartState())
	print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
	print("Start's successors:", problem.getSuccessors(problem.getStartState()))
	"""
	"*** YOUR CODE HERE ***"
	from util import Stack
	
	pacmanFringe = Stack()
	visitedNodes = []
	path = []
	
	startState = problem.getStartState()
	
	if problem.isGoalState(startState):
		return []
	
	pacmanFringe.push((startState,visitedNodes,path))
	
	while not pacmanFringe.isEmpty():
		currentState, visitedNodes, path = pacmanFringe.pop()
		visitedNodes.append(currentState)
		if problem.isGoalState(currentState):
			return path
		for nextState in problem.getSuccessors(currentState):
			if nextState[0] not in visitedNodes:
				currentpath = path + [nextState[1]]
				pacmanFringe.push((nextState[0],visitedNodes,currentpath))
			

def breadthFirstSearch(problem):
	"""Search the shallowest nodes in the search tree first."""
	"*** YOUR CODE HERE ***"
	
	from util import Queue
	
	queue = Queue()
	
	visitedNodes = []
	path = []
	
	startState = problem.getStartState()
	
	queue.push((problem.getStartState(),[]))
	
	if problem.isGoalState(startState):
		return []
		
	while (True):
		if queue.isEmpty():
			return []
		
		positionState, path = queue.pop()
		visitedNodes.append(positionState)
		
		if problem.isGoalState(positionState):
			return path
			
		nextState = problem.getSuccessors(positionState)
		
		if nextState:
			for node in nextState:
				if node[0] not in visitedNodes and node[0] not in (state[0] for state in queue.list):
					newPath = path + [node[1]]
					queue.push((node[0],newPath))
		

def uniformCostSearch(problem):
	"""Search the node of least total cost first."""
	"*** YOUR CODE HERE ***"
	pacmanFringe=util.PriorityQueue()
	
	visitedNodes=[]
	path=[]
	
	startState=problem.getStartState()
	startCost= len(path)
	
	if problem.isGoalState(startState):
		return []
	
	pacmanFringe.push((startCost,startState,visitedNodes,path),startCost)
	
	while not pacmanFringe.isEmpty():
		currentCost, currentState, visitedNodes, path = pacmanFringe.pop()
		if currentState not in visitedNodes:
			visitedNodes.append(currentState)
			if problem.isGoalState(currentState):
				return path
			for nextState in problem.getSuccessors(currentState):
				if nextState[0] not in visitedNodes:
					currentpath = path + [nextState[1]]
					nextCost= currentCost + nextState[2]
					pacmanFringe.push((nextCost,nextState[0],visitedNodes,currentpath),nextCost)

def nullHeuristic(state, problem=None):
	"""
	A heuristic function estimates the cost from the current state to the nearest
	goal in the provided SearchProblem.  This heuristic is trivial.
	"""
	return 0

def aStarSearch(problem, heuristic=nullHeuristic):
	"""Search the node that has the lowest combined cost and heuristic first."""
	"*** YOUR CODE HERE ***"
	pacmanFringe=util.PriorityQueue()
	
	visitedNodes=[]
	path=[]
	
	startState=problem.getStartState()
	  
	startCost= len(path)
	startingHeuristicCost=heuristic(startState,problem)
	
	if problem.isGoalState(startState):
		return []
	
	startTotal= startCost + startingHeuristicCost
	pacmanFringe.push((startTotal,startCost,startState,path),startTotal)
	
	while not pacmanFringe.isEmpty():
		
		currentTotal, currentCost, currentState, path = pacmanFringe.pop()
		
		if currentState not in visitedNodes:
			visitedNodes.append(currentState)
			if problem.isGoalState(currentState):
				return path
			for nextState in problem.getSuccessors(currentState):
				if nextState[0] not in visitedNodes:
					currentpath = path + [nextState[1]]
					nextCost= currentCost + nextState[2]
					nextHeuristicCost=heuristic(nextState[0],problem)
					nextTotalCost= nextCost + nextHeuristicCost
					pacmanFringe.push((nextTotalCost,nextCost,nextState[0],currentpath),nextTotalCost)

def bidirection(problem,heuristic):

	from searchAgents import FoodSearchProblem,CornersProblem
	from searchAgents import foodHeuristic

	#heuristic=foodHeuristic

	q1 = util.PriorityQueue()
	temp_q1 = []
	q2 = util.PriorityQueue()
	temp_q2 = []
	explorednode1 = set()
	explorednode2 = set()
	startnode = problem.getStartState()
	# endnode = problem.goal

	if type(problem) == FoodSearchProblem:# or type(problem) == CornersProblem:
		for pair in (problem.start[1].asList()):
			a,b = pair
			endnode = ((a,b),startnode[1])
	else:
		endnode = problem.goal

	q1.push((startnode,[],0),0+heuristic(startnode,problem))
	q2.push((endnode, [],0),0+heuristic(endnode,problem,back=True))
	while q1.isEmpty() is not True and q2.isEmpty() is not True:


		forward_min_priority = q1.pop()
		backward_min_priority = q2.pop()

		cost_forward = forward_min_priority[2]
		cost_backward = backward_min_priority[2]

		q1.push(forward_min_priority,cost_forward+heuristic(forward_min_priority[0],problem))
		q2.push(backward_min_priority,cost_backward+heuristic(backward_min_priority[0],problem,back=True))

		if cost_forward < cost_backward:
			currentnode, direction,cost = q1.pop()
			if currentnode not in explorednode1:
				explorednode1.add(currentnode)
				if problem.isGoalState(currentnode) or (currentnode in temp_q2):
					while q2.isEmpty() == False:
						node, direc,cost = q2.pop()
						if node == currentnode:
							direc.reverse()
							solution = direction + ulta(direc)
							return solution
				for(successor, action, stepCost) in problem.getSuccessors(currentnode):
					q1.push((successor, direction + [action],cost+stepCost),max(cost+stepCost+heuristic(successor,problem),2*(cost+stepCost)))
					temp_q1.append(successor)
		else:
			currentnode, direction,cost = q2.pop()
			if currentnode not in explorednode2:
				explorednode2.add(currentnode)
				if currentnode in temp_q1:
					while q1.isEmpty() == False:
						node, direc,cost = q1.pop()
						if node == currentnode:
							direction.reverse()
							solution = direc + ulta(direction)
							return solution
				for(successor, action, stepCost) in problem.getSuccessors(currentnode):
					q2.push((successor, direction + [action],cost+stepCost),max(cost+stepCost+heuristic(successor,problem,back=True),2*(cost+stepCost)))
					temp_q2.append(successor)

					
def ulta(direction):
	'''
	It reverses the path from the goal to the point where the two path meets.
	'''
	j = []
	for i in direction:
		# Convert NORTH to SOUTH
		if i == 'North':
			j.append('South')
		# Convert SOUTH to NORTH
		elif i == 'South':
			j.append('North')
		# Convert EAST to WEST
		elif i== 'East':
			j.append('West')
		# Convert WEST to EAST
		else:
			j.append('East')
	return j

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
bi = bidirection