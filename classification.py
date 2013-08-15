import sys

#Creates a dictionary with the following words to make a codebook

dictionary = open(sys.argv[1])
#array that loads dictionary information.
data = []

for row in dictionary:
    word = row.split()
    data.append(word[:-1][0])

code_1 = ['save','safe', 'risk', 'casu', 'removes', 'reduces', 'pilot', 'danger', 'troop', 'personn', 'crew']
code_2 = ['abroad']
code_3 = ['money', 'expense', 'cost', 'expensive', 'effic', 'effecti', 'spend', 'cheap']
code_4 = ['preparation', 'training', 'trained', 'prepared']
code_5 = ['hurt', 'kill', 'Kill']
code_6 = ['targeti', 'precis', 'accura']
code_7 = ['surv', 'reconn']
code_8 = ['terrori']
code_9 = ['techno']
code_10 = ['secre', 'spy', 'watch', 'covert']
code_11 = [ 'well', 'useful']
code_90 = ['nothing']
code_91 = ['terrible', 'horr']
code_97 = ['dono','know']
code_98 = ['enough']
code_99 = ['dk','d/k']
code_book = {1:code_1, 2:code_2, 3:code_3, 4:code_4, 5:code_5, 6:code_6, 7:code_7, 8:code_8, 9:code_9, 10:code_10, 11:code_11, 90:code_90, 91:code_91, 97: code_97, 98:code_98, 99:code_99}

#dictionary for the classifications
class_dict = {}

for lst in code_book:
    for term in code_book[lst]:
        for item in data:
            lower_case = item.lower()
            if term in lower_case:
                class_dict[lower_case] = lst

#Classifies the data
#File with the phrases/sentences to be classified.
file = open(sys.argv[2])
#dictionary that assigns a classification to a phrase/sentence
data2 = {}

for row in file:
    phrase = row.split()[:-1]
    #lc stands for "lower case"
    lc_phrase = []
    for word in phrase:
        lc_phrase.append(word.lower())
    codes = []
    for term in class_dict:
        if term in lc_phrase:
            codes.append(class_dict[term])
    classif = list(set(codes))
    sentence = " ".join(phrase)
    data2[sentence] = classif

for item in data2:
    print item, data2[item]
    
    
