# After Python 3.6, order of insertion is preserved
dic = {1: 'first', 2: 'second', 3: 'third'}
# This will insert the 0 key at the end
dic[0] = 'fourth'
print(dic)
# This will NOT insert the key at the end because 1 exists
dic[1] = 'new first'
print(dic)
# Also, this does not return the first element of the dic
# because it was inserted at the end
dic[0]
