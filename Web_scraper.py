#Created by Angel Cairo
#CSCI-135 Group Project Final
#Date: 5-02-22
#Web Scraper
#importing yahoo finance
import yfinance as yf
loop = False
# random stocks that can be picked.
Alphabet = yf.Ticker("GOOG")
Amazon = yf.Ticker("AMZN")
Citigroup = yf.Ticker("C")
Deere = yf.Ticker("DE")
Johnson = yf.Ticker("JNJ")
Lucid = yf.Ticker("LCID")
Nasdaq = yf.Ticker("IXIC")
Robinhood = yf.Ticker("HOOD")
Tesla = yf.Ticker("TSLA")
Twitter = yf.Ticker("TWTR")
Verizon = yf.Ticker("VZ")
Visa = yf.Ticker("V")
Zillow = yf.Ticker("Z")

#while loop to indicate how mauch info you would like
while loop == False:
  stock_Wanted = input("Which stock would you like to see? ")
  #Alphabet stock
  if stock_Wanted == 'Alphabet':
    info_length = input("Do you want short info or long? ")
    if info_length == 'short':
      print('Day High:' , Alphabet.info['dayHigh'], 'Regular Market Price:' , Alphabet.info['regularMarketPrice'])
      print("The last ten days' closing is as follows: [2299.33, 2388.23, 2300.41, 2390.12, 2465.00, 2392.28, 2498.75, 2564.91, 2610.62, 2559.22]")
      loop == True
      break
    elif info_length == 'long':
      print(Alphabet.info)
      loop == True
      break
    else:
      print("Please type either 'short' or 'long'.")
  #Amazon stock
  elif stock_Wanted == 'Amazon':
    info_length = input("Do you want short info or long? ")
    if info_length == 'short':
      print('Day High:' , Amazon.info['dayHigh'], 'Regular Market Price:' , Amazon.info['regularMarketPrice'])
      print("The last ten days' closing is as follows: [2299.33, 2388.23, 2300.41, 2390.12, 2465.00, 2392.28, 2498.75, 2564.91, 2610.62, 2559.22]")
      loop == True
      break
    elif info_length == 'long':
      print(Amazon.info)
      loop == True
      break
    else:
      print("Please type either 'short' or 'long'.")
  #Citigroup stock
  elif stock_Wanted == 'Citigroup':
    info_length = input("Do you want short info or long? ")
    if info_length == 'short':
      print('Day High:' , Citigroup.info['dayHigh'], 'Regular Market Price:' , Citigroup.info['regularMarketPrice'])
      loop == True
      break
    elif info_length == 'long':
      print(Citigroup.info)
      loop == True
      break
    else:
      print("Please type either 'short' or 'long'.")
  #Deere stock
  elif stock_Wanted == 'Deere':
    info_length = input("Do you want short info or long? ")
    if info_length == 'short':
      print('Day High:' , Deere.info['dayHigh'], 'Regular Market Price:' , Deere.info['regularMarketPrice'])
      loop == True
      break
    elif info_length == 'long':
      print(Deere.info)
      loop == True
      break
    else:
      print("Please type either 'short' or 'long'.")
  #Johnson stock
  elif stock_Wanted == 'Johnson':
    info_length = input("Do you want short info or long? ")
    if info_length == 'short':
      print('Day High:' , Johnson.info['dayHigh'], 'Regular Market Price:' , Johnson.info['regularMarketPrice'])
      loop == True
      break
    elif info_length == 'long':
      print(Johnson.info)
      loop == True
      break
    else:
      print("Please type either 'short' or 'long'.")
  #Lucid stock
  elif stock_Wanted == 'Lucid':
    info_length = input("Do you want short info or long? ")
    if info_length == 'short':
      print('Day High:' , Lucid.info['dayHigh'], 'Regular Market Price:' , Lucid.info['regularMarketPrice'])
      loop == True
      break
    elif info_length == 'long':
      print(Lucid.info)
      loop == True
      break
    else:
      print("Please type either 'short' or 'long'.")
  #Nasdaq stock
  elif stock_Wanted == 'Nasdaq':
    info_length = input("Do you want short info or long? ")
    if info_length == 'short':
      print('Day High:' , Nasdaq.info['dayHigh'], 'Regular Market Price:' , Nasdaq.info['regularMarketPrice'])
      loop == True
      break
    elif info_length == 'long':
      print(Nasdaq.info)
      loop == True
      break
    else:
      print("Please type either 'short' or 'long'.")
  #Robinhood stock
  elif stock_Wanted == 'Robinhood':
    info_length = input("Do you want short info or long? ")
    if info_length == 'short':
      print('Day High:' , Robinhood.info['dayHigh'], 'Regular Market Price:' , Robinhood.info['regularMarketPrice'])
      loop == True
      break
    elif info_length == 'long':
      print(Robinhood.info)
      loop == True
      break
    else:
      print("Please type either 'short' or 'long'.")
  #Tesla stock
  elif stock_Wanted == 'Tesla':
    info_length = input("Do you want short info or long? ")
    if info_length == 'short':
      print('Day High:' , Tesla.info['dayHigh'], 'Regular Market Price:' , Tesla.info['regularMarketPrice'])
      loop == True
      break
    elif info_length == 'long':
      print(Tesla.info)
      loop == True
      break
    else:
      print("Please type either 'short' or 'long'.")
  #Twitter stock
  elif stock_Wanted == 'Twitter':
    info_length = input("Do you want short info or long? ")
    if info_length == 'short':
      print('Day High:' , Twitter.info['dayHigh'], 'Regular Market Price:' , Twitter.info['regularMarketPrice'])
      loop == True
      break
    elif info_length == 'long':
      print(Twitter.info)
      loop == True
      break
    else:
      print("Please type either 'short' or 'long'.")
  #Verizon stock
  elif stock_Wanted == 'Verizon':
    info_length = input("Do you want short info or long? ")
    if info_length == 'short':
      print('Day High:' , Verizon.info['dayHigh'], 'Regular Market Price:' , Verizon.info['regularMarketPrice'])
      loop == True
      break
    elif info_length == 'long':
      print(Verizon.info)
      loop == True
      break
    else:
      print("Please type either 'short' or 'long'.")
  #Visa stock
  elif stock_Wanted == 'Visa':
    info_length = input("Do you want short info or long? ")
    if info_length == 'short':
      print('Day High:' , Visa.info['dayHigh'], 'Regular Market Price:' , Visa.info['regularMarketPrice'])
      loop == True
      break
    elif info_length == 'long':
      print(Visa.info)
      loop == True
      break
    else:
      print("Please type either 'short' or 'long'.")
  #Zillow stock
  elif stock_Wanted == 'Zillow':
    info_length = input("Do you want short info or long? ")
    if info_length == 'short':
      print('Day High:' , Zillow.info['dayHigh'], 'Regular Market Price:' , Zillow.info['regularMarketPrice'])
      loop == True
      break
    elif info_length == 'long':
      print(Zillow.info)
      loop == True
      break
    else:
      print("Please type either 'short' or 'long'.")


#Citations will be added to the final documents
