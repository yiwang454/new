
# HHEd -A -D -V -T 1 -H ./exp/R9/ml/hmm54/MODELS w ./new_models 

import os
import matplotlib.pyplot as plt
from collections import defaultdict

project_dir = '/project_bdda6/bdda/ywang/all.seem5330-project'

mpe_4 = [0.890441, 0.930231, 0.948934, 0.960577, 0.967147]
mpe_54 = [0.899335, 0.934925, 0.951746 , 0.960739 , 0.966571]

# plot 8.1
fig = plt.figure()

x_list = ['hmm{}'.format(i) for i in range(1, 6)]
print(x_list)
plt.plot(x_list,mpe_4, linestyle='-', marker='.', color='r', label='hmm4')
plt.plot(x_list,mpe_54, linestyle='-', marker='.', color='b', label='hmm54')


# x_ticks = list(range(1, 5))
# plt.xticks(x_ticks)
plt.xlabel('hmm training step')
plt.ylabel('minimum phone error rate)')
plt.legend(framealpha=0.6) # bbox_to_anchor=(1, 0), loc=3, borderaxespad=0
plt.savefig('./step_6_1.png')

