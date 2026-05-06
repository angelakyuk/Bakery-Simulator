from numpy import random
import json

# ANGELA KYUK
class Shop:
    """Provide and update information about shop items.
    
    Attributes:
        shopdata (dict): A dictionary with the following keys:
            - "Recipes" (dict of {str:list[str]}): A dictionary of recipe 
                ingredients. The keys are recipe names and the values are a
                list of ingredients.
            - "Recipe prices" (dict of {str:int}): A dictionary of recipe 
                prices for the player. The keys are recipe names and the 
                values are the corresponding price.
            - "Selling prices" (dict of {str:int}): A dictionary of selling
                prices of baked goods to customers. The keys are recipe
                names and the values are the corresponding selling price.
            - "Ad levels" (dict of {str:int}): A dictionary of ad level 
                information. The keys are ad levels and the values are the
                number of customers the player will serve at that level.
            - "Ad prices" (dict of {str:int}): A dictionary of ad level 
                prices. The keys are ad levels and the values are the 
                corresponding price.
        recipes (list of str): A list of all recipe names.
        ad_levels (list of str): A list of all ad level titles.
        unlockable (dict of {str:str}): A dictionary of the lock status of shop
            items. Keys are recipe or ad level names. Values are "Locked" or
            "Owned".
        recipe_shop (dict of {str:tuple(int, int)}): A dictionary of recipe
            shop information. Keys are recipe names. Values are tuples of the
            recipe's price for the player and selling price to customers.
        ad_shop (dict of {str:tuple(int, int)}): A dictionary of ad level shop
            information. Keys are the ad level. Values are tuples of the level's 
            price for the player and the number of customers they'll serve at 
            that level.
    """
    def __init__(self, shop_path, unlocked_items = {}, unlocked_ad = {}):
        """Initialize ShopData object.
        
        Args:
            shop_path: A path to a JSON file that has shop information.
        
        Side effects:
            Sets the attributes shopdata, recipes, ad_levels, unlockable, 
                recipe_shop, and ad_shop.
        """
        with open(shop_path, 'r') as f:
            self.shopdata = json.load(f)
            self.shopdata = dict(self.shopdata)
            # turned JSON file into dict
        
        self.recipes = [r for r in self.shopdata["Recipes"]]
        self.ad_levels = [a for a in self.shopdata["Ad levels"]]
        self.all_shop = self.recipes + self.ad_levels
        self.unlockable = {i : "Locked" for i in self.all_shop}
        if unlocked_items == {}: # <
            self.unlockable["Sugar cookies"] = "Owned" # <
        else: # <
            for i in unlocked_items: # <
                self.unlockable[i] = "Owned" # <
        if unlocked_ad == {}: # <
            self.unlockable["Level 1"] = "Owned" # <
        else: # <
            self.unlockable["Level 1"] = "" # <
            self.unlockable["Level 2"] = "" # <
            self.unlockable["Level 3"] = "" # <
            self.unlockable[list(unlocked_ad)[0]] = "Owned" # <
        # Added these lines so the shop knows what's already unlocked when
        # the player opens it up
        self.recipe_shop = {r : (self.shopdata["Recipe prices"][r], 
                                 self.shopdata["Selling prices"][r]) 
                            for r in self.recipes}
        self.ad_shop = {a : (self.shopdata["Ad prices"][a], 
                             self.shopdata["Ad levels"][a]) 
                        for a in self.ad_levels}
        
    def __str__(self):
        """Provide an informal string representation for the game's shop.

        Returns:
            str: The informal representation of the game's shop, which includes
                the item's name, purchase price, selling price to customers or 
                number of customers to serve, and lock status.
        """
        recipe_shop = [f"{r}:\n(P) ${p[0]} * (S) ${p[1]} * {self.unlockable[r]}\n" 
                       for r, p in self.recipe_shop.items()]
        ad_shop = [f"{a}:\n(P) ${i[0]} * (C) {i[1]} * {self.unlockable[a]}\n"
                   for a, i in self.ad_shop.items()]
        return (f"------ Recipe Shop ------\n"
                f"Recipe Price (P) | Selling Price (S) | Lock Status\n\n"
                f"{'\n'.join(recipe_shop)}"
                '\n*Note: "Selling Price" is what your customers will pay.\n'
                f"\n------ Ad Level Shop ------\n"
                f"Level Price (P) | Customers (C) | Lock Status\n\n"
                f"{'\n'.join(ad_shop)}"
        )
        
    #Shop methods below by Ethan Gustave
    
    def get_price(self, item_name):
        """Gets price of item given the item name.
        
        Args: 
            item_name(str): name of the item whose price is to be checked.
            
        Returns: 
            the price of the item.
        """
        return(self.recipe_shop(item_name[1]))
        # self.recipe_shop[item][0] bc tuple is (price, selling price)
    
    def owned(self, item_name):
        """Checks if item is owned.
            
            Args:
                item_name(str): the name of the item to be checked
            Returns:
                Bool:
                    True: if item is owned.
                    False: if item is not owned.

            """
        if self.unlockable[item_name] == "Owned":
            return True
        else:
            return False
        
    def check_item(self, item_name):
        """Checks if item request is valid. 
            
            Args:
                item_name(str): the name of the item to be bought
            Returns:
                Bool:
                    True: if item is valid.
                    False: if item is invalid.
            """
        if item_name in self.recipe_shop:
            return True
        else:
            return True if item_name in self.ad_shop else False
        # if item in self.all_shop True else False?
    
    def buy_item(self, item_name):
        """Attempts to buy an item from the shop.
        
        Args:
            item_name: the name of the item to be bought
        Returns:
            Bool:
                True: If the item is bought
                False: if the item name isn't valid or the item is already unlocked.
        Side Effects: 
            - Prints to console depending on result of method
            - Changes the value of an item in the dictionary unlockable from 
                "Locked" to "Owned" if the item is bought.
        """
        
        if item_name in self.unlockable:
            if self.unlockable[item_name] == "Owned":
                pass
            else:
                if item_name in self.recipes:
                    self.unlockable[item_name] == "Owned"
                if item_name in self.ad_levels:
                    self.unlockable["Level 1"] = ""
                    self.unlockable["Level 2"] = ""
                    self.unlockable["Level 3"] = ""
                    self.unlockable[item_name] = "Owned"

