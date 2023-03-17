import requests


API_KEY = "d9db5d4c9a384719bccc179789fc0f20"
SEARCH_API = "https://api.spoonacular.com/recipes/complexSearch"

params = {
    "apiKey": API_KEY,
    "includeIngredients": "saffron",
    "excludeIngredients": "Asparagus",
    "number": 2
}

req = requests.get(SEARCH_API, params)
req.raise_for_status()
results = req.json()
print(results)