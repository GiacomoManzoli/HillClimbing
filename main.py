#!/usr/bin/env python
# -*- coding: utf-8 -*-

from search import HillClimbingLateralSearch, HillClimbingSearch, HillClimbingStocasticSearch, HillClimbingRandomRestartSearch
from problem import NQueens
import util

import csv
csv.register_dialect('lol', delimiter=';')


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

    times = 1000

   

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
    

if __name__ == "__main__":
    main()