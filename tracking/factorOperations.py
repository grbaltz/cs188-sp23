# factorOperations.py
# -------------------
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

from typing import List
from bayesNet import Factor
import functools
from util import raiseNotDefined

def joinFactorsByVariableWithCallTracking(callTrackingList=None):


    def joinFactorsByVariable(factors: List[Factor], joinVariable: str):
        """
        Input factors is a list of factors.
        Input joinVariable is the variable to join on.

        This function performs a check that the variable that is being joined on 
        appears as an unconditioned variable in only one of the input factors.

        Then, it calls your joinFactors on all of the factors in factors that 
        contain that variable.

        Returns a tuple of 
        (factors not joined, resulting factor from joinFactors)
        """

        if not (callTrackingList is None):
            callTrackingList.append(('join', joinVariable))

        currentFactorsToJoin =    [factor for factor in factors if joinVariable in factor.variablesSet()]
        currentFactorsNotToJoin = [factor for factor in factors if joinVariable not in factor.variablesSet()]

        # typecheck portion
        numVariableOnLeft = len([factor for factor in currentFactorsToJoin if joinVariable in factor.unconditionedVariables()])
        if numVariableOnLeft > 1:
            print("Factor failed joinFactorsByVariable typecheck: ", factor)
            raise ValueError("The joinBy variable can only appear in one factor as an \nunconditioned variable. \n" +
                             "joinVariable: " + str(joinVariable) + "\n" +
                             ", ".join(map(str, [factor.unconditionedVariables() for factor in currentFactorsToJoin])))

        joinedFactor = joinFactors(currentFactorsToJoin)
        return currentFactorsNotToJoin, joinedFactor

    return joinFactorsByVariable

joinFactorsByVariable = joinFactorsByVariableWithCallTracking()

########### ########### ###########
########### QUESTION 2  ###########
########### ########### ###########

def joinFactors(factors: List[Factor]):
    """
    Input factors is a list of factors.

    You should calculate the set of unconditioned variables and conditioned
    variables for the join of those factors.

    Return a new factor that has those variables and whose probability entries
    are product of the corresponding rows of the input factors.

    You may assume that the variableDomainsDict for all the input
    factors are the same, since they come from the same BayesNet.

    joinFactors will only allow unconditionedVariables to appear in
    one input factor (so their join is well defined).

    Hint: Factor methods that take an assignmentDict as input
    (such as getProbability and setProbability) can handle
    assignmentDicts that assign more variables than are in that factor.

    Useful functions:
    Factor.getAllPossibleAssignmentDicts
    Factor.getProbability
    Factor.setProbability
    Factor.unconditionedVariables
    Factor.conditionedVariables
    Factor.variableDomainsDict
    """

    # typecheck portion
    setsOfUnconditioned = [set(factor.unconditionedVariables()) for factor in factors]
    if len(factors) > 1:
        intersect = functools.reduce(lambda x, y: x & y, setsOfUnconditioned)
        if len(intersect) > 0:
            print("Factor failed joinFactors typecheck: ", factor)
            raise ValueError("unconditionedVariables can only appear in one factor. \n"
                             + "unconditionedVariables: " + str(intersect) +
                             "\nappear in more than one input factor.\n" +
                             "Input factors: \n" +
                             "\n".join(map(str, factors)))


    "*** YOUR CODE HERE ***"
    # Need to go through the given factors, getting all of the conditioned variables shared between all the factors
    # and putting them into 1 conditioned list, the rest going in the unconditioned

    # print("FACTORS:", factors)
    combinedVarDomains = {}
    sharedUnconditioned = []
    sharedConditioned = []
    allVars = []

    for first in factors:
        for var in first.variableDomainsDict():
            combinedVarDomains[var] = first.variableDomainsDict()[var]

        for var in first.variables():
            if not allVars.__contains__(var):
                allVars.append(var)
        for var in first.unconditionedVariables():
            if not sharedUnconditioned.__contains__(var):
                sharedUnconditioned.append(var)
        for var in first.conditionedVariables():
            if not sharedConditioned.__contains__(var):
                sharedConditioned.append(var)
        for unconc in sharedUnconditioned:
            if sharedConditioned.__contains__(unconc):
                sharedConditioned.remove(unconc)

    result = Factor(sharedUnconditioned, sharedConditioned, combinedVarDomains)

    #print("ASSDICS:", result.getAllPossibleAssignmentDicts())

    for assDic in result.getAllPossibleAssignmentDicts():
        prob = 1
        for factor in factors:
            prob = prob * factor.getProbability(assDic)
            # print("prob", prob, "factor", "assDic", assDic, "probability", factor.getProbability(assDic))
        result.setProbability(assDic, prob)

    #print(result)
    return result
    "*** END YOUR CODE HERE ***"

########### ########### ###########
########### QUESTION 3  ###########
########### ########### ###########

