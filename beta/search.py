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
	vsn_disp = []
	
	startState = problem.getStartState()
	
	if problem.isGoalState(startState):
		problem.display(vsn_disp)
		return []
	
	pacmanFringe.push((startState,visitedNodes,path))
	
	while not pacmanFringe.isEmpty():
		currentState, visitedNodes, path = pacmanFringe.pop()
		visitedNodes.append(currentState)
		vsn_disp.append(currentState[0])
		if problem.isGoalState(currentState):
			problem.display(vsn_disp)
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
	vsn_disp = []
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
		vsn_disp.append(positionState[0])
		
		if problem.isGoalState(positionState):
			problem.display(vsn_disp)
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
	vsn_disp = []
	
	startState=problem.getStartState()
	startCost= len(path)
	
	if problem.isGoalState(startState):
		return []
	
	pacmanFringe.push((startCost,startState,visitedNodes,path),startCost)
	
	while not pacmanFringe.isEmpty():
		currentCost, currentState, visitedNodes, path = pacmanFringe.pop()
		if currentState not in visitedNodes:
			visitedNodes.append(currentState)
			vsn_disp.append(currentState[0])
			if problem.isGoalState(currentState):
				problem.display(vsn_disp)
				return path
			for nextState in problem.getSuccessors(currentState):
				if nextState[0] not in visitedNodes:
					currentpath = path + [nextState[1]]
					nextCost= currentCost + nextState[2]
					pacmanFringe.push((nextCost,nextState[0],visitedNodes,currentpath),nextCost)

def nullHeuristic(state, problem=None,back=False):
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
	vsn_disp = []
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
			vsn_disp.append(currentState[0])
			if problem.isGoalState(currentState):
				problem.display(vsn_disp)
				return path
			for nextState in problem.getSuccessors(currentState):
				if nextState[0] not in visitedNodes:
					currentpath = path + [nextState[1]]
					nextCost= currentCost + nextState[2]
					nextHeuristicCost=heuristic(nextState[0],problem)
					nextTotalCost= nextCost + nextHeuristicCost
					pacmanFringe.push((nextTotalCost,nextCost,nextState[0],currentpath),nextTotalCost)



class Node:
	def __init__(self, position, actions, cost=0, h=0, pr=0):
		self.pos = position
		self.actions = actions
		self.cost = cost
		self.f = self.cost + h
		self.pr = pr


