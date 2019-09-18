#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  knapsack_matrix = [[0 for column in range(capacity + 1)] for row in range(len(items) + 1)]
  
  '''
  This function uses the format (rows, columns)
  '''

  rows = len(knapsack_matrix)
  columns = len(knapsack_matrix[0])
  
  for row in range(1, rows):
    '''
    row is current item index
    start with 1 to have row of zeros initially
    need to access items index of (row - 1) because Items input is a zero indexed list
    next line - confirming all items being accessed
    '''

    for column in range(1, columns):
      current_item = items[row - 1]

      ''' first option - choose value in previous column '''
      top_option = knapsack_matrix[row - 1][column]

      ''' second option - use current item, plus value in previous row (less current item size)'''
      item_and_previous_option = 0
      ''' add current item if it fits '''
      if current_item.size <= column:
        item_and_previous_option += current_item.value
        ''' add previous value if it also fits '''
        if column - current_item.size >= 0:
          item_and_previous_option += knapsack_matrix[row - 1][column - current_item.size]

      ''' pick higher value - immediately above, or current row item and any values from previous row that fit '''
      knapsack_matrix[row][column] = max(top_option, item_and_previous_option) 

  ''' find out which ones were chosen '''

  row_index = rows - 1
  column_index = columns - 1
  used_items = []

  while row_index > 0:
    if knapsack_matrix[row_index][column_index] == knapsack_matrix[row_index - 1][column_index]:
      # do nothing if current value matches value in next row (remember, we're decrementing)
      pass
    else:
      # add item to the used_items list. decrement size available (column_index) by size of the current object
      used_items.append(row_index)
      column_index -= items[row_index - 1].size  

    # decrement the row index 
    row_index -= 1

  # tests expect a dictionary with a sorted list
  used_items.sort()
  dict_to_return = {}
  dict_to_return['Value'] = knapsack_matrix[-1][-1]
  dict_to_return['Chosen'] = used_items

  return dict_to_return
  
if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')