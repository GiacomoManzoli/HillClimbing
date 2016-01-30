# -*- coding: utf-8 -*-

from base_search import BaseSearch
from node import Node

from util import util

class HillClimbingStocasticSearch(BaseSearch):
    """Classe che effettua la ricerca hill climbing stocastica, ovvero sceglie l'azione da eseguire in modo causale tra tutte quelle che migliorano il valore della funzione di valutazione.
    La probabilità di scelta di una determinata azione viene influenzata da quanto l'azione migliora la funzione obiettivo.
    """

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

            current_value = problem.value(current.state)

            # lista dei vicini che migliorano la funzione obiettivo
            choices = []
            for s in neighbors:
                v = problem.value(s.state)
                if v < current_value and self.__minimize:
                    choices.append((s,current_value - v))
                else:
                    if v > current_value and not self.__minimize:
                        choices.append((s,v - current_value))

            # Non ci sono stati che migliorano la funzione obiettivo
            if len(choices) == 0:
                break;

            # Sceglie lo stato
            neighbor = util.weighted_choice(choices)        
            #print cnt, current, problem.value(current.state), neighbor, problem.value(neighbor.state)
            
            cnt += 1
            current = neighbor

        return (current.state, current, cnt)


    





    