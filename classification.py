import sys

dictionary = open(sys.argv[1])
data = []

for row in dictionary:
    data.append(row)

new_dict = []

for row in data:
    score = int(row.split()[-1])
    if score != 0:
        word = row.split()[:-1]
        new_dict.append(word[0])

code_1 = ['save', 'safe', 'risk', 'casualties']
code_2 = ['abroad']
code_3 = ['money', 'expense', 'cost', 'expensive']
code_4 = ['preparation', 'training', 'prepared']
code_5 = ['hurt', 'kills']
code_6 = ['target', 'precise', 'accura']
code_7 = ['surv', 'reconn']
code_8 = ['terrori']
code_9 = ['tech']
code_10 = ['secre', 'spy']
code_book = {1:code_1, 2:code_2, 3:code_3, 4:code_4, 5:code_5, 6:code_6, 7:code_7, 8:code_8, 9:code_9, 10:code_10}

classifications = {}

for list in code_book:
    for term in code_book[list]:
        for item in new_dict:
            if term in item:
                print item, list
#            else:
 #               print item, 10