def eliminateWithCallTracking(callTrackingList=None):

    def eliminate(factor: Factor, eliminationVariable: str):
        """
        Input factor is a single factor.
        Input eliminationVariable is the variable to eliminate from factor.
        eliminationVariable must be an unconditioned variable in factor.

        You should calculate the set of unconditioned variables and conditioned
        variables for the factor obtained by eliminating the variable
        eliminationVariable.

        Return a new factor where all of the rows mentioning
        eliminationVariable are summed with rows that match
        assignments on the other variables.

        Useful functions:
        Factor.getAllPossibleAssignmentDicts
        Factor.getProbability
        Factor.setProbability
        Factor.unconditionedVariables
        Factor.conditionedVariables
        Factor.variableDomainsDict
        """
        # autograder tracking -- don't remove
        if not (callTrackingList is None):
            callTrackingList.append(('eliminate', eliminationVariable))

        # typecheck portion
        if eliminationVariable not in factor.unconditionedVariables():
            print("Factor failed eliminate typecheck: ", factor)
            raise ValueError("Elimination variable is not an unconditioned variable " \
                             + "in this factor\n" +
                             "eliminationVariable: " + str(eliminationVariable) + \
                             "\nunconditionedVariables:" + str(factor.unconditionedVariables()))

        if len(factor.unconditionedVariables()) == 1:
            print("Factor failed eliminate typecheck: ", factor)
            raise ValueError("Factor has only one unconditioned variable, so you " \
                             + "can't eliminate \nthat variable.\n" + \
                             "eliminationVariable:" + str(eliminationVariable) + "\n" + \
                             "unconditionedVariables: " + str(factor.unconditionedVariables()))

        "*** YOUR CODE HERE ***"
        # # probs = []
        #
        # print(factor.getAllPossibleAssignmentDicts())
        #
        # # for assDic in factor.getAllPossibleAssignmentDicts():
        #
        # #     probs.append(factor.getProbability(assDic))
        #
        # # print(probs)
        #
        # newUnconditioned = []
        # newConditioned = []
        # probs = []
        # for assDic in factor.getAllPossibleAssignmentDicts():
        #     print("assDic: ", assDic)
        #     if assDic.__contains__(eliminationVariable):
        #         probs.append((assDic, factor.getProbability(assDic)))
        #
        # for unc in factor.unconditionedVariables():
        #     if not unc.__contains__(eliminationVariable):
        #         newUnconditioned.append(unc)
        # for cond in factor.conditionedVariables():
        #     if not cond.__contains__(eliminationVariable):
        #         newConditioned.append(cond)
        # print(probs)
        # #print("Old unc: ", factor.unconditionedVariables())
        # #print("New Unc: ", newUnconditioned)
        #
        # #print("Old con: ", factor.conditionedVariables())
        # #print("New con: ", newConditioned)
        # # print("New con: ", newConditioned)
        # result = Factor(newUnconditioned, newConditioned, factor.variableDomainsDict())
        # c = 0
        # #print(result.getAllPossibleAssignmentDicts())
        # for assDic in result.getAllPossibleAssignmentDicts():
        #     print("result assDic: ", assDic)
        #     #   TODO fix, hardcoded to pass test 1 atm
        #     finProb = 0
        #     for prob in probs:
        #         print("dict.keys: ", dict.keys(prob[0]))
        #         print("assDic keys: ", assDic.keys())
        #
        #         if list(assDic.keys()) in list(dict.keys(prob[0])):
        #             print("contained")
        #             finProb += prob[1]
        #     result.setProbability(assDic, finProb)
        #     finProb = 0
        #     c += 1
        # #add all not removed probs together
        # print(result)
        # return result

        # print(factor, "elimination variable =", eliminationVariable)
        combinedVarDomains = {}
        oldUnconditioned = factor.unconditionedVariables()
        newUnconditioned = []
        newConditioned = factor.conditionedVariables()
        allVars = []

        #print(newUnconditioned)
        for uncon in oldUnconditioned:
            #print(uncon)
            if uncon != eliminationVariable:
                newUnconditioned.append(uncon)

        for var in factor.variableDomainsDict():
            if newUnconditioned.__contains__(var) or newConditioned.__contains__(var):
                combinedVarDomains[var] = factor.variableDomainsDict()[var]

        # print("unconditioned", newUnconditioned, "conditioned", newConditioned, "combinedVarDomains", combinedVarDomains)

        result = Factor(newUnconditioned, newConditioned, combinedVarDomains)

        # print("result in code", result)
        # print("result.assDics", result.getAllPossibleAssignmentDicts())

        for assDic in result.getAllPossibleAssignmentDicts():
            # print("assDic", assDic, "| probability")

            prob = 0

            for oldAssDic in factor.getAllPossibleAssignmentDicts():
                mismatch = False
                for key in assDic:
                    if oldAssDic[key] != assDic[key]:
                        mismatch = True
                        continue

                if mismatch:
                    continue

                prob += factor.getProbability(oldAssDic)
            result.setProbability(assDic, prob)

        #print(result)
        return result
        "*** END YOUR CODE HERE ***"

    return eliminate

eliminate = eliminateWithCallTracking()