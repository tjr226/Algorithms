#!/usr/bin/python

import argparse

def find_max_profit(prices):
  historical_min_price = prices[0]
  max_profit = prices[1] - prices[0]

  for i in range(1, len(prices)):
    current_profit = prices[i] - historical_min_price
    if current_profit > max_profit:
      max_profit = current_profit
    if prices[i] < historical_min_price:
      historical_min_price = prices[i]

  return max_profit

# stock_prices = [10, 7, 5, 8, 11, 9]
# print(find_max_profit(stock_prices))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))