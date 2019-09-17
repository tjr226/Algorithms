#!/usr/bin/python

import sys

# def rock_paper_scissors_recursion(n, arr):
#   pass

# def rock_paper_scissors(n):
#   # recursive version
#   rps_list = [['rock'], ['paper'], ['scissors']]
#   return_list = rps_list[:]

#   if n <= 0:
#     return [[]]
#   elif n == 1:
#     return return_list
#   else:
#     rock_paper_scissors_recursion(n - 1, rps_list)




def rock_paper_scissors_iterative(n):
  rps_list = [['rock'], ['paper'], ['scissors']]
  return_list = rps_list[:]

  if n == 0:
    return [[]]
  elif n == 1:
    return return_list
    
  while n > 1:
    temp_list = []
    for i in return_list:
      for j in rps_list:
        temp_list.append(i + j)
    n -= 1
    return_list = temp_list[:]

  return return_list

print(rock_paper_scissors_iterative(3))


# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')