# TO USE: python3 game_demo.py shop_data.JSON
import json
import time
from numpy import random
import sys
from argparse import ArgumentParser
class Shop:
    def __init__(self, shop_path):
        with open(shop_path, 'r') as f:
            self.shopdata = json.load(f)
            self.shopdata = dict(self.shopdata)
        
        self.recipes = [r for r in self.shopdata["Recipes"]]
        self.ad_levels = [a for a in self.shopdata["Ad Levels"]]
        # self.owned_recipes = {"Sugar cookies":self.shopdata["Recipes"]["Sugar cookies"]}
        self.owned_recipes = {r : self.shopdata["Recipes"][r] for r in self.recipes}
        self.ad_level = {"Level 1":self.shopdata["Ad Levels"]["Level 1"]}
        self.profit = 0
        
        all_shop = self.recipes + self.ad_levels
        self.unlockable = {i : "Locked" for i in all_shop}
        self.unlockable["Sugar cookies"] = "Owned"
        self.unlockable["Level 1"] = "Owned"
        
        self.recipe_shop = {r : (self.shopdata["Recipe prices"][r], 
                                 self.shopdata["Selling prices"][r]) 
                            for r in self.recipes}
        self.ad_shop = {a : (self.shopdata["Ad prices"][a], 
                             self.shopdata["Ad Levels"][a]) 
                        for a in self.ad_levels}
        
    def __str__(self):
        """Provide an informal string representation for the game's shop, which
        includes recipes and ad levels.

        Returns:
            str: The informal representation of the game's shop.
        """
        recipe_shop = [f"\n{r}:\n${prices[0]} (P) * ${prices[1]} (S) * {self.unlockable[r]}" 
                       for r, prices in self.recipe_shop.items()]
        ad_shop = [f"\n{a}:\n${info[0]} (P) * {info[1]} (C) * {self.unlockable[a]}"
                   for a, info in self.ad_shop.items()]
        return (f"\n------ Recipe Shop ------\n"
                f"Recipe Price (P) | Selling Price (S) | Lock Status\n"
                '*Note: "Selling Price" is what your customers will pay.\n'
                f"{'\n'.join(recipe_shop)}"
                f"\n\n------ Ad Level Shop ------\n"
                f"Level Price (P) | Customers (C) | Lock Status\n"
                f"{'\n'.join(ad_shop)}"
        )

    def valid_request(self, request):
        """Ensure that the player's input for a menu option request is valid.

        Args:
            request (str): player's input when asked if they want a certain menu 
            option.

        Returns:
            str: the player's input if it's valid. If input is invalid, 'invalid'.
        """
        if not isinstance(request, str):
            return 'invalid'
        else:
            if request in ('shop', 'recipes', 'continue', 'end game'):
                return request
            else:
                return 'invalid'
            
    def fulfill_request(self, request):
        """Carry out player's menu option request.

        Args:
            request: player's menu option request.

        Side effects:
            Print to stdout.
            Modify attributes if player purchases an item.
        """
        if request == 'recipes':
            recipes = [f"\n{r}: {self.owned_recipes[r]}" for r in self.owned_recipes]
            print("\n------ Your Recipes ------\n"
                f"{'\n'.join(recipes)}")
        elif request == 'shop':
            print(self)
        elif request == 'continue':
            self.day_profit()
            pass
        elif request == 'end game':
            print("Thanks for playing!")
            quit()
    
    def day_profit(self, show_stats = True, expense_rate = None):
        """
        Calculates the revenue, expenses, and profits for the day.
        
        Args:
            customerpath: The path of the text file to be used to import
            customer names.
            show_stats: Determines if all the stats should be printed.
            expense_rate: A set amount of money going towards expenses.
        """
        
        current_level = list(self.ad_level)[0]
        # 3
        num_customers = self.shopdata["Ad Levels"][current_level]
        # 3
        revenue = 0
        expenses = 0
        
        for i in range(num_customers):
            current_dish = random.choice(list(self.owned_recipes))
            selling_price = self.shopdata["Selling prices"][current_dish]
            score = handle_dish(current_dish, self.owned_recipes)
            revenue += (selling_price * (score / 2))
            expenses += round(revenue * random.rand(), 2)

        daily_profit = revenue - expenses
        self.profit += daily_profit

        print("------ Today's Stats ------")
        print(f"Customers served: {num_customers}")
        print(f"Revenue: ${round(revenue, 2)}")
        print(f"Expenses: ${expenses}")
        print(f"Daily profit: ${round(daily_profit, 2)}")
        print(f"Total profit: ${round(self.profit, 2)}")
        self.prompt_request()
        
    def prompt_request(self):
        """Prompt player for menu option requests and carry them out.

        Side effects:
            Print to stdout.
            Modify certain attributes if player purchases an item.
        """
        menu_options = ("\n------ Menu Options ------\n"
                    "[recipes] to review your recipes\n"
                    "[shop] to browse the shop\n"
                    "[continue] to continue to the next day\n"
                    "[end game] to end the game\n\n"
                    )
        request = input(menu_options)
        validated = self.valid_request(request.lower())
        while validated == 'invalid':
            print("\n* That's not a valid menu option. Try again! *")
            request = input(menu_options)
            validated = self.valid_request(request.lower())
        self.fulfill_request(validated)
        more = input("\nWould you like to select another menu option? (Y/N). ")
        while more.lower() not in ('y', 'n'):
            print("\n* That's not a valid option. Try again! *")
            more = input("\nWould you like to select another menu option? (Y/N). ")
        if more.lower() == 'y':
            self.prompt_request()
        elif more.lower() == 'n':
            self.fulfill_request('continue')
            
