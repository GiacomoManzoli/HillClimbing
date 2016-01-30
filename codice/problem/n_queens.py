# -*- coding: utf-8 -*-
from problem import Problem
import random

class NQueens(Problem):

    """ 
    Gli stati del problema sono modellati come liste di interi di lunghezza pari alla dimensione della scacchiera.
    L'elemento i-esimo della lista corrisponde alla riga in cui si trova la regina della colonna i.

    Ad esempio la lista [0,1,2] corrisponde allo stato

    -------
    |R| | |
    -------
    | |R| |
    -------
    | | |R|
    -------

    Questa modellazione aiuta a minimizzare i conflitti, dal momento che non si possono avere due regine nella stessa colonna
    """

    # Dimensione della scacchiera
    __board_size = 0

    def __init__(self, board_size=8, initial=None):
        if initial:
            Problem.__init__(self, initial)
        else:
            Problem.__init__(self, [0 for i in range(board_size)])
        self.__board_size = board_size
        


    def actions(self, state):
        """Ritorna tutte le possibili azioni nello stato, nella forma (c,r) e specifica la riga r in cui si sposta la regina della colonna c
        """
        actions = []
        for c, rc in enumerate(state):
            # per ogni colonna vengono aggiunte tante azioni quante sono le righe
            # escludendo l'azione che non muove la regina (ovvero quando i == rc)
            actions = actions + [(c, i) for i in range(self.__board_size) if i != rc ]
        return actions

    def result(self, state, action):
        """Ritorna lo stato in cui si finisce se si esegue l'azione """
        (c,r) = action
        # crea una copia dello stato
        new_state = list(state)
        new_state[c] = r
        return new_state

    def goal_test(self, state):
        """ Ritorna true se lo stato è un goal, ovvero se non ci sono minacce"""
        return self.value(state) == 0

    def value(self, state):
        """ Funzione euristica del problema, calcola il numero di minacce"""
        minacce = 0
        # i -> colonna
        # ri -> riga della regina nella colonna i
        for i, ri in enumerate(state):
            # j -> colonna
            # rj -> riga della regina nella colonna j
            for j, rj in enumerate(state[i+1:]):
                # viene enumerata una lista più corta quindi è necessario aggiornare j
                # aggiungendo i
                j = j+i+1
                # le due regine si trovano sulla stessa riga
                if ri == rj:
                    minacce += 1
                # stessa diagonale 
                elif (j-i) == (rj-ri):
                    minacce += 1
                elif (j-i) == (ri-rj):
                    minacce += 1   
        return minacce

    def random_state(self):
        state = [random.randint(0, self.__board_size-1) for i in range(self.__board_size)]
        return state
        
    @staticmethod
    def string_state(state):
        # ┐ ─ └ ┴ ┬ ├ ┼ ┤ │ ┘ ┌
        # ┌─┬─┬─┐
        # │▓│ │ │
        # ├─┼─┼─┤
        # │ │▓│ │
        # ├─┼─┼─┤
        # │ │ │▓│
        # └─┴─┴─┘
        #
        print state
        size = len(state)
        str = "┌─"
        end = "└─"
        for i in range(size-1):
            str += "┬─"
            end += "┴─"
        str += "┐\n"
        end += "┘\n"
        for i in range(size):
            # preparo la riga
            row = "│"
            row2 = "├"
            for j in range(size):
                if i == state[j]:
                    row += "▓│"
                else:
                    row += " │"
                row2 += "─┼"
            # il -3 serve altrimenti rimane un ?, non so perché
            row2 = row2[:-3]+"┤"
            if i != size-1:
                str += row+"\n"+row2+"\n"
            else:
                str += row+"\n" 
        str += end
        return str









