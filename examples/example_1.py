# !/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
# import the module
# Usually copy the module stimlist.py to the folder together with your main python script
# and then import it using:
#       import stimlist as stl
import src.stim_list as stl

# load your csv file
f = open("test.csv", "r")
cc = csv.reader(f)
next(cc)
in_seq = []
for row in cc:
    in_seq.append(row)

# First: call the package with your parameters.
# In this example the parameters are:
#   in_seq: the input list from the csv file
#   exp_cond = 2: index of the experimental condition column, starts counting at zero
#   trial_id = 0: index of the trial id/trial number column, starts counting at zero, default value is zero
#   k = 3: number of consecutive repetitions allowed for any experimental condition, default value is one
my_list = stl.StimList(in_seq, 2, k=3)

# Second: call the main method to shuffle your list with the parameters
my_list = my_list.prand_seq()

# Your list is ready to use
print(my_list)
