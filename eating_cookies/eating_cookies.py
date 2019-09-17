#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# cache = {1: 1, 2: 2, 3: 4}
cache = []

def eating_cookies(n, cache=None):
  # memoized version using a list of zeros as cache
  cache[0] = 1
  cache[1] = 1
  cache[2] = 2
  cache[3] = 4
  
  if n < 0:
    return cache[0]
  elif cache[n] != 0:
    return cache[n]
  else:
    result = eating_cookies(n - 3, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 1, cache)
    cache[n] = result
    return result

# def eating_cookies(n, cache=None):
#   # memoized version using a dictionary as cache
#   # print(n, cache)
#   if n <= 0:
#     return 1
#   elif n < len(cache:
#     return cache[n]
#   else:
#     result = eating_cookies(n - 3, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 1, cache)
#     cache[n] = result
#     return result

# def eating_cookies_recursive(n, cache=None):
#   # print(n)
#   # recursive version
#   if n <= 0:
#     return 1
#   if n == 1:
#     return 1
#   elif n == 2:
#     return eating_cookies_recursive(n - 1) + 1
#   elif n == 3:
#     return eating_cookies_recursive(n - 2) + eating_cookies_recursive(n - 1) + 1
#   else:
#     return eating_cookies_recursive(n - 3) + eating_cookies_recursive(n - 2) + eating_cookies_recursive(n - 1)
# #
# print(eating_cookies(5, cache))
# print(eating_cookies(2, cache))

# print(eating_cookies(1, cache))
# print(eating_cookies(10, cache))
# print(eating_cookies(100, cache))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')