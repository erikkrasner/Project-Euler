#!/usr/bin/env python
# 21124
# 0.06 s

from itertools import imap

word_length_memo = {1:len('one'),
                    2:len('two'),
                    3:len('three'),
                    4:len('four'),
                    5:len('five'),
                    6:len('six'),
                    7:len('seven'),
                    8:len('eight'),
                    9:len('nine'),
                    10:len('ten'),
                    11:len('eleven'),
                    12:len('twelve'),
                    13:len('thirteen'),
                    14:len('fourteen'),
                    15:len('fifteen'),
                    16:len('sixteen'),
                    17:len('seventeen'),
                    18:len('eighteen'),
                    19:len('nineteen'),
                    20:len('twenty'),
                    30:len('thirty'),
                    40:len('forty'),
                    50:len('fifty'),
                    60:len('sixty'),
                    70:len('seventy'),
                    80:len('eighty'),
                    90:len('ninety'),
                    1000:len('onethousand')}

def word_length(num):
    if num in word_length_memo:
	return word_length_memo[num]
    if num >= 100:
	if not num % 100:
	    return word_length(num / 100) + len('hundred')
	return word_length(num / 100) + len('hundredand') + word_length(num % 100)
    return word_length(10 * (num / 10)) + word_length(num % 10)

print sum(imap(word_length,xrange(1,1001)))
