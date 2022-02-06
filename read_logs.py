import os
import matplotlib.pyplot as plt
from collections import defaultdict

project_dir = '/project_bdda6/bdda/ywang/all.seem5330-project'


first_log_prob_list = [-7.594958e+01, -7.482834e+01, -7.465045e+01, -7.456168e+01]
x_list = [i for i in range(1, len(first_log_prob_list)+1)]


def get_step_acc_one(dir, feature, set_name = ['feb89', 'oct89', 'feb91', 'sep92']): # type=['wp', 'ng'], 
    acc_dict = defaultdict(list)
    for i in range(1, 5):
        for n in set_name:
            log_path = os.path.join(dir, 'hmm{}/test_wp_{}.{}/LOG'.format(i, n, feature))

            with open(log_path, 'r') as f_read:
                all_text = f_read.readlines()
                acc_str = all_text[-5].split(' ')[2]
                acc_num = float(acc_str.lstrip('Acc='))
                acc_dict[n].append(acc_num)
        
    return acc_dict

def latex_print(l):
    out = ''
    for item in l:
        out += str(item) + ' & '
    print(out)

DIR = '/project_bdda6/bdda/ywang/all.seem5330-project/exp/old_R1/ml/'

# ACC_DICT1 = get_step_acc_one(DIR, feature='1')
# ACC_DICT2 = get_step_acc_one(DIR, feature='2')
ACC_DICT3 = get_step_acc_one(DIR, feature='3')

# plot 1.2
fig = plt.figure()
colors = ['r', 'b', 'g', 'k']
for set, c in zip(ACC_DICT3, colors):
    # plt.plot(x_list, ACC_DICT1[set], linestyle='-', marker='o', color=c, label=set)
    # plt.plot(x_list, ACC_DICT2[set], linestyle='--', marker='.', color=c, label=set)
    print(set)
    # latex_print(ACC_DICT1[set])
    latex_print(ACC_DICT3[set])

# x_ticks = list(range(1, 5))
# plt.xticks(x_ticks)
# plt.xlabel('hmm iteration No.')
# plt.ylabel('Word accuracy')
# plt.legend(framealpha=0.6) # bbox_to_anchor=(1, 0), loc=3, borderaxespad=0
# plt.savefig('./step_1_2.png')

# # plot 1.1
# fig = plt.figure()
# p = plt.plot(x_list, first_log_prob_list, linestyle='-', marker='o', markerfacecolor='k')
# plt.xlabel('hmm iteration No.')
# plt.ylabel('Training data log-likelihood (per frame)')
# x_ticks = list(range(1, 5))
# plt.xticks(x_ticks)
# plt.savefig('./step_1_0.png')


    