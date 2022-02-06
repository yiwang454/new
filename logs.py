import os
import matplotlib.pyplot as plt
from collections import defaultdict

project_dir = '/project_bdda6/bdda/ywang/all.seem5330-project'

# less_DIR = os.path.join(project_dir, 'exp/R16_lesslayer/dnntrain/dnn5.finetune')
# more_DIR = os.path.join(project_dir, 'exp/R16_deeper/dnntrain/dnn9.finetune')

# less_DIR = os.path.join(project_dir, 'exp/R16_shortcontext/dnntrain/dnn7.finetune')
# more_DIR = os.path.join(project_dir, 'exp/R16_context/dnntrain/dnn7.finetune')

def get_step_acc_one(four_dir, set_name = ['feb89', 'oct89', 'feb91', 'sep92']): # type=['wp', 'ng'], 
    
    acc_list = []
    for n in set_name:
        log_path = os.path.join(four_dir, 'test_wp_{}.1/LOG'.format(n))

        with open(log_path, 'r') as f_read:
            all_text = f_read.readlines()
            acc_str = all_text[-5].split(' ')[2]
            acc_num = float(acc_str.lstrip('Acc='))
            acc_list.append(acc_num)
    print(' & '.join(list(map(str ,acc_list))))
        

get_step_acc_one(less_DIR)
get_step_acc_one(more_DIR)