#!/usr/bin/env python
# example from readme, run as PYTHONPATH=. python examples/random1.py

import duckylights
import random

def random_color():
  return hex(random.randint(0, 256**3 - 1))[2:].rjust(6, '0')

with duckylights.keyboard() as dev, dev.programming() as ducky:
  colors = [random_color() for i in range(6 * 22)]
  ducky.custom_mode(colors)
  input()
