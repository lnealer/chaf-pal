import argparse
from Ingredient import *
from RecipeFinder import *
from glob import glob
from enum import Enum
from Recipe import *

class IngredientType(Enum):
  MEAL = 1
  PROTEIN = 2
  VEGGIE = 3
  CARB = 4

def ReadIngredientFile(ingredient_file):
  # put the ingredient list into the out dictionary
  # each line is of format: ingredient_name ingredient_type
  out = {"Protein":[], "Veggie":[], "Carb":[]}

  with open(ingredient_file) as file:
    data = file.read()
    ingredient_list = data.split('\n')

  for ingredient in ingredient_list:
    line = ingredient.split(' ')
    ingredient_name = ' '.join(line[0:-1])
    ingredient_typename = line[-1]
    out[ingredient_typename.title()] \
    .append(Ingredient(ingredient_name.lower(),  \
                        IngredientType[ingredient_typename.upper()]))
  return out
                
def ReadRecipeFile(meal_filename):
  recipe = Recipe()
  with open(meal_filename) as file:
    data = file.read()
    ingredients = data.split('\n')
  recipe.name = ingredients.pop(0)

  for ingredient_info in ingredients:
    line = ingredient_info.split(' ')
    ingredient_name = ' '.join(line[0:-1])
    ingredient_type = IngredientType[line[-1].upper()]
    ingredient = Ingredient(ingredient_name, ingredient_type)
    recipe.add_ingredient(ingredient)
  return recipe


def ReadMealsFolder(meal_folder_name):
  out = []
  meal_filenames = glob(f"{meal_folder_name}/*.txt")
  for meal_filename in meal_filenames:
    recipe = ReadRecipeFile(meal_filename)
    out.append(recipe)
  return out

def ParseFiles(meals_folder, ingredients_file):
  meals = ReadMealsFolder(meals_folder)
  ingredients = ReadIngredientFile(ingredients_file)
  return meals,ingredients

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
    "--ingredients_file",
    type=str,
    default = "ingredients.txt",
    help = "The name of the txt file containing your list of available ingredients"
  )

  parser.add_argument(
    "--recipe_folder",
    type=str,
    default = "recipes",
    help = "The name of the folder containing your recipes in .txt form"
  )

  args = parser.parse_args()
  meals,ingredients = ParseFiles(args.recipe_folder, args.ingredients_file)
  recipeFinder = RecipeFinder(meals, ingredients)
  recipe = recipeFinder.FindRecipe()
  if recipe:
    print("For dinner you'll be having %s with:\n\tProtein: %s\n\tVeggie: %s\n\tCarb: %s" \
        % (recipe["Meal"].name.lower(), recipe["Protein"].name, \
          recipe["Veggie"].name, recipe["Carb"].name))
    print("Bon appetit!")