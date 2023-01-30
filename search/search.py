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

def depthFirstSearch(problem: SearchProblem):
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
    reached = []
    fringe = util.Stack()
    fringe.push((problem.getStartState(), [], 0))

    while not fringe.isEmpty():
        state, action, cost = fringe.pop()

        if problem.isGoalState(state):
            return action

        if state not in reached:
            reached.append(state)

            for successor in problem.getSuccessors(state):
                fringe.push((successor[0], action + [successor[1]], cost + successor[2]))

    # TAKE 2: DOES NOT WORK
    # states = []
    # savedTuple = list(((None, None), [], 0))
    # fringe = util.Stack()
    # fringe.push((problem.getStartState(), None, 0))
    #
    # while not fringe.isEmpty():
    # #for i in range(5):
    #     state, action, cost = fringe.pop()
    #     #print("state = ", state, " action = ", action, " cost = ", cost)
    #     #print("Current state is ", savedTuple[0], "\nPopped state is ", state)
    #     if problem.isGoalState(state):
    #         # return the path to said goal
    #         savedTuple[0] = state
    #         savedTuple[1].append(action)
    #
    #         print("path = ", savedTuple[1])
    #         return savedTuple[1]
    #
    #     if state not in states:
    #         states.append(state)
    #
    #         print("savedTuple[0] = ", savedTuple[0], " | state = ", state)
    #
    #         savedTuple[0] = state
    #
    #         print("POST ASSIGNMENT:\nsavedTuple[0] = ", savedTuple[0], " | state = ", state)
    #
    #         if action is not None:
    #             savedTuple[1].append(action)
    #
    #         print("savedTuple = ", savedTuple, "  action = ", action, "\n")
    #
    #         for successor in problem.getSuccessors(state):
    #             print(successor)
    #             fringe.push(successor)
    #
    # return None

    # TAKE 1: WORKS BUT NOT FOR AUTOGRADER
    #
    # path = util.Stack()
    # pathDir = util.Stack()
    # reached = [problem.getStartState()] # needs to store states as tuples with different directions cause loops
    #
    # # current node, popped from the top of path
    # path.push(problem.getStartState())
    # pathDir.push('Start')
    #
    # # check if top of path has unreached successors
    # # if so, replace top of path, add first unreached successor to path and to reached, repeat
    # while True:
    #     curr = path.pop()
    #     dir = pathDir.pop()
    #     #print("curr = ", curr)
    #
    #     if problem.isGoalState(curr):
    #         path.push(curr)
    #         pathDir.push(dir)
    #         break
    #
    #     for successor in problem.getSuccessors(curr):
    #         #print(successor[0])
    #         if successor[0] not in reached:
    #             path.push(curr)
    #             pathDir.push(dir)
    #             path.push(successor[0])
    #             pathDir.push(successor[1])
    #             reached.append(successor[0])
    #             #print("reached = ", reached, "\n")
    #             break
    #         #print(successor[0], " has been reached already")
    #
    # result = []
    #
    # # Code here to create list of actions from queue backwards
    # temp = pathDir.pop()
    # while temp is not 'Start':
    #     result.append(temp)
    #     temp = pathDir.pop()
    #
    # print(result[::-1])
    # return result[::-1]

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    reached = []
    fringe = util.Queue()
    fringe.push((problem.getStartState(), [], 0))

    while not fringe.isEmpty():
        state, action, cost = fringe.pop()

        if problem.isGoalState(state):
            return action

        if state not in reached:
            reached.append(state)

            for successor in problem.getSuccessors(state):
                fringe.push((successor[0], action + [successor[1]], cost + successor[2]))

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    reached = []
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0), 0)

    while not fringe.isEmpty():
        state, action, cost = fringe.pop()

        if problem.isGoalState(state):
            return action

        if state not in reached:
            reached.append(state)

            for successor in problem.getSuccessors(state):
                fringe.push((successor[0], action + [successor[1]], cost + successor[2]), cost + successor[2])

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    reached = []
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))

    while not fringe.isEmpty():
        state, action, cost = fringe.pop()

        if problem.isGoalState(state):
            return action

        if state not in reached:
            reached.append(state)

            for successor in problem.getSuccessors(state):
                fringe.push((successor[0], action + [successor[1]], cost + successor[2]), cost + successor[2] + heuristic(successor[0], problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
