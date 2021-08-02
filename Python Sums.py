#Suhas Gondi
#Sums Image Data
#TESTING TO GET AVERAGE STUFF TO WORK

import glob
import csv
import os


for filename in glob.glob('*.txt'):
    reader = open(filename,'rb')
    fs = []
    ls = []
    for row in reader:
        print(row)
        row = row.split()
        if row == []:
            continue
        try:
            float(row[0])
            row = map(float,row)
           # if row[1] < 5 or row[10] < 50: this is an example of a condition that can be set to eliminate data
            #    continue
            ls.append(row) 
        except ValueError:
            lm = list(zip(*ls))
            lp = []
            for i in range(len(lm)):
                if i==6: #average branch length column
                    lp.append(lm[i][lm[1].index(max(lm[1]))]) #appends average branch length value in row with highest number of branches
                else:
                    lp.append(sum(lm[i]))
            fs.append(lp)
            ls = []
    if ls !=[]:
        lm = list(zip(*ls))
        lp = []
        for i in range(len(lm)):
                if i==6: #average branch length column
                    lp.append(lm[i][lm[1].index(max(lm[1]))]) #appends average branch length value in row with highest number of branches
                else:
                    lp.append(sum(lm[i]))
        fs.append(lp)
    writer = csv.writer(open("Out"+filename+".txt",'w'), delimiter='\t')
    writer.writerow([' ', '#Branches','# Junctions','# End-point voxels','# Junction voxels','# Slab voxels','Average Branch Length','# Triple points','# Quadruple points','Maximum Branch Length','Longest Shortest Path','spx','spy','spz'])
    for row in fs:
        writer.writerow(row)

