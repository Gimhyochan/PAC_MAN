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
import copy
from game import Directions
from game import Actions

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
    # init
    stack = util.Stack()
    direction = []
    state = problem.getStartState()
    stack.push([state, []])
    visitedNode = []
    visitedNode.append(state)
    #print("INITIAL STATE: ", str(state))
    #print("INITIAL visitedNode" + str(visitedNode))
    # DFS
    while not stack.isEmpty():
        #print(stack.list)
        #print(direction)
        #print(state)
        if problem.isGoalState(state):
            #print("Goal")
            #print(state)
            #print(stack_direction.list)
            #print(stack_state.list)
            return direction
        #print("State: " + str(state))
        successors = problem.getSuccessors(state)
        for successor in successors:
            if successor[0] not in visitedNode:
                #print("Successor[1]")
                #print(successor[1])
                direction.append(successor[1])
                #print(direction)
                stack.push([successor[0],copy.deepcopy(direction)])
                #print(stack.list)
                direction.pop()
                #print(direction)
        #print("Stack List:\n"+str(stack.list))
        state, direction = stack.pop()
        #print("Stack List:\n"+str(stack.list))
        #print(state)
        #print(direction)
        visitedNode.append(state)

    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # init
    queue = util.Queue()
    direction = []
    state = problem.getStartState()
    visitedNode = []
    visitedNode.append(state)
    while(True):
        if problem.isGoalState(state):
            return direction
        # print("State: " + str(state))
        successors = problem.getSuccessors(state)
        for successor in successors:
            if successor[0] not in visitedNode:
                # print("Successor[1]")
                # print(successor[1])
                condition = False
                for que in queue.list:
                    if que[0] == successor[0]:
                        condition = True
                        break
                if condition:
                    continue
                direction.append(successor[1])
                queue.push([successor[0], copy.deepcopy(direction)])
                direction.pop()
                # print(direction)
        # print("Stack List:\n"+str(stack.list))
        if queue.isEmpty():
            break
        state, direction = queue.pop()
        # print("Stack List:\n"+str(stack.list))
        # print(state)
        # print(direction)
        visitedNode.append(state)
    return direction
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    "Dijkstra Alogorithm"
    Priorityqueue = util.PriorityQueue()
    "direction info in the Prioirty Queue"
    #direction = []
    state = problem.getStartState()
    Priorityqueue.push((state, [], 0), 0)
    visitedNode = {}
    # print("INITIAL STATE: ", str(state))
    # print("INITIAL visitedNode" + str(visitedNode))
    #uniformCostSearch
    while True:
        # print(Priorityqueue.list)
        # print(direction)
        # print(state)
        #a = Priorityqueue.pop()
        #print(a)
        state, direction, cost = Priorityqueue.pop()
        #print(state)
        #print(direction)
        #print(visitedNode)
        visitedNode[state] = cost
        if problem.isGoalState(state):
            return direction
        for successor, successor_direction, successor_cost in problem.getSuccessors(state):
            if(successor not in visitedNode):
                #print(cost + successor_cost)
                visitedNode[successor] = cost + successor_cost
                Priorityqueue.push((successor, direction + [successor_direction],
                                    cost + successor_cost), cost + successor_cost)
            elif successor in visitedNode:
                # print(cost + successor_cost)
                if visitedNode[successor] > cost + successor_cost:
                    visitedNode[successor] = cost + successor_cost
                    Priorityqueue.push((successor, direction + [successor_direction],
                                        cost + successor_cost), cost + successor_cost)
        if Priorityqueue.isEmpty():
            break
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    state = problem.getStartState()
    visitedNode = []
    Priorityqueue = util.PriorityQueue()
    Priorityqueue.push((state, []), nullHeuristic(state, problem))
    cost = 0
    while True:
        state, direction = Priorityqueue.pop()
        if problem.isGoalState(state):
            return direction
        if state not in visitedNode:
            for coordinates, directions, cost in problem.getSuccessors(state):
                #print("coordinates: " + str(coordinates) + " directions: " + str(directions) + " cost: " + str(cost))
                coordinates = coordinates
                if coordinates not in visitedNode:
                    nActions = direction + [directions]
                    nCost = problem.getCostOfActions(nActions) + heuristic(coordinates, problem)
                    Priorityqueue.push((coordinates, direction + [directions]), nCost)
        visitedNode.append(state)
        if Priorityqueue.isEmpty():
            break
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
