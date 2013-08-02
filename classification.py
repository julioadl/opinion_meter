import sys

dictionary = open(sys.argv[1])
data = []

for row in dictionary:
    word = row.split()
    data.append(word[:-1][0])

code_1 = ['save', 'safe', 'risk', 'casualties', 'SAFE', 'Safe', 'Risk']
code_2 = ['abroad']
code_3 = ['money', 'expense', 'cost', 'expensive', 'Money',  'EXPENS', 'Expens']
code_4 = ['preparation', 'training', 'trained', 'prepared']
code_5 = ['hurt', 'kill', 'Kill', 'KILL']
code_6 = ['target', 'TARGET', 'Target', 'precise', 'Precis', 'accura']
code_7 = ['surv', 'Surv', 'reconn']
code_8 = ['terrori', 'TERRORI', 'Terrori']
code_9 = ['techno', 'Techno']
code_10 = ['secre', 'spy', 'Secre', 'Spy', 'SPY']
code_book = {1:code_1, 2:code_2, 3:code_3, 4:code_4, 5:code_5, 6:code_6, 7:code_7, 8:code_8, 9:code_9, 10:code_10}

classifications = {}

for list in code_book:
    for term in code_book[list]:
        for item in data:
            if term in item:
                classifications[item] = list

for item in classifications:
    print item, classifications[item]

