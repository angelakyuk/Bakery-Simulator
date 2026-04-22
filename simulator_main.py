# ANGELA KYUK
from numpy import random
# from argparse import ArgumentParser
# import sys

def valid_request(request):
    """Ensure that the player's input for a menu option request is valid.
    
    Args:
        request (str): player's input when asked if they want a certain menu 
            option.
    
    Returns:
        str: the player's input if it's valid. If input is invalid, 'invalid'.
    """
    valid_requests = ('shop', 'recipes', 'continue', 'end game')
    if not isinstance(request, str):
        return 'invalid'
    else:
        if request in valid_requests:
            return request
        else:
            return 'invalid'
        
advertisement = {1 : 3}
owned_recipes = ('cookie')
recipes = {'cookie' : ['ingredient', 'ingredient']}
shop = {'item' : 5}
# data will be from JSON file
    
def fulfill_request(request):
    """Carry out player's menu option request.
    
    Args:
        request: player's menu option request.
    
    Side effects:
        Print to stdout.
        Modify attributes if player purchases an item.
    """
    if request == 'recipes':
        print(owned_recipes)
    elif request == 'shop':
        # function that shows shop and unlocks items
        pass
    elif request == 'continue':
        # function that starts new day/round
        pass
    elif request == 'end game':
        print("Thanks for playing!")
        quit()

def day_end(ad_level, gross_profit):
    """Display end of day stats and prompt player requests.
    
    Args:
        ad_level: player's current ad level.
        gross_profit: player's gross profit for the day.
        
    Side effects:
        Print to stdout.
    """
    expenses = round(gross_profit * random.rand(), 2)
    print("------ Today's Stats ------\n"
          f"Total customers: {advertisement[ad_level]}\n"
          f"Gross profit: ${round(gross_profit, 2)}\n"
          f"Expenses: ${expenses}\n"
          f"Net Profit: ${round(gross_profit - expenses, 2)}\n"
          )
    prompt_request()

def prompt_request():
    """Prompt player for menu option requests, validate those requests, and 
    fulfill them."
    
    Side effects:
        Print to stdout.
        Modify certain attributes if player purchases an item.
    """
    menu_options = ("------ Menu Options ------\n"
                    "[recipes] to review your recipes\n"
                    "[shop] to browse the shop\n"
                    "[continue] to continue to the next day\n"
                    "[end game] to end the game\n"
                    )
    request = input(menu_options)
    validated = valid_request(request.lower())
    while validated == 'invalid':
        print("That's not a valid menu option. Try again!")
        request = input(menu_options)
        validated = valid_request(request.lower())
    fulfill_request(validated)
    more = input("Would you like to select another menu option? (Y/N). ")
    while more.lower() != 'y' and more.lower() != 'n':
        print("That's not a valid option. Try again!")
        more = input("Would you like to select another menu option? (Y/N). ")
    if more.lower() == 'y':
        prompt_request()
    elif more.lower() == 'n':
        fulfill_request('continue')
        
#Sarayu Vanam's function
def handle_unlocks(money, recipes):
    """
    Determines which recipe is unlocked based on how much money the baker has.

    Args:
        money (float): The amount of money the player currently has.
        recipes (dict): A dictionary of recipes where each recipe includes 
                        its name, price, and locked/unlocked status.

    Side Effects:
        Modifies the recipes dictionary by updating which recipes are 
        locked or unlocked for the player.

    Returns:
        dict: The updated dictionary of recipes with their current unlock status
    """

    for name, info in recipes.items():
        if money >= info["price"]:
            info["unlocked"] = True
        else:
            info["unlocked"] = False

    return recipes

#Ethan Gustave's Function
from random import choice

def create_customers(num, customers):
    """Creates a list of customers from the amount specified for the day

    Args: 
	    num(int): the number of customers to be generated based on ad level.
	    customers(dict): the customers to be chosen from. Key is customer name,
        associated value is a customer object.

    Returns: 
        A list of dictionaries. In the dictionary, the key will be the customer 
        name and the associated value will be a reference to a customer object.
    """
    
    if num > len(customers):
        num = len(customers)
        
    customer_start = customers.copy()
    customer_final = []
    count = 0
    
    while(count < num):
        curr = choice(customer_start.keys())
        customer_final.append(curr, customer_start.pop(curr))
        count += 1
        
    return customer_final


#Kyle Tice's Function

from random import shuffle

def handle_dish(current_dish, recipe_dict):
    """
    Handles the playing stage of each dish by giving inputs to the user. Their
    performance is decided by the order in which the ingredients are typed.

    Args: 
        current_dish (String): the current food dish being made
        recipe_dict (dict): dictionary of foods and associated ingredient lists

    Side Effects:
        Prompts user for extra inputs (active game stage)
    
    Returns:
        score (int): the score of the dish the user just created
    """

    
    correct_order = recipe_dict[current_dish]

    
    shuffled = correct_order[:]
    shuffle(shuffled)

    print(f"\n Dish: {current_dish}")
    print("Ingredients (shuffled):")

    
    for ingredient in shuffled:
        print(f"- {ingredient}")

    print("\nEnter the ingredients in the correct order:")

    user_list = []

    
    for i in range(len(correct_order)):
        user_input = input(f"Step {i+1}: ").strip()
        user_list.append(user_input)

    
    score = rateDish(user_list, correct_order)

    print(f"\n⭐ You scored: {score}/4")

    return score



def rateDish(user_list, correct_list):
    return 0  # placeholder


