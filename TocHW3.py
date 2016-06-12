# -*- coding: utf-8 -*-
import sys
import re
import operator

commandline = sys.argv[1].split(',')

path = sys.argv[2]

pairs = []
for pair in commandline:
	pairs.append(pair)

pattens = []
for pair in pairs:
	pairtemp = pair.split('#')
	pattens.append('.*' + pairtemp[0] + '.*' + pairtemp[1] + '.*')
	pattens.append('.*' + pairtemp[1] + '.*' + pairtemp[0] + '.*')

dataset = file(path, 'r')

numbers = {}

for i in range(0, len(pairs)):
	insert_hash = {pairs[i]:0}
	numbers.update(insert_hash)

for line in dataset:
	for pth in range(0, len(pattens)):
		match = re.match(pattens[pth], line)
		if match:
			numbers[pairs[pth/2]] += 1;

sorted_hash = sorted(numbers.items(), key=operator.itemgetter(1), reverse=True)

for i in range(0, len(sorted_hash)):
	sys.stdout.write(sorted_hash[i][0] + ',' + str(sorted_hash[i][1]) + '\n')

dataset.close()
