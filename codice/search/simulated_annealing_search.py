# -*- coding: utf-8 -*-

from base_search import BaseSearch
from node import Node

import random, sys, math
from util import util


def exp_schedule(k=20, lam=0.05, limit=1000):
    "One possible schedule function for simulated annealing"
    return lambda t: k * math.exp(-lam * t) if t < limit else 0

class SimulatedAnnealingSearch(BaseSearch):
    """Classe che effettua la ricerca con Simulated Annealing"""

    def __init__(self, minimize = True, temperature_fn = exp_schedule()):
        self.__minimize = minimize
        self.__temperature_fn = temperature_fn

    def __calc_p(self, delta_e, T):
        try:
            return 1 / (1+math.exp(delta_e/T))
        except OverflowError:
            return 0

    def search(self, problem):
        return self.search_from_state(problem, problem.initial)

    def search_from_state(self, problem, state):
        current = Node(problem.initial)
        bs = 0

        for t in xrange(sys.maxint):
            
            T = self.__temperature_fn(t)
            if T == 0:
                return (current.state, current, t)
            
            neighbors = current.expand(problem)
            if not neighbors:
                return (current.state, current, t)
            
            # Sceglie un successore a caso
            next = random.choice(neighbors)
            
            # Differenza tra la funzione di valutazione calcolata per lo stato scelto e lo stato corrente
            delta_e = problem.value(next.state) - problem.value(current.state)

            # Booleano che specifica se lo stato sucessore selezionato è migliore o peggiore
            # di quello corrente
            good_state = delta_e > 0
            if self.__minimize: 
                good_state = delta_e < 0

            # Stato migliore
            if good_state:
                current = next
                #print 'GOOD CHOICE', t
            else:
                # Cambio di segno nel caso di minimizzazione o massimizzazione
                c = 1 if self.__minimize else -1
                p = self.__calc_p(c*delta_e,T)

                assert p <= 1, "Probabilità maggiore di 1"
                
                if random.uniform(0,1) <= p:
                    #bs += 1
                    #print 'BAD CHOICE', bs, p, t, problem.value(next.state), next
                    current = next

        assert False, "Non dovrebbe essere arrivato fin qui"           

    