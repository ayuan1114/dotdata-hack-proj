# author: Aaron Yuan

import requests

# Class that retrieves desired recipe information from API
class RecipeExtract:
    def __init__(self, ingredients: list, number=5):
        self.number = number
        self.ingredients = ingredients
        self.response = {}
        self.recipes = []

    def print(self):
        for recipe in self.recipes:
            print("--------------------------------------------------------------")
            for key in recipe.keys():
                print(key, ":", recipe[key])

    def changeIngredients(self, ingList: list):
        self.ingredients = ingList

    def changeNumber(self, number: int):
        self.number = number

    def cat(self, ingList: list):
        toReturn = ""
        for i in range(len(ingList)):
            toReturn += ingList[i]
            if (i != len(ingList) - 1):
                toReturn += ","
        return toReturn

    def get(self, filename=""):
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

        print(self.cat(self.ingredients))
        print(str(self.number))

        querystring = {"ingredients": self.cat(self.ingredients),
                       "number": str(self.number),
                       "ignorePantry": "true",
                       "ranking": "1"}

        headers = {
            "X-RapidAPI-Key": "a815efa3e5msh871c0c4b35a214cp104d38jsne96a4aadce16",
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

        self.response = requests.get(url, headers=headers, params=querystring)
        print(self.response.json())

    def extract(self, raw=[]):
        if len(raw) == 0:
            raw = self.response.json()
        for recipe in raw:
            newRecipe = {}
            newRecipe["name"] = recipe["title"]
            newRecipe["id"] = recipe["id"]
            newRecipe["imageType"] = recipe["imageType"]
            newRecipe["image"] = recipe["image"]
            newRecipe["numMissing"] = recipe["missedIngredientCount"]
            newRecipe["numIngredients"] = len(recipe["missedIngredients"] + recipe["usedIngredients"])
            newRecipe["ingredients"] = []
            for ingredient in recipe["missedIngredients"] + recipe["usedIngredients"]:
                newIng = {}
                newIng["info"] = ingredient["original"]
                newIng["image"] = ingredient["image"]
                newRecipe["ingredients"].append(newIng)
            self.recipes.append(newRecipe)

    def recipeNames(self):
        return [recipe["name"] for recipe in self.recipes]

    def getRecipe(self, index=-1, name="") -> dict:
        if (index >= 0):
            return self.recipes[index]
        if (name != ""):
            for recipe in self.recipes:
                if recipe["name"] == name:
                    return recipe
        return {}

    def getInstructions(self, index=-1, name=""):
        recipe = self.getRecipe(index=index, name=name)
        if "instructions" in recipe.keys():
            return recipe["instructions"]
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + str(recipe["id"]) + "/information"

        headers = {
            "X-RapidAPI-Key": "a815efa3e5msh871c0c4b35a214cp104d38jsne96a4aadce16",
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        recipe["instructions"] = response.json()["instructions"]

        return recipe["instructions"]