#! python3

import requests
import bs4
import os

recipeName = input('Enter name of a recipe from CafeDelites.com: \n')

if "-" not in recipeName:   # checks to see if the input does not contain a hypen
    recipeName = recipeName.replace(" ", "-").lower()

baseUrl = 'https://cafedelites.com/'
recipeUrl = baseUrl + recipeName + '/'


def main():
    retrieve_recipe(recipeUrl)


def retrieve_recipe(url):
    try:
        r = requests.get(url)
        r.raise_for_status()


    except requests.exceptions.MissingSchema:
        print('''It appears the recipe you entered has a problem.. please consider one of the following:
        Check the spelling of the recipe.
        Check to make sure the recipe exists in cafedelites.com''')
    return r


response = retrieve_recipe(recipeUrl)
soupObj = bs4.BeautifulSoup(response.text, 'html.parser')


# -group elements do not contain the header therefore I have to print it out to the user
def show_ingredients(soup):
    output = []
    ingredients = soup.find_all('div', class_='wprm-recipe-ingredient-group')
    for i in range(len(ingredients)):
        output.append(ingredients[i].text.strip())
    return output


# -group elements do not contain the header therefore I have to print it out to the user
def show_instructions(soup):

    instructions = soup.find_all('div', class_='wprm-recipe-instruction-group')
    for i in range(len(instructions)):
        return instructions[i].text.strip()


retrieve_recipe(recipeUrl)
allIngredients = show_ingredients(soupObj)
print('INGREDIENTS')
for i in range(len(allIngredients)):
    print(allIngredients[i])

allInstructions = show_instructions(soupObj)
print('INSTRUCTIONS')
print(allInstructions)


if __name__ == "__main__":
    main()
