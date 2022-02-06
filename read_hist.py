import os
import matplotlib.pyplot as plt
from collections import defaultdict
import re

project_dir = '/project_bdda6/bdda/ywang/all.seem5330-project'
DIR = os.path.join(project_dir, 'exp/R9/ml/hmm4/stats')

with open(DIR, 'r') as read_stat:
    lines =read_stat.readlines()

bins = ['0', '0-10', '10-30']
bins += ['{}-{}'.format(i*30, (i+1)*30) for i in range(1, 8)]
bins += ['>240']

freq_dict = dict.fromkeys(bins, 0)
all_freq = 0
for i, l in enumerate(lines):
    freq = int(re.split(r"[ ]+", l)[2])
    all_freq += freq
    if freq == 0:
        freq_dict['0'] += 1
    elif freq > 0 and freq <= 10:
        freq_dict['0-10'] += 1
    elif freq <= 30:
        freq_dict['10-30'] += 1
    elif freq > 240:
        freq_dict['>240'] += 1
    else:
        right = ((freq+29) // 30) * 30
        left = right - 30
        freq_dict['{}-{}'.format(left, right)] += 1

print(all_freq)
print(len(lines))
print(all_freq / len(lines))
# plot 2.1
fig = plt.figure()
plt.bar(freq_dict.keys(), freq_dict.values(), width=0.3, )
plt.xlabel('Histogram of frame posterior occupancy')
plt.ylabel('Number of tied states instance')
plt.xticks(rotation=90)

for i, v in enumerate(freq_dict.values()):
    plt.text(i - .25, v + 5, str(v), color='k')

plt.tight_layout()
plt.savefig('./step_3_0.png')