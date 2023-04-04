lst1 = ['a']
print(f'This is lst1: {lst1}')

lst2 = ['b', lst1]
print(f'This is lst2: {lst2}')

lst2[1].append('c')


happy = True
if happy is True:
    print("I am happy")

print("This will print regardless of the value of happy")


happy = True
very_happy = True

if happy is True:
    print("I am happy")                         # <-- four-spaces indentation
    if very_happy is True:                      # <-- four-spaces indentation
        print("Actually, I'm really happy!")

happy = 5
if happy is True:
    print("I am happy")

print(1 == True)



var1 = 'a'
var2 = 'a'
var3 = ['a']
var4 = ['a']

print(var1 == var2)
print(var1 is var2)

print(var3 == var4)
print(var3 is var4)

a = 0
b = True
if a != 0:
   print("a is non-zero")
elif b is True:
   print("b is True")
elif a < 0 and b is True:
   print("a is negative and b is True")
else:
   print("None of the conditions above hold")


name = type(input("Who are you?"))
print("Welcome to the class", name)




hours = input('Enter number of hours you worked this week:')
hours = int(hours)
normal_rate = 51.45
overload_rate = 88.9

if hours > 35:
    pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
else:
    pay = hours * normal_rate

print(f"This weekly payment is: {pay}")

for even in range(0, 18, 2):
    if even > 2:
        continue
print(even)



lst1 = ['a']
lst2 = ['b', lst1]
lst3 = ['b', ['a']]

lst1 = ['a']
print(f'This is lst1: {lst1}')
lst3 = ['b', ['a']]
print(f'This is lst3: {lst3}')
lst3[1].append('c')
print(f"This is lst3 after appending 'c': {lst3}")  ###This is lst3 after appending 'c': ['b', ['a', 'c']]
print(f"This is lst1 after modifying lst3: {lst1}")  ###This is lst1 after modifying lst3: ['a']



happy = False
if happy is True:
     print("I am happy")
print("This will print regardless of the value of happy")

happy = True
if happy is True:
    print("I am happy")
print("This will print regardless of the value of happy")

happy = True
very_happy = True
if happy is True:
    print("I am happy")
    if very_happy is True:
         print("Actually, I'm really happy!")

happy = 5
if happy:
     print("I am happy")


if 5:
    print('5 is Truthy')
if 'a':
    print('A non-empty string is Truthy')
if [1, 2, 3]:
    print('Non-empty containers are Truthy')

if not 0.0:
    print('0 numerical values are Falsy')
if not None:
    print('None is Falsy')
if not '':
    print('Empty strings are Falsy')
if not []:
    print('Empty containers are Falsy')


b = False
if b is True:
    print("b is True")
else:
    print("b is not True")


a=0
b = True
if a != 0:
    print("a is non-zero")
elif b is True:
    print("b is True")
elif a < 0 and b is True:
    print("a is negative and b is True")
else:
    print("None of the conditions above hold")


a = -1
b = True
if a != 0:
    print("a is non-zero")
elif b is True:
    print("b is True")
elif a < 0 and b is True:
    print("a is negative and b is True")
else:
    print("None of the conditions above hold")

happy = True
if happy is True:
    pass

if x > 0 and y is True:
    pass
elif x <= 0 and y is True:
    pass
else:
    pass

name = input('Who are you?')
print(type(name))
print('Welcome to the class', name)

hours = input('Enter number of hours you worked this week: ')
normal_rate = 51.45
overload_rate = 88.9

if hours > 35 :
    pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
else :
    pay = hours * normal_rate
print(f'This weekly payment is: {pay}')

import yfinance
# Set the dates parameters start = '2020-01-01'
end = None
 # Download Qantas stock prices
tic = "QAN.AX"
df = yfinance.download(tic, start, end, ignore_tz=True)
print(df)
df.to_csv('qan_stk_prc.csv')
 # Download Wesfarmers stock prices
tic = "WES.AX"
df = yfinance.download(tic, start, end, ignore_tz=True)
print(df)
df.to_csv('wes_stk_prc.csv')

letters_lst = ["a", "b", "c", "d"]
print(letters_lst[0])
print(letters_lst[1])
print(letters_lst[2])
print(letters_lst[3])

letters_lst = ["a", "b", "c", "d"]
for letter in letters_lst:
    print(letter)

import yfinance start = '2020-01-01'
end = None

tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
    df = yfinance.download(tic, start, end, ignore_tz=True)
    tic_base = tic.lower().split('.')[0]
    df.to_csv(f'{tic_base}_stk_prc.csv')

tic = 'QAN.AX'
tic_base = tic.lower().split('.')[0]
print(tic_base)

tickers = set()
tickers.add("QAN.AX")
tickers.add("QAN.AX")
tickers.add("WES.AX")
for tic in tickers:
    print(tic)


d={
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
}
for key in d:
    print(key)

d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
}
for val in d.values():
    print(val)

d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
}
for key_value_tuple in d.items():
    print(f"key_value_tuple is {key_value_tuple}")  # Unpacking
    key, value = key_value_tuple
    print(f"KEY: {key} VALUE: {value}")

d={
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
}
for key, value in d.items():
    print(f'KEY: {key} VALUE: {value}')

for i in range(0, 5):
    print(f"i is now {i}")

for i in range(0, 5, 1):
    print(f"i is now {i}")

for i in range(5):
    print(f"i is now {i}")

for even in range(0, 10, 2):
    print(f"even is now {even}")

for i in range(5,0):
    print("This will not execute because start is greater than stop.")
for i in range(5,0,-1):
    print("This message will self-destruct in {} secs...".format(i))

letters = ["a", "b", "c", "d", "e"]
 # i is a counter variable
i=0
for x in letters:
     print(f"letters[{i}] --> {x}")
     i += 1 # Shortcut for i = i + 1

letters = ["a", "b", "c", "d", "e"]
for tup in enumerate(letters):
    print(tup)

letters = ["a", "b", "c", "d", "e"]
for i, x in enumerate(letters):
    print(f"letters[{i}] --> {x}")

d={
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
}
for i, tup in enumerate(d.items()):
    print(f'Iteration {i} gives {tup}')

numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
temp_largest = numbers[0]
print('Before', temp_largest)
for number in numbers:
    if number > temp_largest:
        temp_largest = number
    print(number, temp_largest)
print(f'The largest value is {temp_largest}')

the_sum = 0
for i in range(1, 101):
    the_sum = the_sum + i
print(the_sum)


the_sum = 0
i=1
while i <= 100:
    the_sum = the_sum + i
    i=i+1
print(the_sum)

x = 0.1
while x != 1.1:
    x += 0.1
print(x)

for outer_variable in outer_iteratable:
    statement_a
    statement_b
    for inner_variable in inner_iteratable:
        statement_c
        statement_d
        statement_e
    statement_f
    statement_g

years = [2018, 2019, 2020]
months = [
     "Jan",
     "Feb",
     "Mar",
     "Apr",
     "May",
     "Jun",
     "Jul",
     "Aug",
     "Sep",
     "Oct",
     "Nov",
     "Dec",
     ]
for year in years:
    for month in months:
        print("Year: {}, Month: {}".format(year, month))

for i in range(1, 4):
    for j in range(1, 4):
        if i <= j:
            print(i, j)