# def day_end(self):
#         """Display end of day stats and prompt player requests.
    
#         Args:
#             ad_level: The player's current ad level.
        
#         Side effects:
#             Print to stdout.
#         """
#         expenses = round(self.profit * random.rand(), 2)
#         print("------ Today's Stats ------\n"
#           f"Total customers: {self.ad_level}\n"
#           f"Daily profit: {self.daily_profit}"
#           f"Expenses: ${expenses}\n"
#           f"Current profit: ${round(self.profit - expenses, 2)}\n"
#           )
#         self.prompt_request()
    
from random import shuffle

def handle_dish(current_dish, recipe_dict):
    """

    Author: Kyle Tice (with customer logic from Ethan Gustave)
    
    Handles the playing stage of each dish by giving inputs to the user. Their
    performance is decided by the order in which the ingredients are typed.

    Args: 
        current_dish (String): the current food dish being made
        recipe_dict (dict): dictionary of foods and associated ingredient lists

    Side Effects:
        Prompts user for extra inputs (active game stage)
    
    Returns:
        score (int): the score of the dish the user just created
    
    Technique:
        f-strings
    """
    # techniques and authors are in README, don't think they should be in docstrings

    # defines the correct order of ingredients
    correct_order = recipe_dict[current_dish]
    
    shuffled = correct_order[:]
    shuffle(shuffled)
    print(f"\nDish: {current_dish}\n")
    print("Ingredients (shuffled):")

    # builds the user-inputted list of ingredients
    for ingredient in shuffled:
        print(f"- {ingredient}")

    print("\nEnter the ingredients in the correct order:")

    user_list = []

    
    for i in range(len(correct_order)):
        user_input = input(f"Step {i+1}: ").strip()
        user_list.append(user_input)
        
    print("Cooking...\n")
    time.sleep(.5)
    print("Done!")
    time.sleep(.5)
    score = rate_dish(user_list, correct_order)
    time.sleep(1)
    print(f"\nYou scored: {score}/{len(correct_order)}")
    time.sleep(1)
    return score


def rate_dish(user_list, correct_list):
    """

    Author: Kyle Tice
    
    Rates the dish the user just created by checking the positions of all user
    inputted ingredients in comparison to the correct list of ingredients.

    Args: 
        user_list (list of str): the list of ingredients the user typed
        correct_list (list of str): the correct list of ingredients for the dish

    Side Effects:
        prints outputs directly to the user with print() statements
    
    Returns:
        score (int): the score of the dish the user just created
    
    Technique:
        key lambda with sorting
    """
    # ranks ingredients so that correct ones are listed first
    ranked = sorted(
        user_list,
        key=lambda x: (
            x not in correct_list,  # False (correct) comes before True (incorrect)
            correct_list.index(x) if x in correct_list else float('inf')
        )
    )

    # displays the ranking of the user's ingredients
    print("\nRanked ingredients (correct to incorrect):")
    for item in ranked:
        print(f"- {item}")

    # score based on correct position
    score = sum(
        1 for i in range(len(correct_list))
        if i < len(user_list) and user_list[i] == correct_list[i]
    )

    return score
    


def main(path):
    game = Shop(path)
    game.prompt_request()
    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("path")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.path)