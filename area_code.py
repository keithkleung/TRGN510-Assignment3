#!/usr/bin/python

import sys
import re
import fileinput

acode= sys.argv[1]
for each_phone_number in fileinput.input(acode):
    area = re.sub(r'\D', '', each_phone_number)
    area = area[0:3]
    print(area)   
