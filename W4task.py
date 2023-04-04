# You have a few stocks in `watch_list` that you constantly
# monitor for interesting market activity
watch_list = ['QAN.AX', 'CBA.AX', 'BHP.AX']

# The market opens and you notice that the following stocks in
# `active_list` have displayed unusual market activity
active_list = ['CBA.AX', 'BHP.AX', 'NAB.AX', 'WBC.AX', 'RIO.AX']

# You want to buy the stocks that have unusual market activity that
# are also in your `watch_list`

# TASK 1A:
# Use a for loop to create a list called `buy_stocks_list` that contain stocks
# that are in present in both `watch_list` and `active_list`
# len()函数返回一个对象中的项目数。当对象是一个字符串时，len()函数返回该字符串中的字符数。
buy_stocks_list = []
#
for i in range(len(watch_list)):
    for j in range(len(active_list)):
        if watch_list[i] == active_list[j]:
            buy_stocks_list.append(watch_list[i])
print(buy_stocks_list)

# for loop (just 1)
for stock in watch_list:
    if stock in active_list:
        buy_stocks_list.append(stock)
print(buy_stocks_list)



# TASK 1B:
# Use a list comprehension to create a list called `buy_stocks_list` that contain stocks
# that are in present in both `watch_list` and `active_list`
buy_stocks_list = [i for i in watch_list if i in active_list ]
print(buy_stocks_list)

# buy_stocks_list = ???


# After identifying the stocks that you want to buy, you have to decide
# how many shares of each stock to buy. Based on your research, you think that
# the following formula is the best way of determining how many shares to buy:
# # 在确定你想买的股票后，你必须决定
# # 购买每只股票的多少股。根据你的研究，你认为
# # 以下公式是确定购买多少股的最佳方法：
# Buy 17 + 1 + 14 = 32 shares of QAN.AX because
# Q is the 17th letter in the alphabet
# A is the 1st letter in the alphabet
# N is the 14th letter in the alphabet



# TASK 2:
# Write a function called `buy_how_many` that takes in a ticker (e.g. 'QAN.AX')
# and returns the number of shares to buy
# HINT: 'abc'.index('c') returns 2, the index of the letter 'c' in the string 'abc' 'abc'.index('c')返回2，即字母'c'在字符串'abc'中的索引。
# HINT: You can loop through characters in a string like looping through a list 你可以像循环浏览列表一样循环浏览字符串中的字符

# Example1:
# x = 'abc'
# for i in x:
#     print(i)

# Example2:
# alpha = '1234567H'
# print(alpha.index("H"))
# (return 7)


def buy_how_many(ticker):
    tic_base = ticker.upper().split('.')[0]
    number = 0
    for i in tic_base:
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number += alpha.index(i) + 1
    return number

print(buy_how_many("QaN.AX"))


print('Task 2:')
for stock in buy_stocks_list:
    print(f'Buy {buy_how_many(stock)} shares of {stock}')
print()





# TASK 3A:
# Use a for loop to create a dictionary called `buy_stock_dict`
# that contains the stocks in `buy_stocks_list` as its keys
# and the number of shares we should buy for each stock as its values

# buy_stock_dict = ???


# TASK 3B:
# Use a dictionary comprehension to create a dictionary called `buy_stock_dict`
# that contains the stocks in `buy_stocks_list` as its keys
# and the number of shares we should buy for each stock as its values
# 使用字典理解法创建一个名为`buy_stock_dict`的字典，其中包含`buy_stocks_list`中的股票作为键。
# 包含在`buy_stocks_list`中的股票作为其键值
# 以每只股票的购买数量作为其值

# x = {i:j for i,j in enumerate(list(range(3)))}
# print(x)

# x = {i:j for i,j in enumerate(list('abc'))}
# print(x)

buy_stock_dict = {}
for stock in buy_stocks_list:
    buy_stock_dict[stock] = buy_how_many(stock)
print(buy_stock_dict)


buy_stock_dict = {stock:buy_how_many(stock) for stock in buy_stocks_list}
print(buy_stock_dict)


# Bonus: Hackerrank question
# https://www.hackerrank.com/challenges/diagonal-difference/problem