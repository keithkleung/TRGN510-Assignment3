#!/usr/bin/python

import sys
import json
import fileinput
import csv

genome_data = sys.argv[1]
results=[]
for each_line_of_text in fileinput.input(genome_data):
    if each_line_of_text.startswith('#'):
        continue
    line=each_line_of_text.split("\t")

    if line[2] == 'gene':
        s = next(csv.reader([line[8]], delimiter=' '))
        data = {}
        data["geneName"] = (s[3]).rstrip(";")
        data["chr"] = line[0]
        data["startPos"] = int(line[3])
        data["endPos"] = int(line[4])
        results.append(data)

data_json = json.dumps(results, indent=2)
print(data_json)
