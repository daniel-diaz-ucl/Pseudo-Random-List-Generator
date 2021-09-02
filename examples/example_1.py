import csv
import stimlist as stl

f = open("test.csv","r")
cc = csv.reader(f)
next(cc)
in_seq = []
for row in cc: in_seq.append(row)

mylist = stl.StimList(in_seq,2,k=3)

mylist = mylist.prand_seq()
