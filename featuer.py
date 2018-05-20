# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from hazm import *


file = open('C:\mallet\data.txt', 'w', encoding='utf-8')
file.close()

file = open('vwFile1.txt', 'r', encoding='utf-8')

textF = file.readlines()
file1 = open('C:\mallet\data.txt', 'a', encoding='utf-8')

tagger = POSTagger(model='resources/postagger.model')

exist = [None]*100
textLine = [None]*100

for i, line in zip(range(0, 2795), textF) :
    textLine[1] = line.split('		')[1].split(' ')[0]
    textLine[2] = line.split('		')[0].split(' ')[2]

    textTag = tagger.tag(word_tokenize(line))

    if 'تبریزی' in line :
        exist[1] = '1'
    else:
        exist[1] = '0'

    if 'تبریز' in line :
        exist[2] = '1'
    else:
        exist[2] = '0'

    if 'جان' in line :
        exist[3] = '1'
    else:
        exist[3] = '0'

    if 'تو' in line :
        exist[4] = '1'
    else:
        exist[4] = '0'

    if 'چون' in line :
        exist[5] = '1'
    else:
        exist[5] = '0'

    if 'عشق' in line :
        exist[6] = '1'
    else:
        exist[6] = '0'

    if 'عقل' in line :
        exist[7] = '1'
    else:
        exist[7] = '0'

    if 'جمله' in line :
        exist[8] = '1'
    else:
        exist[8] = '0'

    if 'های' in line :
        exist[9] = '1'
    else:
        exist[9] = '0'

    if 'نور' in line :
        exist[10] = '1'
    else:
        exist[10] = '0'

    if 'حافظ' in line :
        exist[11] = '1'
    else:
        exist[11] = '0'

    if 'باد' in line :
        exist[12] = '1'
    else:
        exist[12] = '0'

    if 'شمع' in line :
        exist[13] = '1'
    else:
        exist[13] = '0'

    if 'زلف' in line :
        exist[14] = '1'
    else:
        exist[14] = '0'

    if 'یاد' in line :
        exist[15] = '1'
    else:
        exist[15] = '0'

    if 'دوست' in line :
        exist[16] = '1'
    else:
        exist[16] = '0'

    if 'ساقی' in line :
        exist[17] = '1'
    else:
        exist[17] = '0'

    if 'صبا' in line :
        exist[18] = '1'
    else:
        exist[18] = '0'

    if 'رب' in line :
        exist[19] = '1'
    else:
        exist[19] = '0'

    if 'خاک' in line :
        exist[20] = '1'
    else:
        exist[20] = '0'


    if i % 2 :
        className = 'molana'
    else :
        className = 'hafez'

    file1.write(str(i) +' '+ className +' '+
                'f1' +' '+ textLine[1]+' '+
                'f2' +' '+ textLine[2]+ ' ' +
                'f3' + ' ' + exist[1]
                + ' ' + 'f4' + ' ' + exist[2]
                + ' ' + 'f5' + ' ' + exist[3]
                + ' ' + 'f6' + ' ' + exist[4]
                + ' ' + 'f7' + ' ' + exist[5]
                + ' ' + 'f8' + ' ' + exist[6]
                + ' ' + 'f9' + ' ' + exist[7]
                + ' ' + 'f10' + ' ' + exist[8]
                + ' ' + 'f11' + ' ' + exist[9]
                + ' ' + 'f12' + ' ' + exist[10]
                + ' ' + 'f13' + ' ' + exist[11]
                + ' ' + 'f14' + ' ' + exist[12]
                + ' ' + 'f15' + ' ' + exist[13]
                + ' ' + 'f16' + ' ' + exist[14]
                + ' ' + 'f17' + ' ' + exist[15]
                + ' ' + 'f18' + ' ' + exist[16]
                + ' ' + 'f19' + ' ' + exist[17]
                + ' ' + 'f20' + ' ' + exist[18]
                + ' ' + 'f21' + ' ' + exist[19]
                + ' ' + 'f22' + ' ' + exist[20]
                + ' ' + 'f23' + ' ' + textTag[0][1]
                + ' ' + 'f23' + ' ' + textTag[-1][1]
                )
    file1.write('\n')

file1.close()

'''

'''