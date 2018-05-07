# -*- coding: utf-8 -*-
'''
import random

hafezFile = open('hafez.txt', "r", encoding="utf8")
data_list_hafez = hafezFile.readlines()
hafezFile.close()

molanaFile = open('molana.txt', "r", encoding="utf8")
data_list_molana = molanaFile.readlines()
hafezFile.close()

testFile = open('test.txt', "w", encoding="utf8")
j = 1
for i in range(1, 400):
    rand = random.randint(1, 4000)
    if data_list_hafez[rand] != '\n' :
        if j == 1 :
            text = '1'
        text = text + '\t' + data_list_hafez[rand].strip('\n')
        j += 1
        if j == 4 :
            j = 1
            text = text + "\n"
            testFile.write(text)
        del data_list_hafez[rand]
    else :
        i = i - 1
j = 1
for i in range(1, 400):
    rand = random.randint(1, 4000)
    if data_list_molana[rand] != '\n':
        if j == 1 :
            text = '2'
        text = text + '\t' + data_list_molana[rand].strip('\n')

        j += 1
        if j == 4:
            j = 1
            text = text + "\n"
            testFile.write(text)

        del data_list_molana[rand]
    else:
        i = i - 1

testFile.close()

hafezFile = open("hafezTrain.txt", "w", encoding="utf8")
hafezFile.writelines(data_list_hafez)
hafezFile.close()

molanaFile = open("molanaTrain.txt", "w", encoding="utf8")
molanaFile.writelines(data_list_molana)
molanaFile.close()
'''

import  math

def findWord(file, word):
    for line in file:
        parts = line.split()
        if parts[0] == word:
            file.close()
            return int(parts[1])
    file.close()
    return 0

def num_words(file):
    words = [word for line in file for word in line.split()]
    print ("The total word count is:", len(words))
    return len(words)


def naiveBayes(word, fileAddress, classCountWords, v) :
    file = open(fileAddress, 'r', encoding='utf-8')

    wordCount = findWord(file, word)

    wordPercent = float(wordCount) / classCountWords
    wordPercentS = (float(wordCount) + 1) / (classCountWords + v)       # .... smoothing 1
    return wordPercent, wordPercentS


hafezFile = open("hafezTrain.txt", 'r', encoding='utf-8')
hafez_size = num_words(hafezFile)

molanaFile = open("molanaTrain.txt", 'r', encoding='utf-8')
molana_size = num_words(molanaFile)

wordsCount = hafez_size + molana_size

hafezP = float (hafez_size) / wordsCount
molanaP = float (molana_size) / wordsCount

hafezSortFile = open("hafezSort.txt", 'r', encoding='utf-8')
v_hafez = len(hafezSortFile.readlines(  ))
hafezSortFile.close()

molanaSortFile = open("molanaSort.txt", 'r', encoding='utf-8')
v_molana = count = len(molanaSortFile.readlines(  ))

print(v_molana, v_hafez)

testFile = open('test.txt', 'r', encoding='utf-8')
lines = testFile.readlines()

tp = 0
tn = 0
fp = 0
fn = 0

tp_S = 0
tn_S = 0
fp_S = 0
fn_S = 0

for line in lines :
    words = line.split()
    E_hafezP = 0
    E_hafezP_S = 1

    E_molanaP = 0
    E_molanaP_S = 1

    hafezZiroFlag = 0
    molanaZiroFlag = 0

    if len(words) != 0 :
        #print(words)
        for i in range(len(words)) :
            if i != 0 :
                hafezWordP, hafezWordP_S = naiveBayes(words[i], "hafezSort.txt", hafez_size, v_hafez)

                if hafezWordP != 0 and hafezZiroFlag == 0:
                    E_hafezP = abs(math.log10(hafezWordP)) + E_hafezP
                else :
                    hafezZiroFlag = 1
                E_hafezP_S = hafezWordP_S * E_hafezP_S

                molanaWordP, molanaWordP_S = naiveBayes(words[i], "molanaSort.txt", molana_size, v_molana)

                if molanaWordP != 0 and molanaZiroFlag == 0:
                    E_molanaP = abs(math.log10(molanaWordP)) + E_molanaP
                else:
                    molanaZiroFlag = 1
                E_molanaP_S = molanaWordP_S * E_molanaP_S

        if hafezZiroFlag == 0 :
            naivebayesHafez = abs(math.log10(hafezP)) + E_hafezP
        else:
            naivebayesHafez = 0

        if molanaZiroFlag == 0 :
            naivebayesMolana = abs(math.log10(molanaP)) + E_molanaP
        else:
            naivebayesMolana = 0

        naivebayesHafez_S = hafezP * E_hafezP_S
        naivebayesMolana_S = molanaP * E_molanaP_S

        naivebayesHafez_S = abs(math.log10(naivebayesHafez_S))
        naivebayesMolana_S = abs(math.log10(naivebayesMolana_S))

        if naivebayesHafez > naivebayesMolana :
            nClass = 1
        else:
            nClass = 2

        if naivebayesHafez_S < naivebayesMolana_S :
            nClass_S = 1
        else:
            nClass_S = 2

        if words[0] == '1' :   #t
            if nClass == 1 :    #tp
                tp += 1
            else:   #tn
                fp += 1
        else:   #f
            if nClass == 2: #fp
                tn += 1
            else:   #fn
                fn += 1
#..........................* with smoothing*............................

        if words[0] == '1':  # t
            if nClass_S == 1:  # tp
                tp_S += 1
            else:  # tn
                fp_S += 1
        else:  # f
            if nClass_S == 2:  # fp
                tn_S += 1
            else:  # fn
                fn_S += 1

print('tp : ', tp, '\ttn :', tn, '\tfp : ', fp, 'fn : ', fn)

precision = float(tp) / (tp + fp)
recall = float(tp) / (tp + fn)

print ('precision : ', precision)
print('recall : ', recall)


print('tp_S : ', tp_S, '\ttn_S :', tn_S, '\tfp_S : ', fp_S, 'fn_S : ', fn_S)

precision_S = float(tp_S) / (tp_S + fp_S)
recall_S = float(tp_S) / (tp_S + fn_S)

print ('precision_S : ', precision_S)
print('recall_S : ', recall_S)