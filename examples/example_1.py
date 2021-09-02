import csv
import src.stim_list as stl

f = open("test.csv", "r")
cc = csv.reader(f)
next(cc)
in_seq = []
for row in cc:
    in_seq.append(row)

my_list = stl.StimList(in_seq, 2, k=3)

# my_list = my_list.prand_seq()

print(my_list)
