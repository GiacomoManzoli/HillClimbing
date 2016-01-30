#!/usr/bin/env python
# -*- coding: utf-8 -*-

from search import HillClimbingLateralSearch, HillClimbingSearch, HillClimbingStocasticSearch, HillClimbingRandomRestartSearch, Node, SimulatedAnnealingSearch
from problem import NQueens
from csp import NQueensCSPSolver
from util import util

import math
import csv
csv.register_dialect('lol', delimiter=';')

# 300 -> 5533ms
# 314 -> 7552ms

problem = NQueens(14)

solver = NQueensCSPSolver()

s = solver.enumerate(problem)
print s
#print problem.string_state(s)