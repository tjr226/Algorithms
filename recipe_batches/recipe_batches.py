#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # if you don't have an ingredient, can't make the recipe
  for r in recipe:
    if r not in ingredients:
      return 0


  possible_batches = 0
  can_make_more = True
  
  while can_make_more:
    for i in ingredients:
      if ingredients[i] < recipe[i]:
        can_make_more = False
      else:
        ingredients[i] -= recipe[i]
    
    if can_make_more == True: 
     possible_batches += 1 

  return possible_batches
  


# recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
# ingredients = { 'milk': 232, 'butter': 148, 'flour': 51 }

# print(recipe_batches(recipe, ingredients))


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


