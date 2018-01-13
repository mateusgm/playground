#!/bin/sh

# A simplest-possible example of parallel code at work on a single machine.
./spanning_tree

params="--loss_function squared -b 25 --l2 1e-3 --passes 2 --span_server localhost"

head -n 1000000 | vw --total 2 --node 0 --unique_id 0 --cache_file c0 -k $params > node_0 2>&1 &
tail -n 1000000 | vw --total 2 --node 1 --unique_id 0 --cache_file c1 -k $params

killall spanning_tree
