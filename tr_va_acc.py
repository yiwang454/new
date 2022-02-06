
import os
import matplotlib.pyplot as plt
import re

project_dir = '/project_bdda6/bdda/ywang/all.seem5330-project'

less_DIR = os.path.join(project_dir, 'exp/R16_lesslayer/dnntrain')
# more_DIR = os.path.join(project_dir, 'exp/R16_context/dnntrain')

train_acc = [38.72, 37.79, 40.46, 41.37, 43.10, 52.97, 56.36, 58.85]
valid_acc = [44.55, 45.08, 46.30, 47.03, 47.69, 50.72, 52.11, 53.33]

x_list = ['dnn{}'.format(i) for i in range(3, 5)]
dir_list = x_list + ['dnn5.finetune']
newx_list = x_list + ['dnn5_{}'.format(j) for j in range(1, 5)]
print(dir_list)
print(newx_list)

def get_step_acc_one(four_dir): # type=['wp', 'ng'], 
    
    tr_acc_list = []
    va_acc_list = []
    for d in dir_list:

        log_path = os.path.join(four_dir, d, 'LOG')

        with open(log_path, 'r') as f_read:
            all_text = f_read.readlines()
            for a in all_text:
                if 'Train Accuracy =' in a:
                    tr_acc = float(re.split(r"[ ]+", a)[3].rstrip('%'))
                    tr_acc_list.append(tr_acc)
                elif 'Validation Accuracy =' in a:
                    va_acc = float(re.split(r"[ ]+", a)[3].rstrip('%'))
                    va_acc_list.append(va_acc)
    return tr_acc_list, va_acc_list

    # print(' & '.join(list(map(str ,acc_list))))


tr_acc_list_ls, va_acc_list_ls = get_step_acc_one(less_DIR)
# tr_acc_list_m, va_acc_list_m = get_step_acc_one(more_DIR)

# plot 8.1
fig = plt.figure()


plt.plot(newx_list,tr_acc_list_ls, linestyle='-', marker='.', color='r', label='train acc')
plt.plot(newx_list,va_acc_list_ls, linestyle='-', marker='.', color='b', label='valid acc')

# plt.xticks(newx_list)
plt.xlabel('dnn training step')
plt.ylabel('Word accuracy')
plt.legend(framealpha=0.6) # bbox_to_anchor=(1, 0), loc=3, borderaxespad=0
plt.savefig('./step_8_2.png')

