# -*- coding: utf-8 -*-
from ortools.constraint_solver import pywrapcp
# Google or-tool disponibili su:
# https://github.com/google/or-tools

#####
# Esempi d'uso:

## Risolizione di un CPS
#problem = NQueens(8)
#solver = NQueensCSPSolver()
#sol = solver.solve(problem)

## Enumerazione delle soluzioni
#problem = NQueens(8)
#solver = NQueensCSPSolver()
#sol_count = solver.enumerate(problem)
#####

class NQueensCSPSolver(object):
    
    def __init__(self):
        self.__slv = pywrapcp.Solver('NQueensSolver')

    def solve(self, problem):
        size = len(problem.initial)
        # variabili
        x = [self.__slv.IntVar(0, size-1, 'x_%d'%n) for n in range(size)]
        # vincoli
        # Due regine non possono stare nella stessa riga
        self.__slv.Add(self.__slv.AllDifferent(x, True))

        # Due regine non possono stare nella stessa diagonale
        for i, xi in enumerate(x):
            for j,xj in enumerate(x):
                if i < j:
                    self.__slv.Add(xi - xj != j - i)
                    self.__slv.Add(xi - xj != - (j - i))

        ### Configurazione di default
        #decision_builder = self.__slv.Phase(x,
        #                        self.__slv.INT_VAR_DEFAULT,
        #                        self.__slv.INT_VALUE_DEFAULT)
        # Configurazione ad-hoc
        decision_builder = self.__slv.Phase(x,
                                self.__slv.CHOOSE_MIN_SIZE_LOWEST_MIN,
                                self.__slv.ASSIGN_MIN_VALUE) # Funziona bene anche con INT_VALUE_DEFAULT e MAX_VALUE
        self.__slv.NewSearch(decision_builder, [])
        solution = [-1 for v in x]
        if self.__slv.NextSolution():
            solution = [v.Value() for v in x]
            #print problem.string_state(solution)
            print problem.value(solution)
     

        self.__slv.EndSearch()
        print 'Numero di branch %d' % self.__slv.Branches()
        print 'Numero di fallimenti: %d' % self.__slv.Failures()
        print 'Tempo impiegato: %f (ms)' % self.__slv.WallTime()
        return solution


    def enumerate(self, problem):
        size = len(problem.initial)
        # variabili
        x = [self.__slv.IntVar(0, size-1, 'x_%d'%n) for n in range(size)]
        # vincoli
        # Due regine non possono stare nella stessa riga
        self.__slv.Add(self.__slv.AllDifferent(x, True))

        # Due regine non possono stare nella stessa diagonale
        for i, xi in enumerate(x):
            for j,xj in enumerate(x):
                if i < j:
                    self.__slv.Add(xi - xj != j - i)
                    self.__slv.Add(xi - xj != - (j - i))

        # Configurazione del risolutore
        decision_builder = self.__slv.Phase(x,
                                self.__slv.CHOOSE_MIN_SIZE_LOWEST_MIN,
                                self.__slv.ASSIGN_MIN_VALUE)   

        self.__slv.NewSearch(decision_builder, [])

        sol_count = 0
        solution = [-1 for v in x]
        while self.__slv.NextSolution():
            #print '##############'
            solution = [v.Value() for v in x]
            sol_count += 1
            #print problem.string_state(solution)
            #print problem.value(solution)
     

        self.__slv.EndSearch()
        #print 'Numero di soluzioni: %d' % sol_count
        #print 'Numero di branch %d' % self.__slv.Branches()
        #print 'Numero di fallimenti: %d' % self.__slv.Failures()
        #print 'Tempo impiegato: %f (ms)' % self.__slv.WallTime()
        return sol_count