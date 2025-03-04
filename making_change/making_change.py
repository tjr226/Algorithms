#!/usr/bin/python

import sys

def making_change(amount, denominations):
  if amount < 0:
    return 1

  combinations = [0]*(amount + 1)
  combinations[0] = 1

  for d in denominations:
    for c in range(1, len(combinations)):
      if c >= d:
        combinations[c] += combinations[c-d]
    # print(d, combinations)

  
  return combinations[-1]

  


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")