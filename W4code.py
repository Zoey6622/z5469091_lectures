# Some data (list of tuples)
data = [
  ('a', 1),
  ('b', 2),
  ('c', 3),
  ]

# Create a dict comprehension
dic = {k:v for k, v in data}
print(f'`dic` is {dic}')
print(f'type(dic) is: {type(dic)}')

# Create a list comprehension
lst = [(k, v) for k, v in data]
print(f'`lst` is {lst}')
print(f'type(lst) is {type(lst)}')

# Create a set comprehension
st = {k for k, v in data}
print(f'`st` is {st}')
print(f'type(st) is {type(st)}')

evens = []
for x in range(1_000_000 + 1):
    if x % 2 == 0:
        evens.append(x)
print(evens[:10])

evens = [x for x in range(1_000_000 + 1)if x % 2 == 0]
print(evens[:10])


dic = {'a': 1, 'b': 2, 'c': 3}
 # Create a list of (key, val) tuples called `pairs`
pairs = []
for key, value in dic.items():
    pairs.append((key,value))
print(pairs)

dic = {'a': 1, 'b': 2, 'c': 3}
# Create a list of (key, val) using list comprehensions:
pairs = [(key,value) for key,value in dic.items()]
print(pairs)

dic = {'a': 1, 'b': 2, 'c': 3}
 # Create a set comprehension with the keys from `dic`
keys = {key for key in dic}
print(f'The type of {keys} is {type(keys)}')

evens = []
for x in range(1_000_000 + 1):
    if x % 2 == 0:
        evens.append(x)
print(evens[:10])

evens = [x for x in range(1_000_000 + 1) if x % 2 == 0]
print(evens[:10])


data = [
    ('a', 1),
    ('b', 2),
    ('c', 3), ]
st = {k for k, v in data}
print(f'`st` is {st}')
print(f'type(st) is {type(st)}')

lst = [(k, v) for k, v in data]
print(f'`lst` is {lst}')
print(f'type(lst) is {type(lst)}')

dic = {k:v for k, v in data}
print(f'`dic` is {dic}')
print(f'type(dic) is: {type(dic)}')

data = [
    ('a', 1),
    ('b', 2),
    ('c', 3), ]
 # Is this a tuple comprehension?
not_a_tup = (k for k, v in data)
print(f'The type of `(k for k, v in data)` is {type(not_a_tup)}')

lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
new_lst = [x**2 for x in lst if x**2>150]
print(f'the new list with value of square greater than 150 is {new_lst}')

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
# Approach 2:
# - Use a list comprehension that loops over a set of the original list
result = [i for i in set(numbers) if i % 2 == 0]
result.sort()
print(result)

