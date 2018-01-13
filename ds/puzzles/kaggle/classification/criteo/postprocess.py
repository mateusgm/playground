#!/usr/bin/env python

import sys
import csv
import numpy as np

counter = 1
print "Id,Predicted"

for line in sys.stdin:
    print "%d,%s" % (counter,line.strip("\n"))
    counter += 1