def bidirection(problem,heuristic):

	from searchAgents import FoodSearchProblem,CornersProblem
	from searchAgents import foodHeuristic

	# heuristic=nullHeuristic

	visitedNodes = []
	q1 = util.PriorityQueue()
	temp_q1 = []
	q2 = util.PriorityQueue()
	temp_q2 = []
	# explorednode1 = set()
	# explorednode2 = set()
	startnode = problem.getStartState()
	# endnode = problem.goal
	endnode = problem.getGoalState()

	explorednode1 = dict()
	explorednode2 = dict()

	dict_q1 = dict()
	dict_q2 = dict()

	U = float('inf')


	# if type(problem) == FoodSearchProblem:
	# 	for pair in (problem.start[1].asList()):
	# 		a,b = pair
	# 		endnode = ((a,b),startnode[1])
	# elif type(problem) == CornersProblem:
	# 	endnode = (problem.corners[3],problem.corners)
	# 	print(endnode)
	# else:
	# 	endnode = problem.goal


	q1_node = Node(startnode, [], 0, 0+heuristic(startnode,problem), 0)
	# q1.push((startnode,[],0),0+heuristic(startnode,problem))
	q1.push(q1_node, q1_node.pr)
	dict_q1[startnode] = q1_node

	q2_node = Node(endnode, [], 0, 0+heuristic(endnode, problem, back=True))
	# q2.push((endnode, [],0),0+heuristic(endnode,problem,back=True))
	q2.push(q2_node, q2_node.pr)
	dict_q2[endnode] = q2_node

	final_ans = []
	prev1 = None
	prev2 = None

	
	while q1.isEmpty() is not True and q2.isEmpty() is not True:


		# forward_min_priority = q1.pop()
		# backward_min_priority = q2.pop()

		forward_min_priority = q1.top()
		backward_min_priority = q2.top()
		C = min(forward_min_priority[2].pr, backward_min_priority[2].pr)

		cost_forward = max(forward_min_priority[2].pr+heuristic(forward_min_priority[2].pos,problem),2*forward_min_priority[2].pr)
		cost_backward = max(backward_min_priority[2].pr+heuristic(backward_min_priority[2].pos,problem,back=True),2*backward_min_priority[2].pr)


		# if U <= max(C, f_f.peek().f, f_b.peek().f, g_f.peek().cost + g_b.peek().cost + eps):
			# open_nodes = len(hash_f) + len(hash_b) + 1
			# closed_nodes = len(closed_f) + len(closed_b)
		if U <= max(C, cost_forward, cost_backward):
			
			open_nodes = len(dict_q1) + len(dict_q2) + 1
			closed_nodes = len(explorednode1) + len(explorednode2)

			print ("Total nodes generated: {}".format(open_nodes + closed_nodes))
			print ("Path Length: {}".format(U))
			return final_ans

		elif U <= C:
			return final_ans

		# q1.push(forward_min_priority,cost_forward)
		# q2.push(backward_min_priority,cost_backward)

		# if cost_forward < cost_backward:
		if forward_min_priority[2].pr < backward_min_priority[2].pr:

			currentnode = q1.pop()
			prev1 = currentnode
			pos = currentnode.pos
			if pos in dict_q1:
				dict_q1.pop(pos)
			explorednode1[pos] = currentnode


			# f_f.remove(curr_node)
			# g_f.remove(curr_node)

			children = problem.getSuccessors(pos)
			for child in children:
				child_pos, child_direction, child_cost = child

				present = None

				if child_pos in dict_q1:
					present = dict_q1[child_pos]

				elif child_pos in explorednode1:
					present = explorednode1[child_pos]

				# if node already exists
				if present is None:

					present_actions = currentnode.actions[:] + [child_direction]
					present_cost = currentnode.cost + child_cost
					present_h = heuristic(child_pos, problem)
					present_pr = present_cost + max(present_h, present_cost)
					present = Node(child_pos, present_actions, present_cost, present_h, present_pr)


				else:
					# and is reached by a shorter path then ignore cuurent path
					if present.cost <= currentnode.cost + child_cost:
						continue

					# remove node from Open U Close Lists
					# open_f.remove(this_node)
					q1.remove(present)

					if child_pos in dict_q1:
						dict_q1.pop(child_pos)
					if child_pos in explorednode1:
						dict_q1.pop(child_pos)

					# f_f.remove(this_node)
					# g_f.remove(this_node)

					# else update the cost
					present.cost = (currentnode.cost + child_cost)
					present.f = present.cost + heuristic(present.pos, problem)
					present.actions = currentnode.actions[:] + [child_direction]

					
				q1.push(present, present.pr)
				dict_q1[child_pos] = present

				if child_pos in dict_q2:
					backward_node = dict_q2[child_pos]
					total = present.cost + backward_node.cost
					U = min(U, total)

					backward_node.actions.reverse()
					backward_actions = ulta(backward_node.actions)

					final_ans = present.actions[:] + backward_actions

					print ("Path found:: Forward: {} + Backward: {} = Total cost: {}"\
						.format(present.cost, backward_node.cost, total))

				# f_f.push(this_node, this_node.f)
				# g_f.push(this_node, this_node.cost)

			# if currentnode not in explorednode1:
			# 	explorednode1.add(currentnode)
			# 	visitedNodes.append(currentnode[0])
			# 	if problem.isGoalState(currentnode) or (currentnode in temp_q2):
			# 		while q2.isEmpty() == False:
			# 			node, direc,cost = q2.pop()
			# 			if node == currentnode:
			# 				direc.reverse()
			# 				solution = direction + ulta(direc)
			# 				problem.display(visitedNodes)
			# 				return solution
			# 	for(successor, action, stepCost) in problem.getSuccessors(currentnode):
			# 		q1.push((successor, direction + [action],cost+stepCost),max(cost+stepCost+heuristic(successor,problem),2*(cost+stepCost)))
			# 		# q1.push((successor, direction + [action],cost+stepCost),cost+stepCost+heuristic(successor,problem))
			# 		temp_q1.append(successor)
		else:

			currentnode = q2.pop()
			prev2 = currentnode
			pos = currentnode.pos
			if pos in dict_q2:
				dict_q2.pop(pos)
			explorednode2[pos] = currentnode


			# f_f.remove(curr_node)
			# g_f.remove(curr_node)

			children = problem.getSuccessorsBS(pos)
			for child in children:
				child_pos, child_direction, child_cost = child

				present = None

				if child_pos in dict_q2:
					present = dict_q2[child_pos]

				elif child_pos in explorednode2:
					present = explorednode2[child_pos]

				# if node already exists
				if present is None:

					present_actions = currentnode.actions[:] + [child_direction]
					present_cost = currentnode.cost + child_cost
					present_h = heuristic(child_pos, problem, back=True)
					present_pr = present_cost + max(present_h, present_cost)
					present = Node(child_pos, present_actions, present_cost, present_h, present_pr)


				else:
					# and is reached by a shorter path then ignore cuurent path
					if present.cost <= currentnode.cost + child_cost:
						continue

					# remove node from Open U Close Lists
					# open_f.remove(this_node)
					q2.remove(present)

					if child_pos in dict_q2:
						dict_q2.pop(child_pos)
					if child_pos in explorednode2:
						dict_q2.pop(child_pos)

					# f_f.remove(this_node)
					# g_f.remove(this_node)

					# else update the cost
					present.cost = (currentnode.cost + child_cost)
					present.f = present.cost + heuristic(present.pos, problem)
					present.actions = currentnode.actions[:] + [child_direction]

				# if present == None:	
					# continue

				q2.push(present, present.pr)
				dict_q2[child_pos] = present

				if child_pos in dict_q1:
					front_node = dict_q1[child_pos]
					total = present.cost + front_node.cost
					U = min(U, total)

					front_node.actions.reverse()
					front_actions = ulta(front_node.actions)

					final_ans = present.actions[:] + front_actions

					print ("Path found:: Backward: {} + Forward: {} = Total cost: {}"\
						.format(present.cost, front_node.cost, total))

			# currentnode, direction,cost = q2.pop()
			# if currentnode not in explorednode2:
			# 	explorednode2.add(currentnode)
			# 	visitedNodes.append(currentnode[0])
			# 	if currentnode in temp_q1:
			# 		while q1.isEmpty() == False:
			# 			node, direc,cost = q1.pop()
			# 			if node == currentnode:
			# 				direction.reverse()
			# 				solution = direc + ulta(direction)
			# 				problem.display(visitedNodes)
			# 				return solution
			# 	for(successor, action, stepCost) in problem.getSuccessors(currentnode):
			# 		q2.push((successor, direction + [action],cost+stepCost),max(cost+stepCost+heuristic(successor,problem,back=True),2*(cost+stepCost)))
			# 		# q2.push((successor, direction + [action],cost+stepCost),cost+stepCost+heuristic(successor,problem,back=True))
			# 		temp_q2.append(successor)
	print ("Both queues are empty")
	if prev1 is not None and prev2 is not None:
		prev2.actions.reverse()
		backward_actions = ulta(prev2.actions)

		return prev1.actions + backward_actions

					
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