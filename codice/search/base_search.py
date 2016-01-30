# -*- coding: utf-8 -*-
class BaseSearch(object):
    """Classe astratta che rappresenta un algortimo di ricerca"""
    def search(self, problem):
        """Effettua la ricerca a partire dallo stato iniziale del problema"""
        abstract

    def search_from_state(self, problem, state):
        """Effettua la ricerca a partire da uno stato specifico del problema"""
        abstract