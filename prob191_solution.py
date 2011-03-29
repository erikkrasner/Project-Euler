#!/usr/bin/env python
# 1918080160
# 0.09s
import sys

def num_prize_strings(num_days):
    o,a,aa,l,la,laa = 1,1,0,1,0,0
    for day in range(1,num_days):
	    oldo,olda,oldaa,oldl,oldla,oldlaa = o,a,aa,l,la,laa
	    o = oldo + olda + oldaa
	    a,aa,la,laa = oldo,olda,oldl,oldla
	    l = oldo + olda + oldaa + oldl + oldla + oldlaa
    return o + a + aa + l + la + laa

if __name__ == '__main__':
    print num_prize_strings(int(sys.argv[1]) if sys.argv[1:] else 30)
