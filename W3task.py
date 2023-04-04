# Use the following data for Questions 1 - 3

stk_data = [
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.5,
        'volume': 1000,
        'ownerName': 'John',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.75,
        'volume': 1200,
        'ownerName': 'Micheal',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.4,
        'volume': 150,
        'ownerName': 'Lucy',
     },
]

# Question 1
# Write a simple for-loop to determine the total value traded
# i.e. the sum of price * volume across all dicts in stk_data
value = 0

for i in stk_data:
    value += i['price'] * i['volume']
print(f'The value traded is ${value}')

# Question 2
# We are only interested in finding out whether the total value traded is more than $1000
# In reality, we might be working with a list that contains hundreds or even thousands of items
# Iterating all items in such a list might take a long time
#
# Write a for-loop that contains a break statement that can
# efficiently tell us whether the value traded is more than $1000
# 我们只想知道交易的总价值是否超过了1000美元
# 在现实中，我们可能要处理一个包含数百个甚至数千个项目的列表
# 迭代这样一个列表中的所有项目可能需要很长的时间

# 编写一个包含break语句的for-loop，它可以
# 有效地告诉我们所交易的价值是否超过了1000美元


my_sum = 0
for i in stk_data:
    my sum += i['price'] * i['volume']
    if my_sum > 1000:
        break


# Question 3
# We are only interested in insider trades that are large enough
# E.g. We are not interested in Lucy's trade because
# we consider the value traded = $5.4 * 150 = $810 to be too small
# We only want to consider trades that are >= $1000
# Write a for-loop that sums up the value for trades that are >= $1000
# 我们只对足够大的内幕交易感兴趣
# 例如，我们对露西的交易不感兴趣，因为
# 我们认为交易的价值=5.4美元*150=810美元，太小了
# 我们只想考虑>=1000美元的交易
# 写一个for-loop，对>=1000美元的交易进行加总

insider_values = {}

for i in stk_data1:
    ticker = i['ticker']

    if ticker not in insider_values:
        insider_values[ticker] = 0

    insider_values[ticker] += i['price'] * i['volume']
print(insider_values)


# Question 4
stk_data1 = [
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.5,
        'volume': 1000,
        'ownerName': 'John',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.75,
        'volume': 1200,
        'ownerName': 'Micheal',
     },
    {
        'ticker': 'AAPL',
        'date': '2022-09-30',
        'price': 5.4,
        'volume': 150,
        'ownerName': 'Lucy',
     },
    {
        'ticker': 'AMZN',
        'date': '2022-09-30',
        'price': 11,
        'volume': 950,
        'ownerName': 'John',
     },
    {
        'ticker': 'AMZN',
        'date': '2022-09-30',
        'price': 11.2,
        'volume': 650,
        'ownerName': 'Micheal',
     },
    {
        'ticker': 'IBM',
        'date': '2022-09-30',
        'price': 6,
        'volume': 300,
        'ownerName': 'John',
     },
    {
        'ticker': 'IBM',
        'date': '2022-09-30',
        'price': 6.4,
        'volume': 1100,
        'ownerName': 'Micheal',
     },
]

# Given stk_data1 above, we want to create a dictionary of the form
# {'aapl': xxxx, 'amzn': xxxx, 'ibm': xxxx}, where xxxx is the amount traded for each stock
#
# Achieve this using a single for-loop that iterates over stk_data1

result = {}

for i in stk_data1:

    ticker = i['ticker']
    my_sum = i['price'] * i['volume']

    if ticker not in result.keys():
        result[ticker] = 0

    result[ticker] += my_sum

print(result)
