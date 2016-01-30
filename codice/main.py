#!/usr/bin/env python
# -*- coding: utf-8 -*-

from search import HillClimbingLateralSearch, HillClimbingSearch, HillClimbingStocasticSearch, HillClimbingRandomRestartSearch, Node, SimulatedAnnealingSearch
from problem import NQueens
from csp import NQueensCSPSolver
from util import util

import math
import csp_search as csp
import csv
csv.register_dialect('lol', delimiter=';')

# Funzione di raffreddamento per SA
def exp_schedule(k=20, lam=0.05, limit=1000):
    "One possible schedule function for simulated annealing"
    return lambda t: k * math.exp(-lam * t) if t < limit else 0

# Funzione di test per un oggetto della classe search
# - search: oggetto da usare per la ricerca
# - times: numero di prove da effettuare
# - problems: lista di oggetti Problem da risolve, ognuno viene risolto times volte
# - random: booleano che specifica se la ricerca parte da uno stato casuale o meno
# - fname: percorso relativo del file csv nel quale salvare i risultati delle prove
def test(search, times, problems, random, fname):
    results = []
    timer = util.Timer()
    print 'n\ttime\t\tmoves\topt'
    for problem in problems:
        tot_time = 0.0
        tot_moves = 0.0
        tot_opt = 0.0
        for i in range(times): # times prove
            timer.start()
            if random:
                random_state = problem.random_state()
                (state, node, cnt) = search.search_from_state(problem, random_state)
            else:
                (state, node, cnt) = search.search(problem)
            t = timer.stop()
            tot_time += t
            tot_moves += cnt
            if problem.value(state) == 0:
                tot_opt += 1

        results.append({'n':len(problem.initial), 'avgt':tot_time/times, 'avgm':tot_moves/times,'opt': tot_opt})
        print len(problem.initial),'\t', tot_time/times,'\t', tot_moves/times,'\t', tot_opt
    
    with open(fname, 'w') as csvfile:
        fieldnames = ['n', 'avgt', 'avgm', 'opt']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='lol')

        writer.writeheader()
        writer.writerows(results)

def main():
    print 'start'

    timer = util.Timer()
    problems = [NQueens(n) for n in range(4,26)]
    timer.start()

    times = 10

    print 'HillClimbingSearch'
    test(HillClimbingSearch(), times, problems, False, 'hill_climbing.csv')
    test(HillClimbingSearch(), times, problems, True, 'random_hill_climbing.csv')

    print 'HillClimbingLateralSearch'
    test(HillClimbingLateralSearch(), times, problems, False, 'hill_climbing_lateral.csv')
    test(HillClimbingLateralSearch(), times, problems, True, 'random_hill_climbing_lateral.csv')

    print 'HillClimbingStocasticSearch'
    test(HillClimbingStocasticSearch(), times, problems, False, 'hill_climbing_stocastic.csv')
    test(HillClimbingStocasticSearch(), times, problems, True, 'random_hill_climbing_stocastic.csv')

    print 'HillClimbingRandomRestartSearch(HillClimbingSearch)'
    test(HillClimbingRandomRestartSearch(True, HillClimbingSearch()), times, problems, False, 'hill_climbing_restart.csv')
    test(HillClimbingRandomRestartSearch(True, HillClimbingSearch()), times, problems, True, 'random_hill_climbing_restart.csv')

    print 'HillClimbingRandomRestartSearch(HillClimbingLateralSearch)'
    test(HillClimbingRandomRestartSearch(True, HillClimbingLateralSearch()), times, problems, False, 'hill_climbing_restart_lateral.csv')
    test(HillClimbingRandomRestartSearch(True, HillClimbingLateralSearch()), times, problems, True, 'random_hill_climbing_restart_lateral.csv')

    print 'HillClimbingRandomRestartSearch(HillClimbingStocasticSearch)'
    test(HillClimbingRandomRestartSearch(True, HillClimbingStocasticSearch()), times, problems, False, 'hill_climbing_restart_stocastic.csv')
    test(HillClimbingRandomRestartSearch(True, HillClimbingStocasticSearch()), times, problems, True, 'random_hill_climbing_restart_stocastic.csv')

    print "Tempo totale", timer.stop()


## Codice che confronta le due funzioni di raffreddamento diverse per SA
#sa1 = SimulatedAnnealingSearch()
#sa2 = SimulatedAnnealingSearch(minimize = True, temperature_fn= exp_schedule(k=20, lam=0.005, limit =100))
#problem = NQueens(6)
#
#sa1_opt = 0
#sa1_sub = 0
#sa2_opt = 0
#sa2_sub = 0
#for i in range(1000):
#    r_state = problem.random_state()
#    (s,n,cnt) = sa1.search_from_state(problem, r_state)
#    (s2, n2, cnt2) = sa2.search_from_state(problem, r_state)
#    print "Giro",i
#    if problem.value(s) == 0:
#        sa1_opt += 1
#    else:
#        sa1_sub += 1
#    if problem.value(s2) == 0:
#        sa2_opt += 1
#    else:
#        sa2_sub += 1
#
#
#print sa1_opt, sa1_sub
#print sa2_opt, sa2_sub

#problem = NQueens(300)
#solver = NQueensCSPSolver()
#solver.solve(problem)





## Codice che stampa un po' di stati generati casualmente
#states = {}
#p = NQueens(4)
#for i in range(300):
#    state = p.random_state()
#    str_state = '<'+','.join(str(x) for x in state)+'>'
#    #print str_state
#    if str_state in states:
#        states[str_state] += 1
#    else:
#        states[str_state] = 1
#data = []
#for i, s in enumerate(states):
#    data.append({'state':s, 'cnt':states[s]})
#
#with open('state_stats.csv', 'w') as csvfile:
#    fieldnames = ['state', 'cnt']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='lol')
#    writer.writeheader()
#    writer.writerows(data)

if __name__ == "__main__":
    main()