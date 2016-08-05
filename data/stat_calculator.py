'''
Author:Mir Sahib
Description: Statistical analysis on the csv file
'''

import csv
file_demo = open('file1.csv')
reader = csv.reader(file_demo)

homeWin=0
awayWin=0
draw=0
for line in reader:
	if line[6]=='H':
		homeWin=homeWin+1
	elif line[6]=='A':
		awayWin=awayWin+1
	else:
		draw=draw+1

#print 'Home win = '+str(homeWin)+' Away win = '+str(awayWin)+' Draw = '+str(draw)

print('Output from file1')
with open('demo/file.csv','w') as mycsvfile:
	thedata = csv.writer(mycsvfile)
	thedata.writerow([homeWin,awayWin,draw])
mycsvfile.close()
