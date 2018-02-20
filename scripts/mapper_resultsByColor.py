#!/usr/bin/env python
"""
<write your description here>
INPUT:
    <specify record format here>
OUTPUT:
    <specify record format here>
"""
import re
import sys
# read from standard input
for line in sys.stdin:
    line = line.strip()
    # tokenize
    results = re.findall(r'(?<=Result )([^\n\r\]]*)', line)
    # check the kind of result it is and emit the resulting (k,v) pair
    for result in results:
        if result == '"1-0"':
            print '%s\t%s' % ("white", 1)
        elif result == '"0-1"':
            print '%s\t%s' % ("black", 1)
        elif result == '"1/2-1/2"':
            print '%s\t%s' % ("draw", 1)
        else:
            print '%s\t%s' % ("ongoing", 1)
