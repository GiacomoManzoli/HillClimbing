# -*- coding: utf-8 -*-

from base_search import BaseSearch
from node import Node

from util import util



class HillClimbingSearch(BaseSearch):
    """Classe che effettua la ricerca HillClimbing pura"""

    def __init__(self, minimize = True):
        self.__minimize = minimize

    def search(self, problem):
        return self.search_from_state(problem, problem.initial)

    def search_from_state(self, problem, state):
        cnt = 0
        
        current = Node(state)
        #print "Cnt \t Current \t Best"
        while True:
            if problem.goal_test(current.state):
                break
            neighbors = current.expand(problem)
            if not neighbors:
                break

            if self.__minimize:
                neighbor = util.argmin_random_tie(neighbors,
                                             lambda node: problem.value(node.state))
                # il miglior vicino ha come funzione di valutazione un valore
                # peggiore (maggiore) o uguale a quello dello stato corrente
                if problem.value(neighbor.state) >= problem.value(current.state):
                    break
            else:
                neighbor = util.argmax_random_tie(neighbors,
                                             lambda node: problem.value(node.state))
                if problem.value(neighbor.state) <= problem.value(current.state):
                    break
            
            #print cnt, current, problem.value(current.state), neighbor, problem.value(neighbor.state)
            
            cnt += 1
            current = neighbor

        return (current.state, current, cnt)

    