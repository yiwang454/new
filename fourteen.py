import os
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np


add1 = [3, 82, 515, 82, 5, 2, 0, 0, 0, 0]
add2 = [3, 82, 515, 82, 3, 1, 1, 2, 0, 0]
add3 = [3, 82, 515, 82, 3, 1, 0, 1, 1, 1]
adds = [add1, add2, add3]
x_ticks = list(range(4, 14))



x = np.arange(len(x_ticks))  # the label locations
width = 0.1  # the width of the bars

fig = plt.figure()
plt.bar(x - width, add1, width, label='hmm0')
plt.bar(x , add2, width, label='hmm10')
plt.bar(x + width, add3, width, label='hmm20')

# Add some text for labels, title and custom x-axis tick labels, etc.
plt.xlabel('Number of Gaussian per state')
plt.ylabel('Number of states')
plt.xticks(x, x_ticks)
plt.legend(framealpha=0.6)



plt.tight_layout()
plt.savefig('./step_7_0.png')