# !/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

# here we use the number one for the example adding the subfolders in the path
from ..src.stim_list import stimlist as stl

# import the module.

# Two options:
# 1. Copy the module stimlist.py to the folder together with your main python script
# and then import it using:
#       import stimlist as stl

# 2. Install the package and import the module from it
#       from prlgen import stimlist as stl


# load your csv file
f = open("test.csv", "r")
cc = csv.reader(f)
next(cc)
in_seq = []
for row in cc:
    in_seq.append(row)

# First: call the module with your parameters.
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
