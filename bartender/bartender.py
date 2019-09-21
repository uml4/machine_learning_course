# questions = {
# "strong": "Do ye like yer drinks strong?",
# "salty": "Do ye like it with a salty tang?",
# "bitter": "Are ye a lubber who likes it bitter?",
# "sweet": "Would ye like a bit of sweetness with yer poison?",
# "fruity": "Are ye one for a fruity finish?",
# }
# ingredients = {
# "strong": ["glug of rum", "slug of whisky", "splash of gin"],
# "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
# "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
# "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
# "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
# }

import random


questions = {
            "strong": "Do ye like yer drinks strong?",
            "salty": "Do ye like it with a salty tang?",
            "bitter": "Are ye a lubber who likes it bitter?",
            "sweet": "Would ye like a bit of sweetness with yer poison?",
            "fruity": "Are ye one for a fruity finish?",
            }
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


def user_input():
    # Get randomly an item from question then ask user
    while 1:
        taste, question = random.choice(list(questions.items()))
        print(question + " \n")
        answer = input("Please give us your answer (y/n) - q to stop")
        # print(answer)
        if ( answer == 'y' ) :
            print_ingredient(taste)
            break
        elif ( answer == 'q' ) :
            break


def print_ingredient( taste ):

    print(" here is the ingredient :")
    for ingredient in ingredients[taste]:
         print(ingredient)


user_input()