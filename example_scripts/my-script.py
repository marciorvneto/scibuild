#!/usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as pl

args = sys.argv[1:]
counts = float(args[0])
trials = int(args[1])
for i in range(trials):
          x = np.random.random()
          y = np.random.random()
          x2 = x**2
          y2 = y**2
          x_y = x2 + y2
          dxy = np.sqrt(x_y)
          if dxy <= 1:
                    counts = counts + 1

print ("pi was approximated at ::",4*counts/trials)
