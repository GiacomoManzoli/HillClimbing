# -*- coding: utf-8 -*-

from base_search import BaseSearch
from node import Node
from hill_climbing_search import HillClimbingSearch


import util



class HillClimbingRandomRestartSearch(BaseSearch):
    """Classe che effettua la ricerca hill climbinig effettuando un riavvio casuale finché non viene trovata una soluzione ottima, la tipologia di hill climbing da utilizzare ad ogni iterazione viene decisa dall'oggetto search passato al costruttore, di default viene utilizzato HillClimbingSearch"""

    def __init__(self, minimize = True, search = None):
        self.__minimize = minimize
        if search:
            self.__hc = search
        else:
            self.__hc = HillClimbingSearch(minimize)

    def search(self, problem):
        return self.search_from_state(problem, problem.initial)

    def search_from_state(self, problem, state):
        # Fa la prima ricerca
        (state, node, x) = self.__hc.search(problem)
        cnt = 1

        while not problem.goal_test(state):
            cnt += 1            
            (state, node, x) = self.__hc.search_from_state(problem, problem.random_state())
        
        return (state, node, cnt)
    