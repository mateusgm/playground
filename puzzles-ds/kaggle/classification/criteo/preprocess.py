#!/usr/bin/env python

import sys
import csv
import numpy as np

def f(vals, prefix=None):
    return [
        ( "%s%s:%s" % ( prefix, i, vals[i]) if prefix else vals[i] )
        for i in range(len(vals))
        if  vals[i] != '' and vals[i] != '0'
    ]

def vw_line(label, **nss):
    fmt  = "{}" * ( len(nss) + 1 )
    vals = [ " |{} {}".format(ns, " ".join(fts)) for ns, fts in nss.items() ]
    return fmt.format( label, *vals )

reader = csv.reader( sys.stdin, delimiter="\t" )
test_i = -1 if len(sys.argv) > 1 else 0

for line in reader:
    print vw_line( 
            test_i or int(line[0]) or -1,
            I=f( line[1 +test_i : 14+test_i], 'i' ),
            C=f( line[14+test_i :  ] ))
