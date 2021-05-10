import json

from urllib.request import urlopen

with urlopen("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita") as response:
    source = response.read()

print(source)

data = json.loads(source)

print(json.dumps(data,indent=2))

drink_dict = dict()

for drink in data['drinks']:
    print(drink['idDrink'],drink['strDrink'])
    a = drink['idDrink']
    b = drink['strDrink']
    drink_dict[a] = b

print(drink_dict)

#Writing python dict on json file
 
with open('new_cocktail.json', 'w') as f:
    json.dump(drink_dict,f, indent=2)




    
