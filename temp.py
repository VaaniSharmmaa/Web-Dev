#Hash Map data structure
#_map = {'a':2, 'b': 3 ,'c':5}

#if 'a' in _map:
    #print('yes present')
#else:
    #print('lol')
#for k,v in _map.items():
    #print(k,v)

from collections import Counter

_str = "aaabnmcdfg"
m = Counter(_str)
print(m)
_map = {'a':2, 'b': 3, 'c':5}

for k,v in _map.items():
    print(k,v)