import csv
import stimlist as stl

f = open("test.csv", "r")
cc = csv.reader(f)
next(cc)
in_seq = []
for row in cc:
    in_seq.append(row)

my_list = stl.StimList(in_seq, 2, k=3)

my_list = my_list.prand_seq()

# mynewlist = [y for x,y in sorted(zip(mylist,in_seq))]
#
# inp = [['1','blue','road','motorbike'],['2','red','air','helicopter'],['3','green','sea','ship'],['4','white','air','airplane'],['5','black','road','car']]
# outp = [['5','car'],['4','airplane'],['3','ship'],['2','helicopter'],['1','motorbike']]
#
# mynewlist = [idx for idx,trial in enumerate(outp) if '4' in trial]


print(my_list)
# print(' ')
# print(mynewlist)
