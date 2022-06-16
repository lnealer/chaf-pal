from enum import Enum
from Recipe import *
from Ingredient import *
class IngredientType(Enum):
  MEAL = 1
  PROTEIN = 2
  VEGGIE = 3
  CARB = 4
  

class RecipeFinder:
  def __init__(self, meals, ingredients):
    self.meals = meals
    self.ingredients = ingredients
    empty_ingredient = Ingredient()
    self.currentMeal = {"Meal": Recipe(), 
      "Protein":empty_ingredient, 
      "Veggie":empty_ingredient, 
      "Carb":empty_ingredient}
    self.stack = self.meals
  

  def IsMealValid(self):
    # check if the current meal is valid
    # a valid meal has all of the ingredients for the chosen recipe
    recipe = self.currentMeal["Meal"]
    #self.meals[self.currentMeal["Name"]]
    return self.currentMeal["Protein"].name in recipe.proteins \
      and self.currentMeal["Veggie"].name in recipe.veggies \
      and self.currentMeal["Carb"].name in recipe.carbs

  def IngredientInRecipe(self, ingredient, recipe):
    if ingredient.type.value == IngredientType.PROTEIN.value:
      return ingredient.name in recipe.proteins
    elif ingredient.type.value == IngredientType.CARB.value:
      return ingredient.name in recipe.carbs
    elif ingredient.type.value == IngredientType.VEGGIE.value:
      return ingredient.name in recipe.veggies
    else:
      return False

  def MealIncomplete(self): 
    # check if the meal is complete 
    # i.e. does it contain a protein, veggie, and carb
    return not self.currentMeal["Protein"].name != "" \
      or not self.currentMeal["Veggie"].name != "" \
      or not self.currentMeal["Carb"].name != ""

  def MoveForward(self):
    # run one step of the algorithm
    if not self.stack:
      # if the stack is empty, the algorithm has failed to find a valid recipe
      print("Go to the grocery store!")
      return -1

    current_ingredient = self.stack.pop()
    self.currentMeal[current_ingredient.type.name.title()] = current_ingredient
    if (not self.MealIncomplete()) and self.IsMealValid():
      # you have a well balanced and valid recipe
      return 1
    if self.IngredientInRecipe(current_ingredient, self.currentMeal["Meal"]) or current_ingredient.type.value == IngredientType.MEAL.value:
      # push the next ingredient type onto the list
      next_ingredient_type = IngredientType(current_ingredient.type.value + 1)
      self.stack = self.stack + self.ingredients[next_ingredient_type.name.title()] 
    #print(self.stack)
    return 0

  def FindRecipe(self):
    while self.MoveForward() == 0:
      out = self.currentMeal
    if self.MoveForward == -1:
      return None
    return self.currentMeal
  