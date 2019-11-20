# Loads a static database of recipes into a recipe book called book at module level.
# Asks users for info and then does things with them
from recipe import *

def ask_for_filename(prompt="Filename?", default='recipes.json'):
    raw = default
    try:
        raw = input(prompt) or default
        # See, it's easier to ask for forgiveness then permission
        open(raw, 'r').read()  # See if they gave us a file we can open
    except:
        raise Exception("Bad filename!")
    finally:
        return raw

userInput = ask_for_filename('Where should we load the local recipes from (use recipes.json if you aren\'t sure)? ', default='recipes.json')
file = open(userInput, 'r+')
data = file.read()
lines = data.split('\n')
import json
recipes = []
for i in range(len(lines)):
    recipe = recipe_from_args(json.loads(lines[i]))
    recipes.append(recipe)
book=RecipeBook(recipes)
file.close()
