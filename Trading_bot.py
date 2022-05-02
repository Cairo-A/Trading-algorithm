#Created by Angel Cairo
#CSCI-135 Group Project Final
#Date: 5-02-22
#Trading bot

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
#no . of stocks
    n_stock = capital / min_p
  
  return n_stock*max_prof_val

#customer info
Name = input("Please enter customer's name: ")
Email = input("Please enter customer's email: ")
Phone = input("Please enter customer's phone number: ")
capital = int(input("How much would the customer like to start with?: "))
#potential profit
#This example utilizes Alphabet Inc. last 10 days' closing prices. (4/18/22-4/29/22)
print('Name:' ,Name, 'Email:' ,Email, 'Phone #:' ,Phone, 'Profit:' ,stock_market(capital,[2299.33, 2388.23, 2300.41, 2390.12, 2465.00, 2392.28, 2498.75, 2564.91, 2610.62, 2559.22]))
#final balance
print('Final Balance:', capital+stock_market(capital,[2299.33, 2388.23, 2300.41, 2390.12, 2465.00, 2392.28, 2498.75, 2564.91, 2610.62, 2559.22]))


#Citations will be added to the final documents
