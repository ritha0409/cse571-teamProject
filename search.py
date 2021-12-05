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
    Search the deepest states in the search tree first.

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
    visitedstates = []
    path = []
    vsn_disp = []
    
    startState = problem.getStartState()
    
    if problem.isGoalState(startState):
        problem.display(vsn_disp)
        return []
    
    pacmanFringe.push((startState,visitedstates,path))
    
    while not pacmanFringe.isEmpty():
        currentState, visitedstates, path = pacmanFringe.pop()
        visitedstates.append(currentState)
        vsn_disp.append(currentState[0])
        if problem.isGoalState(currentState):
            problem.display(vsn_disp)
            return path
        for nextState in problem.getSuccessors(currentState):
            if nextState[0] not in visitedstates:
                currentpath = path + [nextState[1]]
                pacmanFringe.push((nextState[0],visitedstates,currentpath))
            

def breadthFirstSearch(problem):
    """Search the shallowest states in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    from util import Queue
    
    queue = Queue()
    
    visitedstates = []
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
        visitedstates.append(positionState)
        vsn_disp.append(positionState[0])
        
        if problem.isGoalState(positionState):
            problem.display(vsn_disp)
            return path
            
        nextState = problem.getSuccessors(positionState)
        
        if nextState:
            for state in nextState:
                if state[0] not in visitedstates and state[0] not in (state[0] for state in queue.list):
                    newPath = path + [state[1]]
                    queue.push((state[0],newPath))
        

def uniformCostSearch(problem):
    """Search the state of least total cost first."""
    "*** YOUR CODE HERE ***"
    pacmanFringe=util.PriorityQueue()
    
    visitedstates=[]
    path=[]
    vsn_disp = []
    
    startState=problem.getStartState()
    startCost= len(path)
    
    if problem.isGoalState(startState):
        return []
    
    pacmanFringe.push((startCost,startState,visitedstates,path),startCost)
    
    while not pacmanFringe.isEmpty():
        currentCost, currentState, visitedstates, path = pacmanFringe.pop()
        if currentState not in visitedstates:
            visitedstates.append(currentState)
            vsn_disp.append(currentState[0])
            if problem.isGoalState(currentState):
                problem.display(vsn_disp)
                return path
            for nextState in problem.getSuccessors(currentState):
                if nextState[0] not in visitedstates:
                    currentpath = path + [nextState[1]]
                    nextCost= currentCost + nextState[2]
                    pacmanFringe.push((nextCost,nextState[0],visitedstates,currentpath),nextCost)

def nullHeuristic(state, problem=None,back=False):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the state that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pacmanFringe=util.PriorityQueue()
    
    visitedstates=[]
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
        
        if currentState not in visitedstates:
            visitedstates.append(currentState)
            vsn_disp.append(currentState[0])
            if problem.isGoalState(currentState):
                problem.display(vsn_disp)
                return path
            for nextState in problem.getSuccessors(currentState):
                if nextState[0] not in visitedstates:
                    currentpath = path + [nextState[1]]
                    nextCost= currentCost + nextState[2]
                    nextHeuristicCost=heuristic(nextState[0],problem)
                    nextTotalCost= nextCost + nextHeuristicCost
                    pacmanFringe.push((nextTotalCost,nextCost,nextState[0],currentpath),nextTotalCost)


def bidirection(problem, heuristic=nullHeuristic):

    foward_open_priority_queue = util.PriorityQueue()   
    openf = dict()
    temp_forward_state = (problem.getStartState(),[],0,heuristic(problem.getStartState(), problem),heuristic(problem.getStartState(), problem))
    foward_open_priority_queue.push(temp_forward_state, temp_forward_state[4])
    openf[problem.getStartState()] = temp_forward_state

    back_open_priority_queue = util.PriorityQueue()   
    openb = dict() 
    tenp_back_state = (problem.goal,[],0,heuristic(problem.goal, problem, back=True),heuristic(problem.goal, problem, back=True))
    back_open_priority_queue.push(tenp_back_state,tenp_back_state[4])
    openb[problem.goal] = tenp_back_state

    path = []
    closef = dict() 
    closeb = dict()    
    visitedstates = []

    U = 10000000  

    while not foward_open_priority_queue.isEmpty() and not back_open_priority_queue.isEmpty():

        tempf = foward_open_priority_queue.peek()
        tempb = back_open_priority_queue.peek()

        if U <= max( getMin(foward_open_priority_queue.heap) + getMin(back_open_priority_queue.heap) + 1, min(tempf[4],tempb[4]), getMin(foward_open_priority_queue.heap,False), getMin(back_open_priority_queue.heap,False)):
            problem.display(visitedstates,True)
            return path


        if tempf[4]<tempb[4]:
            current_state  = foward_open_priority_queue.pop()
            visitedstates.append(current_state[0])

            if not openf.get(current_state[0]) == None:
                del openf[current_state[0]]
            closef[current_state[0]] = current_state

            for successor_state, successor_action, successor_cost in problem.getSuccessors(current_state[0]):
                existing_state = openf.get(successor_state)
 
                if existing_state == None:
                    existing_state = closef.get(successor_state)


                if not(not existing_state == None and existing_state[2] <= current_state[2] + successor_cost):
                    if not existing_state == None:

                        existing_state = [existing_state[0],current_state[1][:] + [successor_action],current_state[2] + successor_cost,existing_state[2] + heuristic(existing_state[0], problem),existing_state[4]]
        
                        if foward_open_priority_queue.has(existing_state):
                            foward_open_priority_queue.remove(existing_state)
                        else:
                            foward_open_priority_queue.push(existing_state,existing_state[4])

                        if not openf.get(successor_state) == None or not closef.get(successor_state) == None:
                            if not openf.get(successor_state) == None:
                                del openf[successor_state]
                            if not closef.get(successor_state) == None:
                                del closef[successor_state]

                    else:
                        existing_state = [successor_state,current_state[1][:] + [successor_action],current_state[2] + successor_cost,heuristic(successor_state, problem),max((current_state[2] + successor_cost)*2,current_state[2] + successor_cost+heuristic(successor_state, problem))]

                    foward_open_priority_queue.push(existing_state, existing_state[4])
                    openf[successor_state] = existing_state


                    if not openb.get(successor_state) == None:
                        
                        path = existing_state[1] + ulta(openb[successor_state][1])

                        U = min(U, existing_state[2]+openb[successor_state][2])

        else:
            current_state = back_open_priority_queue.pop()
            visitedstates.append(current_state[0])


            if not openb.get(current_state[0]) == None:
                del openb[current_state[0]]
            closeb[current_state[0]] = current_state

            for successor_state, successor_action, successor_cost in problem.getSuccessors(current_state[0],back=True):
                existing_state = openb.get(successor_state)

                if  existing_state == None:
                    existing_state = closeb.get(successor_state)

                if not(not existing_state == None and existing_state[2] <= current_state[2] + successor_cost):

                    if existing_state is not None:

                        existing_state = [existing_state[0],current_state[1][:] + [successor_action],current_state[2] + successor_cost,existing_state[2] + heuristic(existing_state[0], problem, back=True),existing_state[4]]
                   

                        if back_open_priority_queue.has(existing_state):
                            back_open_priority_queue.remove(existing_state)
                        else:
                            back_open_priority_queue.push(existing_state,existing_state[4])

                        if not openb.get(successor_state) == None or not closeb.get(successor_state) == None:
                            if not openb.get(successor_state) == None:
                                del openb[successor_state]
                            if not closeb.get(successor_state) == None:
                                del closeb[successor_state]

                    else:
                        existing_state = [successor_state,current_state[1][:] + [successor_action],current_state[2] + successor_cost,heuristic(successor_state, problem, back=True),max((current_state[2] + successor_cost)*2,current_state[2] + successor_cost+heuristic(successor_state, problem, back=True))]

                    back_open_priority_queue.push(existing_state, existing_state[4])
                    openb[successor_state] = existing_state

                    if not openf.get(successor_state) ==None:
                                                
                        path = openf[successor_state][1] + ulta(existing_state[1])
                        U = min(U, existing_state[2]+openf[successor_state][2])


def ulta(direction):
    '''
    It reverses the path from the goal to the point where the two path meets.
    '''
    newD = direction
    newD.reverse()
    j = []
    for i in newD:
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

def getMin(ar,g=True):
    m=10000000
    for a in ar:
        if g:
            if a[2][2]<m:
                m = a[2][2]
        else:
            if a[2][3]<m:
                m = a[2][3]

    return m

bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
bi = bidirection
