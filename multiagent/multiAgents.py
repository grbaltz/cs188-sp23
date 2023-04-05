# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
<<<<<<< HEAD
        """python pacman.py -p ReflexAgent -l testClassic
=======
        """
>>>>>>> fffbbf998f3ab4f618a672b92e58d9ef97ea5b42
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"
<<<<<<< HEAD
=======
        #print(scores, legalMoves)
>>>>>>> fffbbf998f3ab4f618a672b92e58d9ef97ea5b42


        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
<<<<<<< HEAD
        print("newPos -----------------------------------------------------------\n", newPos)
        print("newFood -----------------------------------------------------------\n", newFood)
        print("newGhostStates -----------------------------------------------------------\n", newGhostStates)
        print("newScaredTimes -----------------------------------------------------------\n", newScaredTimes)

        scareds = 0
        for scared in newScaredTimes:
            scareds += scared
        if scareds == 0:
            #proceed being scared of ghost
            for ghost in newGhostStates:
                if newFood[newPos[0]][newPos[1]] == "T" and ghost.getGhostPositiion() != newPos:
                    print("returned 99999")
                    return 99999
                #dist = 9999
                #for food in newFood.asList():
                #    if food == "F":
                #        dist = newPos[0]

        else:
            if newFood[newPos[0]][newPos[1]] == "T":
                print("returned 99999")
                return 99999

        return successorGameState.getScore()
        return successorGameState.getScore()
=======
        #print(newPos)

        for i in range(len(newGhostStates)):
            if manhattanDistance(newGhostStates[i].getPosition(), newPos) <= 1:
                return -float('inf')

        if newFood.asList() == []:
            return float('inf')

        maxDist = -float('inf')
        for food in newFood.asList():
            #print("food =", food, "| mD =", manhattanDistance(food, newPos), "| getScore =", successorGameState.getScore(), " maxDist =", maxDist, "| 999999 - mD =", (999999 - manhattanDistance(food, newPos)))
            if (999999 - manhattanDistance(food, newPos)) > maxDist:
                maxDist = (999999 - manhattanDistance(food, newPos))

        # if moving here reduces the amount of food
        if (len(newFood.asList()) < len(currentGameState.getFood().asList())):
            return float('inf')

        return successorGameState.getScore() + maxDist
>>>>>>> fffbbf998f3ab4f618a672b92e58d9ef97ea5b42

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
<<<<<<< HEAD
        util.raiseNotDefined()
=======

        """
        Make move that gets to agent-relative score
        To do that: Consider each successor and choose the one with a higher value/lower value
        
        For each agent, get its successors (recursively do this up to depth 
            times i.e.: call getSuccessors on each agent depth times)
        """

        # For each legal pacman action, compute its score
            # Call helper on each agent, sum the values together
            # Return highest scoring call ^^^

        return self.helper(gameState, self.depth, 0)[1]


    def helper(self, gameState: GameState, current_depth: int, agentIndex: int):
        if current_depth == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), None

        # loop over possible actions

        if agentIndex == 0:  # pacman woo
            return self.maximize(gameState, current_depth, agentIndex)
        else:
            return self.minimize(gameState, current_depth, agentIndex)

    def minimize(self, state: GameState, current_depth: int, agentIndex: int):
        v = float('inf')
        best_action = None
        if agentIndex == state.getNumAgents() - 1:
            current_depth -= 1

        for action in state.getLegalActions(agentIndex):
            temp_v = v
            v = min(v, self.helper(state.generateSuccessor(agentIndex, action), current_depth, (agentIndex + 1) % state.getNumAgents())[0])
            if v != temp_v:
                best_action = action
        return v, best_action

    def maximize(self, state: GameState, current_depth: int, agentIndex: int):
        v = -float('inf')
        best_action = None
        for action in state.getLegalActions(agentIndex):
            temp_v = v
            v = max(v, self.helper(state.generateSuccessor(agentIndex, action), current_depth, (agentIndex + 1) % state.getNumAgents())[0])
            if v != temp_v:
                best_action = action
        return v, best_action

>>>>>>> fffbbf998f3ab4f618a672b92e58d9ef97ea5b42

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
<<<<<<< HEAD
        util.raiseNotDefined()
