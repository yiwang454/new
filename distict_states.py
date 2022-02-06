import os
import matplotlib.pyplot as plt
from collections import defaultdict
import re

project_dir = '/project_bdda6/bdda/ywang/all.seem5330-project'
DIR = os.path.join(project_dir, 'samples/RMHTK/lib/dicts/mono.hd.dct')
TREE = os.path.join(project_dir, 'exp/R9/ml/treeg.list')
TIE = os.path.join(project_dir, 'exp/R7/ml/hmm2/stats')

state = 'sh-n+b'

with open(TREE, 'r') as read_stat:
    trees =read_stat.readlines()

with open(TIE, 'r') as read_stat:
    ties =read_stat.readlines()

for tree in trees:
    s = re.split(r"[ ]+", tree.rstrip())
    if len(s)== 2:
        if s[1] == state:
            key = s[0]
            print(key)


# count = 2
# triphone_set = set()
# for i, l in enumerate(lines):
#     if i > 2:
#         chars = re.split(r"[ ]+", l.rstrip())[1:]
#         # print(len(chars))
#         if len(chars) == 1:
#             raise ValueError('wrong')
#         elif len(chars) == 2:
#             triphone_set.add("sil-{}+{}".format(chars[0], chars[1]))
#             triphone_set.add("{}-{}+sil".format(chars[0], chars[1]))
#         else:
#             for j in range(len(chars)-2):
#                 triphone_set.add("{}-{}+{}".format(chars[j], chars[j+1], chars[j+2]))

# print(len(triphone_set) + 2)
            
        

