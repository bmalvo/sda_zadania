# Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.
# Can you help him to find out, how many cakes he could bake considering his recipes?
#
# Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object)
# and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts
# (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects,
# can be considered as 0.
#
# Examples:
#
# # must return 2
# cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# # must return 0
recipe = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
available = {'sugar': 500, 'flour': 2000, 'milk': 2000}

recipe_1 = {'flour': 500, 'sugar': 200, 'eggs': 1}
available_1 = {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}

recipe_2 = {'milk': 97, 'eggs': 5, 'oil': 15}
available_2 = {'cream': 8485, 'flour': 6178, 'pears': 8284, 'milk': 75, 'apples': 501, 'chocolate': 6635, 'eggs': 6820,
               'sugar': 5697, 'cocoa': 1983, 'oil': 7990}

recipe_3 = {'cream': 69, 'oil': 47, 'cocoa': 49}
available_3 = {'milk': 6863, 'pears': 6551, 'apples': 9098, 'cream': 9223, 'nuts': 1029, 'flour': 614, 'eggs': 8499,
               'oil': 4662, 'sugar': 8729, 'cocoa': 2700}
 # 1 should equal 55

many = []
def cakes(recipe, available):
    for key in recipe:
        if key not in available or recipe[key] > available[key]:
            return 0
    for key in available:
        if key in recipe:
            many.append(available[key]/recipe[key])
    return round(min(many))

# print(cakes(recipe_1,available_1))
# print(cakes(recipe,available))
# print(cakes(recipe_2,available_2))
print(cakes(recipe_3,available_3))