=======
        return self.helper(gameState, self.depth, 0, -float('inf'), float('inf'))[1]


    def helper(self, gameState: GameState, current_depth: int, agentIndex: int, a: int, b: int):
        if current_depth == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), None

        # loop over possible actions

        if agentIndex == 0:  # pacman woo
            return self.maximize(gameState, current_depth, agentIndex, a, b)
        else:
            return self.minimize(gameState, current_depth, agentIndex, a, b)

    def minimize(self, state: GameState, current_depth: int, agentIndex: int, a: int, b: int):
        v = float('inf')
        best_action = None
        if agentIndex == state.getNumAgents() - 1:
            current_depth -= 1

        for action in state.getLegalActions(agentIndex):
            temp_v = v
            v = min(v, self.helper(state.generateSuccessor(agentIndex, action), current_depth, (agentIndex + 1) % state.getNumAgents(), a, b)[0])

            if v != temp_v:
                best_action = action
            if v < a:
                return v, best_action

            b = min(b, v)
        return v, best_action

    def maximize(self, state: GameState, current_depth: int, agentIndex: int, a: int, b: int):
        v = -float('inf')
        best_action = None
        for action in state.getLegalActions(agentIndex):
            temp_v = v
            v = max(v, self.helper(state.generateSuccessor(agentIndex, action), current_depth, (agentIndex + 1) % state.getNumAgents(), a, b)[0])

            if v != temp_v:
                best_action = action
            if v > b:
                return v, best_action

            a = max(a, v)
        return v, best_action
>>>>>>> fffbbf998f3ab4f618a672b92e58d9ef97ea5b42

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
<<<<<<< HEAD
        util.raiseNotDefined()
=======
        return self.helper(gameState, self.depth, 0)[1]


    def helper(self, gameState: GameState, current_depth: int, agentIndex: int):
        if current_depth == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), None

        # loop over possible actions

        if agentIndex == 0:  # pacman woo
            return self.maximize(gameState, current_depth, agentIndex)
        else:
            return self.randomize(gameState, current_depth, agentIndex)

    def randomize(self, state: GameState, current_depth: int, agentIndex: int):
        v = 0
        best_action = None
        if agentIndex == state.getNumAgents() - 1:
            current_depth -= 1

        for action in state.getLegalActions(agentIndex):
            p = 1/len(state.getLegalActions(agentIndex))
            temp_v = v
            v += p * self.helper(state.generateSuccessor(agentIndex, action), current_depth, (agentIndex + 1) % state.getNumAgents())[0]
            if v != temp_v:
                best_action = action
        return v, best_action

    def maximize(self, state: GameState, current_depth: int, agentIndex: int):
        v = -float('inf')
        best_action = None
        for action in state.getLegalActions(agentIndex):
            temp_v = v
            v = max(v, self.helper(state.generateSuccessor(agentIndex, action), current_depth, (agentIndex + 1) % state.getNumAgents())[0])
            if v != temp_v:
                best_action = action
        return v, best_action
>>>>>>> fffbbf998f3ab4f618a672b92e58d9ef97ea5b42

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
<<<<<<< HEAD
    util.raiseNotDefined()
=======
    # do something to determine which moves are better than others
    # things to try:
    # if food amount goes down, closest manhattan distance to food
    pos = currentGameState.getPacmanPosition()
    food_left = len(currentGameState.getFood().asList())
    scared_times = [ghostState.scaredTimer for ghostState in currentGameState.getGhostStates()]
    closest_food = float('inf')
    closest_pellet = float('inf')
    scared = 0
    can_reach_ghost = 0
    food_distances = 0
    ghost_distances = 0
    score = currentGameState.getScore()

    for food in currentGameState.getFood():
        closest_food = min(closest_food, manhattanDistance(pos, food))
        if manhattanDistance(pos, food) >= 0:
            # score += manhattanDistance(pos, food)
            score += 50

    # for pellet in currentGameState.getCapsules():
    #     closest_pellet = min(closest_pellet, manhattanDistance(pos, pellet))

    for ghost in currentGameState.getGhostStates():
        if manhattanDistance(pos, ghost.getPosition()) > 0:
            # score += manhattanDistance(pos, ghost.getPosition())
            score += 50/manhattanDistance(pos, ghost.getPosition())

        # if ghost.scaredTimer >= manhattanDistance(pos, ghost.getPosition()):
        #     scared += 10
        # #print("scared =", ghost.scaredTimer)
        #
        # if ghost.scaredTimer == 0 and manhattanDistance(pos, ghost.getPosition()) > 5:
        #     scared += 5



    #print("values =", food_left, closest_food, scared)
    #print("score =", 100 - food_left - closest_food + scared)
    return score
>>>>>>> fffbbf998f3ab4f618a672b92e58d9ef97ea5b42

# Abbreviation
better = betterEvaluationFunction
