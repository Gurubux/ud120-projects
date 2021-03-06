# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:58:41 2019

@author: Guru
"""

#!/usr/bin/env python
"""
convert dos linefeeds (crlf) to unix (lf)
usage: dos2unix.py 
"""
original = "../outliers/practice_outliers_ages.pkl"
destination = "../outliers/practice_outliers_ages_unix.pkl"

content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))

print("Done. Saved %s bytes." % (len(content)-outsize))