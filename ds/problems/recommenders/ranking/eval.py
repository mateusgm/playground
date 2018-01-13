#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import heapq

from itertools import izip
from sklearn.metrics import *

def is_on_topk(row, label, k=3):
    preds  = zip(map(float,row), range(0,len(row)))
    ranked = heapq.nlargest(k, preds)
    preds, topk = zip(*ranked)
    return int(label) in topk

def parse_topk(row, label_row, exclusive=False):
    row   = row.strip().split(',')
    preds = row if exclusive else row[:label_i] + ( row[label_i+1:] if label_i != -1 else []  )
    label = label_row.strip().split(',')[label_i]
    return is_on_topk(preds, labels['i'][label], k=k)


# params

k         = int(sys.argv[1] or 3)
label_i   = int(sys.argv[2] or 0)
label_ext = len(sys.argv) > 3


# init

labels = pd.read_csv('csvs/targets.csv', names=['i','targets']).set_index('targets')
total  = .0
hits   = .0


# metrics

if label_ext:
    label_src = open(sys.argv[3])
    next(label_src) # skip header

    for row, label_row in izip(sys.stdin, label_src):
        hits  += parse_topk(row, label_row, exclusive=True)
        total += 1

else:
    for row in sys.stdin:
    hits  += parse_topk(row, row, exclusive=False)
    total += 1

# print "Top{}: {} / {}".format(k, hits / total, total)
print hits / total
