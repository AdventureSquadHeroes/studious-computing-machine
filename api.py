import requests

API_KEY = "d9db5d4c9a384719bccc179789fc0f20"
SEARCH_API = "https://api.spoonacular.com/recipes/complexSearch"
RECIPE_API = "https://api.spoonacular.com/recipes/"

class RecipeSearch:
    
    def __init__(self, ingredients=None, cuisine=None, equipment=None):
        self.ingredients = ingredients
        self.cuisine = cuisine
        self.equipment = equipment

    def search(self):
        header = {
            "x-api-key": API_KEY
        }
        params = {
            "cuisine": self.cuisine,
            "includeIngredients": self.ingredients,
            "equipment": self.equipment,
            "number": 25
        }
        req = requests.get(SEARCH_API, params=params, headers=header)
        req.raise_for_status()
        results = req.json()
        return results
        
    def recipe_search(id):
        recipe_api = f"https://api.spoonacular.com/recipes/{id}/information"
        header = {
            "x-api-key": API_KEY
        }
        params = {
            "id": id
        }
        req = requests.get(recipe_api, params=params, headers=header)
        req.raise_for_status()
        results = req.json()
        return results
