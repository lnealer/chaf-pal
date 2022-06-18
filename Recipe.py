from enum import Enum

class IngredientType(Enum):
  MEAL = 1
  PROTEIN = 2
  VEGGIE = 3
  CARB = 4

class Recipe:

  def __init__(self, proteins=None, veggies=None, carbs=None, name=""):
    if proteins is None or carbs is None or veggies is None:
      self.proteins = []
      self.veggies = []
      self.carbs = []
      self.name = ""
      self.type  = IngredientType.MEAL
    else:
      self.name = name
      self.proteins = proteins
      self.veggies = veggies
      self.carbs = carbs
      self.type  = IngredientType.MEAL

  def add_ingredient(self, ingredient):
    if ingredient.type.value == IngredientType.PROTEIN.value:
      self.proteins.append(ingredient.name)
    elif ingredient.type.value == IngredientType.CARB.value:
      self.carbs.append(ingredient.name)
    elif ingredient.type.value == IngredientType.VEGGIE.value:
      self.veggies.append(ingredient.name)
    else:
      return 0
    return 1