class Game:
    """Play Bakery Simulator.
    
    Attributes:
        owned_recipes (dict of {str:list[str]}): A dictionary of recipes the
            player owns. Keys are recipe names. Values are the recipe's 
            ingredients.
        ad_level (dict of {str:int}): A dictionary of the player's current 
            ad level. The key is the ad level (e.g. "Level 1"). The value is
            the number of customers they will serve.
        profit (int): How much money the player currently has.
    """
    def __init__(self, path):
        """_summary_
                    
        Side effects: Sets attributes owned_recipes, ad_level, and profit.
        """
        self.shop = Shop(path)
        self.owned_recipes = {"Sugar cookies":self.shop.shopdata["Recipes"]
                              ["Sugar cookies"]}
        self.ad_level = {"Level 1":self.shop.shopdata["Ad Levels"]["Level 1"]}
        self.profit = 0
        
    def unlock_item(self, item_name):
        """Unlocks an item.
        
        Args: 
            item_name:
                the name of the item to be unlocked.
        Side Effects:
            Modifies owned_recipes and ad_level attributes.
        """
        if item_name in self.shop.shopdata["Recipes"]:
            self.owned_recipes[item_name] = self.shop.shopdata["Recipes"][item_name]
        elif item_name in self.shop.shopdata["Ad levels"]:
            self.ad_level = {item_name : self.shop.shopdata["Ad Levels"][item_name]}
    # Added unlock functionality to Game class so owned_recipes and ad_level had
    # functionality within the game -Ethan
            
    def valid_request(self, request):
        """Ensure that the player's input for a menu option request is valid.
    
        Args:
            request (str): The player's input when asked if they want a certain 
                menu option.
    
        Returns:
            str: The player's input if it's valid. If the input is invalid, 
                returns 'invalid'.
        """
        if not isinstance(request, str):
            return 'invalid'
        else:
            if request in ('shop', 'recipes', 'continue', 'end game'):
                return request
            else:
                return 'invalid'
            
    def fulfill_request(self, request, customerdata):
        """Carry out the player's menu option request.
    
        Args:
            request: The player's menu option request.
    
        Side effects:
            Print to stdout.
            Modify attributes if player purchases an item.
        """
        if request == 'recipes':
            recipes = [f"{r}: {self.owned_recipes[r]}" for r in self.owned_recipes]
            print("------ Your Recipes ------\n"
                f"{'\n'.join(recipes)}")
        elif request == 'shop':
            print(self.shop)
            self.run_shop()
        elif request == 'continue':
            self.day_profit(customerdata)
        elif request == 'end game':
            print("Thanks for playing!")
            quit()
            
    def prompt_request(self, customerdata):
        """Prompt player for menu option requests and carry them out.
    
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
        validated = self.valid_request(request.lower())
        while validated == 'invalid':
            print("That's not a valid menu option. Try again!")
            request = input(menu_options)
            validated = self.valid_request(request.lower())
        self.fulfill_request(validated, customerdata)
        more = input("Would you like to select another menu option? (Y/N). ")
        while more.lower() not in ('y', 'n'):
            print("That's not a valid option. Try again!")
            more = input("Would you like to select another menu option? (Y/N). ")
        if more.lower() == 'y':
            self.prompt_request()
        elif more.lower() == 'n':
            self.fulfill_request('continue', customerdata)
            
    def day_end(self):
        """Display end of day stats and prompt player requests.
    
        Args:
            ad_level: The player's current ad level.
        
        Side effects:
            Print to stdout.
        """
        expenses = round(self.profit * random.rand(), 2)
        print("------ Today's Stats ------\n"
          f"Total customers: {self.ad_level}\n"
          f"Daily profit: {self.daily_profit}"
          f"Expenses: ${expenses}\n"
          f"Current profit: ${round(self.profit - expenses, 2)}\n"
          )
        self.prompt_request()
    
    def day_profit(self, customerpath, show_stats = True, expense_rate = None):
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
        num_customers = self.gamedata["Ad levels"][current_level]
        # 3
        customers = create_customers(num_customers, customerpath)
        revenue = 0
            
        for c in customers:
            current_dish = random.choice(list(self.owned_recipes))
            selling_price = self.shop.shopdata["Selling prices"][current_dish]
            score = handle_dish(current_dish, self.owned_recipes, c)
            revenue += (selling_price * (score / 2))
            expenses += round(revenue * random.rand(), 2)
        # alternative dish code that implements handle_dish and create_customer
        
        for i in range(num_customers):
            current_dish = random.choice(list(self.owned_recipes))
            selling_price = self.gamedata["Selling prices"][current_dish]
            revenue += selling_price
            expenses = round(revenue * random.rand(), 2)

        daily_profit = revenue - expenses
        self.profit += daily_profit

        print("------ Today's Stats ------")
        print(f"Customers served: {len(customers)}")
        print(f"Revenue: ${round(revenue, 2)}")
        print(f"Expenses: ${expenses}")
        print(f"Daily profit: ${round(daily_profit, 2)}")
        print(f"Total profit: ${round(self.profit, 2)}")
    
    def run_shop(self):
        
        
        player_in = input(
            """What would you like to do?
            Options: buy, leave"""
        )
        
        if player_in == "buy":
            item = input("What would you like to purchase?")
            if self.shop.check_item(item):
                if self.shop.get_price(item) <= self.profit:
                    if self.profit >= self.shop.get_price(item):
                        self.unlock_item(item)
                        self.shop.buy_item(item)
                        print("Thank you for your business!\n")
                else:
                    print("You can't afford this item.\n")
            else:
                print("We don't have this item.\n")
            # is this to execute run_shop again
        
        if player_in == "leave":
            print("Thanks for stopping by!\n")
    # Moved this method to the Game class and made small edits because it would 
    # be annoying to impleemnt otherwise


#Ethan Gustave's Function
    
from random import choice

def create_customers(num, customer_path):
    """Creates a list of customers from the amount specified for the day

    Args: 
	    num(int): the number of customers to be generated based on ad level.
	    customers_path(str): the path of the txt file to be used to import
            customer names.

    Returns: 
        A list of customer names.
    """
    
    with open(customer_path, 'r') as f:
        customer_start = f.readlines()
        
    customer_final = []
    indicies = []
    
    count = 0 
    while count < num:
        curr = choice(customer_start)
        if customer_start[curr] in indicies:
            count -= 1
        else:
            customer_final.append(curr)
            indicies.append(customer_start[curr])
        count += 1
       
    return customer_final


#Kyle Tice's Function

from random import shuffle

def handle_dish(current_dish, recipe_dict, customer_name):
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
    print(f"{customer_name} walked in!")
    print(f"\n Dish: {current_dish}")
    print("Ingredients (shuffled):")

    # builds the user-inputted list of ingredients
    for ingredient in shuffled:
        print(f"- {ingredient}")

    print("\nEnter the ingredients in the correct order:")

    user_list = []

    
    for i in range(len(correct_order)):
        user_input = input(f"Step {i+1}: ").strip()
        user_list.append(user_input)

    
    score = rate_dish(user_list, correct_order)
   

    print(f"\nYou scored: {score}/4")

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
    print("\n Ranked ingredients (best to worst):")
    for item in ranked:
        print(f"- {item}")

    # score based on correct position
    score = sum(
        1 for i in range(len(correct_list))
        if i < len(user_list) and user_list[i] == correct_list[i]
    )

    return score


def main(filepath, customerpath):
    game = Game(filepath)
    
    game.prompt_request(customerpath)
