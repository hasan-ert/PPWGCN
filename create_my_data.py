import json
import random

input_file = './data/netbeans_my.json'

start_file_name = input_file
with open(start_file_name, 'r', encoding='utf-8') as fin:
    all_bugs_info = [json.loads(line.strip()) for line in fin.readlines()]
random.shuffle(all_bugs_info)
count_dict = {"1":0, "2":0, "3":0, "4":0, "5":0}
for rep in all_bugs_info:
    count_dict[rep["priority"]] += 1    

train_rates = ["0.5", "0.4", "0.3", "0.2", "0.1"]
for rate in train_rates:
    limit_dict = {"1":0, "2":0, "3":0, "4":0, "5":0}
    labels_list = []
    des_list = []
    my_method_list = []
    train_or_test_list = []
    for line in all_bugs_info:
        my_method_list.append(line["my_method"])
        des_list.append(line["description"])
        labels_list.append(line["priority"])
        limit_dict[line["priority"]] += 1
        if limit_dict[line["priority"]] <= int(count_dict[line["priority"]] * float(rate)):
                train_or_test_list.append('train')
        else:
            train_or_test_list.append('test')
    dataset_name_1 = 'netbeans' + '_' + 'my_method' + "_" + rate
    meta_data_list = []
    for i in range(len(my_method_list)):
        meta = str(i) + '\t' + train_or_test_list[i] + '\t' + labels_list[i]
        meta_data_list.append(meta)
    meta_data_str = '\n'.join(meta_data_list)
    f = open('data/' + dataset_name_1 + '.txt', 'w')
    f.write(meta_data_str)
    f.close()
    corpus_str = '\n'.join(my_method_list)
    f = open('data/corpus/' + dataset_name_1 + '.txt', 'w')
    f.write(corpus_str)
    f.close()

    dataset_name_2 = 'netbeans' + '_' + 'description' + "_" + rate
    meta_data_list = []
    for i in range(len(des_list)):
        meta = str(i) + '\t' + train_or_test_list[i] + '\t' + labels_list[i]
        meta_data_list.append(meta)
    meta_data_str = '\n'.join(meta_data_list)
    f = open('data/' + dataset_name_2 + '.txt', 'w')
    f.write(meta_data_str)
    f.close()
    corpus_str = '\n'.join(des_list)
    f = open('data/corpus/' + dataset_name_2 + '.txt', 'w')
    f.write(corpus_str)
    f.close()
