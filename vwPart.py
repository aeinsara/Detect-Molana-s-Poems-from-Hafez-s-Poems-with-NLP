# -*- coding: utf-8 -*-
'''
hafezFile = open("hafez.txt", 'r', encoding="utf8")
molanaFile = open("molana.txt", 'r', encoding="utf8")

vwFile = open("vwFile.txt", 'w', encoding="utf8")

turnHafez = 0
turnMolana = 0

for hafezLine in hafezFile:
    if hafezLine != '\n' :
        turnHafez = turnHafez + 1

        if turnHafez == 1:
            vwFile.write("1 | %s\t" % hafezLine.split("\n")[0])
        elif turnHafez < 3 :
            vwFile.write("\t%s" % hafezLine.split("\n")[0])
        else :
            vwFile.write("\n")
            turnHafez = 0;

            for molanaLine in molanaFile:
                 if molanaLine != '\n' :
                     turnMolana = turnMolana + 1

                     if turnMolana == 1 :
                         vwFile.write("2 | %s\t" % molanaLine.split("\n")[0])
                     elif turnMolana < 3:
                         vwFile.write("\t%s" % hafezLine.split("\n")[0])
                     else:
                         vwFile.write("\n")
                         turnMolana = 0
                         break

# -*- coding: utf-8 -*-

hafezFile = open("hafez.txt", 'r', encoding="utf8")
molanaFile = open("molana.txt", 'r', encoding="utf8")

vwFile = open("vwFile.txt", 'w', encoding="utf8")
#hafezLine = hafezFile.read().split("\n")


for hafezLine, molanaLine in zip(hafezFile, molanaFile):
    if hafezLine != '\n' :
        vwFile.write("1 | %s" % hafezLine.split("\n")[0])
        vwFile.write("\n")
    if molanaLine != '\n' :
        vwFile.write("-1 | %s" % molanaLine.split("\n")[0])
        vwFile.write("\n")
'''

tp = 0
tn = 0
fp = 0
fn = 0

predictFile = open("predictions.txt", 'r', encoding="utf8")
testFile = open("testVW.txt", 'r', encoding="utf8")

for testLine, predictLine, in zip (testFile, predictFile):
    print("pre : " , float(predictLine.split("\n")[0]),"test : ", testLine.split(" ")[0])
    if float(testLine.split(" ")[0]) == 1 :
        if float(predictLine.split("\n")[0]) > 0.0 :
            tp += 1 #tp
        else:
            fp += 1 #fp
    else:
        if float(predictLine.split("\n")[0]) > 0.0 :
            fn += 1    #fn
        else:
            tn += 1 #tn


print('tp : ', tp, '\ttn :', tn, '\tfp : ', fp, 'fn : ', fn)

precision = float(tp) / (tp + fp)
recall = float(tp) / (tp + fn)

print ('precision : ', precision)
print('recall : ', recall)
