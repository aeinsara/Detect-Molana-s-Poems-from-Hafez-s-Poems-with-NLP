# -*- coding: utf-8 -*-
import urllib2
import re
'''
#........................................* hafez *........................................

file = open("hafez.txt",'w')
file.close()
for i in range(1,100):
    j = str(i)
    url = 'https://ganjoor.net/hafez/ghazal/sh'+j
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()

    r1 = re.findall('<div class="m1"><p>(.*?)</p>',the_page)
    r2 = re.findall('<div class="m2"><p>(.*?)</p>', the_page)

    file = open("hafez.txt",'a')

    for text in r1:
        text = re.sub('<BR>','\n',text)
        text = re.sub(' ', '\n', text)
        file.write(text)
        file.write("\n")

    for text in r2:
        text = re.sub('<BR>','\n',text)
        text = re.sub(' ', '\n', text)
        file.write(text)
        file.write("\n")

file.close()

#....................................* hafez normalize*....................................

file = open("hafez.txt",'r')
lines = file.readlines()

file.close()

f = open("hafezNorm.txt","w")

for line in lines:
    if line!="که"+"\n" and line!="در"+"\n" \
            and line!="به"+"\n" and line!="برای"+"\n" \
            and line!="از"+"\n" and line!="را"+"\n" \
            and line!="و"+"\n" and line!="ز"+"\n" \
            and line!="تا"+"\n"and line!="یا"+"\n" \
            and line!="با"+"\n" and line!="بر"+"\n":
        f.write(line)

f.close()

'''
#..........................* count of hafez*..........................

file1=open("hafezNorm.txt","r+")
frequency = {}

file2 = open("hafezCount.txt",'w')
file2.close()

file2 = open("hafezCount.txt",'a')

for word in file1.read().split():
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    file2.write(str(frequency[words]))
    file2.write('\t')
    file2.write(words)
    file2.write("\n")

file1.close()
file2.close()


'''
#........................................* molana *........................................
file = open("molana.txt",'w')
file.close()
for i in range(1,100):
    j = str(i)
    url = 'https://ganjoor.net/moulavi/shams/ghazalsh/sh'+j
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()

    r1 = re.findall('<div class="m1"><p>(.*?)</p>',the_page)
    r2 = re.findall('<div class="m2"><p>(.*?)</p>', the_page)

    file = open("molana.txt",'a')

    for text in r1:
        text = re.sub('<BR>','\n',text)
        text = re.sub(' ', '\n', text)
        file.write(text)
        file.write("\n")
    for text in r2:
        text = re.sub('<BR>','\n',text)
        text = re.sub(' ', '\n', text)
        file.write(text)
        file.write("\n")

#....................................* molana normalize*....................................
file = open("molana.txt",'r')
lines = file.readlines()

file.close()

f = open("molanaNorm.txt","w")

for line in lines:
    if line!="که"+"\n" and line!="در"+"\n" \
            and line!="به"+"\n" and line!="برای"+"\n" \
            and line!="از"+"\n" and line!="را"+"\n" \
            and line!="و"+"\n" and line!="ز"+"\n" \
            and line!="تا"+"\n" and line!="یا"+"\n" \
            and line!="با"+"\n" and line!="بر"+"\n":
        f.write(line)

f.close()
'''
#..........................* count of molana*..........................
file1=open("molanaNorm.txt","r+")
frequency = {}

file2 = open("molanaCount.txt",'w')
file2.close()

file2 = open("molanaCount.txt",'a')

for word in file1.read().split():
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    file2.write(str(frequency[words]))
    file2.write('\t')
    file2.write(words)
    file2.write("\n")

file1.close()
file2.close()
