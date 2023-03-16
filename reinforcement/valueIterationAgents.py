# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp: mdp.MarkovDecisionProcess, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates() - get every state/location on the board
              mdp.getPossibleActions(state) - get every possible move from a given state/location
              mdp.getTransitionStatesAndProbs(state, action) - get essentially the value of taking an action 'action' from state 'state'
              mdp.getReward(state, action, nextState) - get the reward
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        """
          Run the value iteration algorithm. Note that in standard
          value iteration, V_k+1(...) depends on V_k(...)'s.
        """
        "*** YOUR CODE HERE ***"
        """
        Load every state in the mdp into self.values with a value of 0
        """
        """
        Iterate for self.iteration amount of times:
        each iteration calculates the value for each state, starting from the terminal state (kind of)
        """
        for i in range(self.iterations):
            # calculate value of self.values
            # create temp counter to not overwrite self.values
            values_copy = util.Counter()
            for state in self.mdp.getStates():
                # if self.mdp.isTerminal(state):
                #     print("found terminal")
                #     self.values[state] = self.mdp.getReward(state, 'exit', state)
                #     continue
                best_value = -float('inf')

                for action in self.mdp.getPossibleActions(state):
                    value = self.computeQValueFromValues(state, action)

                    if value > best_value:
                        best_value = value

                # if a best value was found, update the relevant state
                if best_value != -float('inf'):
                    print(state)
                    values_copy[state] = best_value
                else:
                    values_copy[state] = 0

                # self.values[state] = self.computeQValueFromValues(state, self.computeActionFromValues(state))
                # print(self.getValue(state))

                self.values = values_copy


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        """
        Do the T(s,a,s')[R(s,a,s') + yVk] thing for one given action
        """
        reward = 0
        if self.mdp.isTerminal(state):
            # skip it
            print('found terminal')
            return self.mdp.getReward(state, 'exit', state)

        for next_state, probability in self.mdp.getTransitionStatesAndProbs(state, action):
            # given the possible state and probability, add to reward:
            # poss_state[1](self.mdp.getReward(poss_state[0] + discount(reward of staying there)
            #print(probability, self.mdp.getReward(state, action, next_state), self.discount, self.getValue(next_state))
            print(state, next_state)
            # if self.mdp.isTerminal(next_state):
            #     reward += self.mdp.getReward(state, action, next_state)
            # else:
            state_reward = self.mdp.getReward(state, action, next_state)
            #print('made it')
            next_state_reward = self.values[next_state]
            parentheses = state_reward + (self.discount * next_state_reward)
            reward += probability * parentheses
        return reward

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        """
        For every possible action, get the QValue and then return the best
        """
        best_action = None
        best_value = -float('inf')

        #print(self.mdp.getPossibleActions(state))

        for action in self.mdp.getPossibleActions(state):
            if self.computeQValueFromValues(state, action) > best_value:
                best_action = action
                best_value = self.computeQValueFromValues(state, action)

        return best_action


    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
