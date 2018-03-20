from __future__ import unicode_literals
from norm import *

#.................................hafez normal............................
normalizer = Normalizer()
myfile = open('hafez.txt', 'r')

file = open("hafezNorm.txt",'w')
file.close()

data=myfile.read()

textNorm = normalizer.normalize(data)
#textNorm = data #---------------------------alaki

file = open("hafezNorm.txt",'a')

file.write(textNorm)

file.close()

#.................................molana normal............................
#normalizer = Normalizer()
myfile = open('molana.txt', 'r')

file = open("molanaNorm.txt",'w')
file.close()

data=myfile.read()

textNorm = normalizer.normalize(data)
#textNorm = data #---------------------------alaki

file = open("molanaNorm.txt",'a')

file.write(textNorm)

file.close()