#Created by Angel Cairo
#CSCI-135 Group Project Final
#Date: 5-02-22
#Trading bot
#This is the current version implemented as of 5/2/22
def stock_market(capital,stock_price):
  max_prof_val, curr_max_val = 0, 0
  for price in reversed(stock_price):
#maximum current value of the stock
    curr_max_val = max(curr_max_val, price)
#potential profit
    pot_profit = curr_max_val - price
#maximum profit
    max_prof_val = max(pot_profit, max_prof_val)
  
    min_p = min(stock_price)
#number of stocks
    n_stock = capital / min_p
  
  return n_stock*max_prof_val

#customer info
Name = input("Please enter customer's name: ")
Email = input("Please enter customer's email: ")
Phone = input("Please enter customer's phone number: ")
capital = int(input("How much money would the customer like to invest with?: "))
#potential profit
#This example utilizes the regular prices of all stocks pulled from Webscraper except Nasdaq. (5/02/22)
# For future updates, I would implement the ability to let the user change the numbers in the list. For now, the link in the final documentation should give you the ability to edit that part if you want to change the numbers
print('Name:' ,Name, 'Email:' ,Email, 'Phone #:' ,Phone, 'Profit:' , stock_market(capital, [2343.14, 2490, 48.71, 381.23, 178.64, 19.06, 10.48, 902.94, 49.14, 46.23, 211.53, 40.96]))
#final balance
print('Final Balance:', capital+stock_market(capital,[2343.14, 2490, 48.71, 381.23, 178.64, 19.06, 10.48, 902.94, 49.14, 46.23, 211.53, 40.96]))
