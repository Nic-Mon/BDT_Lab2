#!/usr/bin/env python
import sys

cur_word = None
cur_count = 0
for line in sys.stdin:
    key, value = line.split()
    # tally counts from current key
    if key == cur_word: 
        cur_count += int(value)
    # OR emit current total and start a new tally 
    else: 
        if cur_word:
            print '%s\t%s' % (cur_word, cur_count)
        cur_word, cur_count  = key, int(value)
# don't forget the last record! 
print '%s\t%s' % (cur_word, cur_count)
