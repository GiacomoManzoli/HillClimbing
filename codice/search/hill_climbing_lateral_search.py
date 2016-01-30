# -*- coding: utf-8 -*-

from base_search import BaseSearch
from node import Node

from util import util



class HillClimbingLateralSearch(BaseSearch):
    """Classe che effettua la ricerca Hill Climbing con la possibilità di effettuare
    mosse laterali nel caso non ci siano mosse migliore"""
    def __init__(self, minimize = True, lateral_move = 100):
        self.__minimize = minimize
        self.__lateral_move = lateral_move

    def search(self, problem):
        return self.search_from_state(problem, problem.initial)

    def search_from_state(self, problem, state):
        cnt = 0
        lateral_move = self.__lateral_move
        current = Node(state)

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

                current_value = problem.value(current.state)
                neighbor_value = problem.value(neighbor.state)
                
                if neighbor_value == current_value:
                    # Mossa laterale
                    #print 'Mossa laterale'
                    lateral_move -= 1

                if neighbor_value < current_value:
                    # Mossa buona, resetto le mosse laterali
                    lateral_move = self.__lateral_move
                else:
                    if neighbor_value > current_value:
                        break
                    # Mossa che non migliora, se non posso fare delle mosse laterali termino
                    if lateral_move <= 0:
                        #print 'EXIT'
                        break
            else:
                neighbor = util.argmax_random_tie(neighbors,
                                             lambda node: problem.value(node.state))
                
                current_value = problem.value(current.state)
                neighbor_value = problem.value(neighbor.state)


                if neighbor_value == current_value:
                    # Mossa laterale
                    lateral_move -= 1

                if neighbor_value > current_value:
                    # Mossa buona, resetto le mosse laterali
                    lateral_move = self.__lateral_move
                else:
                    if neighbor_value > current_value:
                        break
                    # Mossa che non migliora, se non posso fare delle mosse laterali termino
                    if lateral_move <= 0:
                        break
            #print cnt, current, problem.value(current.state), neighbor, problem.value(neighbor.state)
            cnt += 1
            current = neighbor
            
        return (current.state, current, cnt)

    