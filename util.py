# -*- coding: utf-8 -*-
import random
import time

class Timer(object):
    def start(self):
        self.__time = time.clock()

    def stop(self):
        return time.clock() - self.__time

def argmax_random_tie(seq, fn):
    "Return an element with highest fn(seq[i]) score; break ties at random."
    return argmin_random_tie(seq, lambda x: -fn(x))

def argmin_random_tie(seq, fn):
    """Return an element with lowest fn(seq[i]) score; break ties at random.
    Thus, for all s,f: argmin_random_tie(s, f) in argmin_list(s, f)"""
    best_score = fn(seq[0]); n = 0
    for x in seq:
        x_score = fn(x)
        if x_score < best_score:
            best, best_score = x, x_score; n = 1
        elif x_score == best_score:
            n += 1
            if random.randrange(n) == 0:
                best = x
    return best

def weighted_choice(choices):    
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    for c, w in choices:
        r -= w 
        if r <= 0:
            return c
    assert False, "Errore nella distribuzione"
              



