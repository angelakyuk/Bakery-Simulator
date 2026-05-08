from numpy import random
from random import choice, shuffle
import json, argparse, time

class Shop:
    """Provide and update information about shop items.
    
    Attributes:
        shopdata (dict): A dictionary with the following keys:
            - "Recipes" (dict of {str:list[str]}): A dictionary of recipe 
                ingredients. Keys are recipe names. Values are a list of
                ingredients.
            - "Recipe prices" (dict of {str:int}): A dictionary of recipe 
                prices for the player. Keys are recipe names. Values are the
                corresponding price.
            - "Selling prices" (dict of {str:int}): A dictionary of selling
                prices of baked goods to customers. Keys are recipe names.
                Values are the corresponding selling price.
            - "Ad levels" (dict of {str:int}): A dictionary of ad level 
                information. Keys are ad levels. Values are the number of
                customers the player will serve at that level.
            - "Ad prices" (dict of {str:int}): A dictionary of ad level 
                prices. Keys are ad levels. Values are the corresponding price.
        recipes (list of str): A list of all recipe names.
        ad_levels (list of str): A list of all ad level titles.
        unlockable (dict of {str:str}): A dictionary of the lock status of shop
            items. Keys are recipe or ad level names. Values are "Locked" or
            "Owned".
        owned_recipes (dict of {str:list[str]}): A dictionary of recipes the
            player owns. Keys are recipe names. Values are the recipe's 
            ingredients.
        ad_level (dict of {str:int}): A dictionary of the player's current 
            ad level. The key is the ad level (e.g. "Level 1"). The value is
            the number of customers they will serve.
        recipe_shop (dict of {str:tuple(int, int)}): A dictionary of recipe
            shop information. Keys are recipe names. Values are tuples of the
            recipe's price for the player and selling price to customers.
        ad_shop (dict of {str:tuple(int, int)}): A dictionary of ad level shop
            information. Keys are ad level titles (e.g. "Level 1"). Values are 
            tuples of the level's price and the number of customers to serve.
    """
    def __init__(self, shop_path):
        """Initialize ShopData object.
        
        Author: Angela Kyuk
        Technique: Comprehensions (list, dictionary).
        
        Args:
            shop_path: A path to a JSON file that has shop information.
        
        Side effects:
            Sets attributes shopdata, recipes, ad_levels, all_shop, unlockable, 
                owned_recipes, ad_level, recipe_shop, and ad_shop.
        """
        with open(shop_path, 'r') as f:
            self.shopdata = dict(json.load(f))
        
        self.recipes = [r for r in self.shopdata["Recipes"]]
        self.ad_levels = [a for a in self.shopdata["Ad levels"]]
        self.all_shop = self.recipes + self.ad_levels
        
        self.unlockable = {i : "Locked" for i in self.all_shop}
        self.unlockable["Sugar cookies"] = "Owned"
        self.unlockable["Level 1"] = "Owned"
        self.owned_recipes = {"Sugar cookies":
                              self.shopdata["Recipes"]["Sugar cookies"]}
        self.ad_level = {"Level 1":
                         self.shopdata["Ad levels"]["Level 1"]}
        
        self.recipe_shop = {r : (self.shopdata["Recipe prices"][r], 
                                 self.shopdata["Selling prices"][r]) 
                            for r in self.recipes}
        self.ad_shop = {a : (self.shopdata["Ad prices"][a], 
                             self.shopdata["Ad levels"][a]) 
                        for a in self.ad_levels}
        
    def __str__(self):
        """Provide an informal string representation for the game's shop.

        Author: Angela Kyuk
        Technique: Magic method that's not __init__.
        
        Returns:
            str: The informal representation of the game's shop, which includes
                the item's name, purchase price, selling price to customers or 
                number of customers to serve, and lock status.
        """
        recipe_shop = [f"\n{r}:\n${round(p[0], 2)} (P) * ${round(p[1], 2)} (S) * {self.unlockable[r]}" 
                       for r, p in self.recipe_shop.items()]
        ad_shop = [f"\n{a}:\n${round(i[0], 2)} (P) * {i[1]} (C) * {self.unlockable[a]}"
                   for a, i in self.ad_shop.items()]
        return (f"\n------ Recipe Shop ------\n"
                f"Recipe Price (P) | Selling Price (S) | Lock Status\n"
                '*Note: "Selling Price" is what your customers will pay.\n'
                f"{'\n'.join(recipe_shop)}"
                f"\n\n------ Ad Level Shop ------\n"
                f"Level Price (P) | Customers (C) | Lock Status\n"
                '*Note: You can only own one ad level. If you buy a new one, the rest will be locked.\n'
                f"{'\n'.join(ad_shop)}"
        )
        
    #Shop methods below by Ethan Gustave
    def get_price(self, item_name):
        """Gets price of item given the item's name.
        
        Args: 
            item_name (str): The name of the item whose price is to be checked.
            
        Returns: 
            int: The purchase price of the item.
        """
        return(self.recipe_shop(item_name[1]))
        ## will this be used for only recipes? if not, consider this code
        # if item in self.recipes:
            # return self.recipe_shop[item][0]
        # elif item in self.ad_levels:
            # return self.ad_shop[item][0]
    
    def owned(self, item_name):
        """Checks if item is owned.
            
        Args:
            item_name (str): The name of the item to be checked.
        
        Returns:
            Bool: True if item is owned. False if item is not owned.
            """
        if self.unlockable[item_name] == "Owned":
            return True
        else:
            return False
        # return True if self.unlockable[item] == "Owned" else False ?
            ## conditional expr equiv to whole conditional statement (if it's right)
        
    def check_item(self, item_name):
        """Checks if item request is valid. 
            
        Args:
            item_name (str): The name of the item to be bought.
            
        Returns:
            Bool: True if item is valid. False if item is invalid.
            """
        if item_name in self.recipe_shop:
            return True
        else:
            return True if item_name in self.ad_shop else False
        # return True if item in self.all_shop else False
            ## all_shop has the names of all shop items. ^ conditional expr is equiv 
            ## to the entire conditional statement (if it's right)
    
    def buy_item(self, item_name):
        """Attempts to buy an item from the shop.
        
        Args:
            item_name (str): The name of the item to be bought
                        
        Returns:
            Bool: True if the item is bought. False if the item name isn't valid 
                or the item is already unlocked.
                
        Side Effects: 
            Prints to console depending on result of method.
            Changes the value of an item in the dictionary unlockable from 
                "Locked" to "Owned" if the item is bought.
            # Modifies attributes owned_recipes or ad_level if the item is bought. (if we move these)
        """
        
        if item_name in self.unlockable:
            if self.unlockable[item_name] == "Owned":
                pass
            else:
                if item_name in self.recipes:
                    self.unlockable[item_name] == "Owned"
                    self.owned_recipes[item_name] == self.shopdata["Recipes"][item_name]
                        ## added owned_recipes to Shop
                if item_name in self.ad_levels:
                    self.unlockable["Level 1"] = "" # for a in self.ad_levels:
                    self.unlockable["Level 2"] = "" #     self.unlockable[a] = "" ## OR "Locked" (check note in __str__ for context)
                    self.unlockable["Level 3"] = "" # self.unlockable[item_name] = "Owned"
                    self.unlockable[item_name] = "Owned"
                    self.ad_level.clear()     ## so that there's only one value for current ad level
                    self.ad_level[item_name] == self.shopdata["Ad levels"][item_name]
                        ## added ad_level to Shop
                        ## or we could remove owned_recipes and ad_level entirely and use self.unlockable

                    ## what would buy_item print to stdout?

class Game:
    """Play Bakery Simulator.
    
    Attributes:
        customers (list of str): A list of possible customer names.
        shop (Shop): The instance of Shop used in this game.
        profit (int): The total amount of money the player currently has.
    """
    def __init__(self, shop_path, customer_path):
        """Initialize Game object.
        
        Author: Angela Kyuk
        
        Args:
            shop_path (str): A path to a JSON file containing shop information.
            customer_path (str): A path to a txt file containing possible 
                customer names
                    
        Side effects: 
            Sets attributes customers, shop, and profit.
        """
        with open(customer_path, 'r') as f: # should we add encoding?
            self.customers = f.readlines()
            
        self.shop = Shop(shop_path)
        # self.owned_recipes = {"Sugar cookies":self.shop.shopdata["Recipes"]
        #                       ["Sugar cookies"]}
        # self.ad_level = {"Level 1":self.shop.shopdata["Ad levels"]["Level 1"]}
        self.profit = 0
        
    def unlock_item(self, item_name):
        """Unlocks an item.
        
        Args: 
            item_name (str): the name of the item to be unlocked.
            
        Side Effects:
            Modifies owned_recipes and ad_level attributes.
        """
        if item_name in self.shop.shopdata["Recipes"]:
            self.owned_recipes[item_name] = self.shop.shopdata["Recipes"][item_name]
        elif item_name in self.shop.shopdata["Ad levels"]:
            self.ad_level = {item_name : self.shop.shopdata["Ad levels"][item_name]}
    ## can remove this function if we add owned_recipes and ad_level to Shop
            
    def valid_request(self, request):
        """Ensure that the player's input for a menu option request is valid.
    
        Args:
            request (str): The player's input when asked if they want a certain 
                menu option.
    
        Returns:
            str: The player's input if it's valid or "invalid" if the input is 
                invalid.
        """
        if not isinstance(request, str):
            return 'invalid'
        else:
            if request in ('shop', 'recipes', 'continue', 'end game'):
                return request
            else:
                return 'invalid'
            
    def fulfill_request(self, request):
        """Carry out the player's menu option request.
        
        Author: Angela Kyuk
    
        Args:
            request (str): The player's menu option request.
    
        Side effects:
            Prints to stdout.
            Modifies attributes if the player purchases an item in run_shop.
            Terminates program if the player inputs "end"
        """
        if request == 'recipes':
            # recipes = [f"{r}: {self.owned_recipes[r]}" 
            #            for r in self.owned_recipes]
            recipes = [f"\n{r}: {self.shop.owned_recipes[r]}" 
                       for r in self.shop.owned_recipes]
            ## ^ if we add owned_recipes to Shop
            
            # recipes = [f"{r}: {self.shop.shopdata["Recipes"][r]}" 
            #            for r in self.shop.recipes 
            #            if self.shop.unlockable[r] == "Owned"]
                ## ^ if we remove owned_recipes
            print("------ Your Recipes ------\n"
                f"{'\n'.join(recipes)}\n")
        elif request == 'shop':
            print(self.shop)
            self.run_shop()
        elif request == 'continue':
            self.day_profit()
        elif request == 'end':
            print("Thanks for playing!")
            quit()
            
    def prompt_request(self):
        """Prompt player for menu option requests and carry them out.
        
        Author: Angela Kyuk
    
        Side effects:
            Prints to stdout.
            Modifies certain attributes if player purchases an item.
        """
        menu_options = ("\n------ Menu Options ------\n"
                    "[recipes] to review your recipes\n"
                    "[shop] to browse the shop\n"
                    "[continue] to continue to the next day\n"
                    "[end] to end the game\n"
                    )
        request = input(menu_options)
        validated = self.valid_request(request.lower())
        while validated == 'invalid':
            print("That's not a valid menu option. Try again!")
            request = input(menu_options)
            validated = self.valid_request(request.lower())
        self.fulfill_request(validated)
        more = input("Would you like to select another menu option? (Y/N). ")
        while more.lower() not in ('y', 'n'):
            print("That's not a valid option. Try again!")
            more = input("Would you like to select another menu option? (Y/N). ")
        if more.lower() == 'y':
            self.prompt_request()
        elif more.lower() == 'n':
            self.fulfill_request('continue')
    
    def day_profit(self, show_stats=True, expense_rate=None):
        """Calculate daily profit, expenses, and total profit.
        
        Args:
            show_stats (bool): Method does nothing if False. Method executes as 
                normal if True. Defaults to True.
            expense_rate (None or int): A set amount of money going towards 
                expenses.
                
        Returns:
            None: If show_stats is False
            
        Side effects:
            Prints to stdout if show_stats is True.
            Modifies attribute profit.
        """
        if not show_stats:
            return None
        # current_level = list(self.ad_level)[0]
        current_level = list(self.shop.ad_level)[0] 
            ## if we move ad_level to Shop
        num_customers = self.shop.shopdata["Ad levels"][current_level]
        customers = self.create_customers(num_customers)
        revenue = 0
            
        for c in customers:
            # current_dish = choice(list(self.owned_recipes)) ## owned_recipes in Shop
            current_dish = choice(list(self.shop.owned_recipes))
            price = self.shop.shopdata["Selling prices"][current_dish]
            # score = handle_dish(current_dish, self.owned_recipes, c) ## owned_recipes in Shop
            score = handle_dish(current_dish, self.shop.owned_recipes, c)
            revenue += (price * (score / 2))
            revenue += ((price * choice(self.shop.shopdata["Order amounts"])) 
                        + (score)/2) ## added order amounts from JSON file
            ## changed selling_price to price to make it a line under 80 chars {crying emoji}

        if expense_rate is None:
            expense_rate = random.rand() * 0.25
        expenses = round(revenue * expense_rate, 2)
        daily_profit = round(revenue - expenses, 2)
        self.profit += daily_profit

        print("------ Today's Stats ------\n"
            f"Customers served: {len(customers)}\n"
            f"Revenue: {round(revenue, 2)}\n"
            f"Expenses: {expenses}\n"
            f"Daily profit: {daily_profit}\n"
            f"Total profit: {round(self.profit, 2)}\n"
        )
        self.prompt_request()
    
    def run_shop(self):
        """
        """
        print("\nWhat would you like to do?")
        player_in = input("[buy] to buy an item\n[leave] to leave shop\n")
        while player_in not in ('buy', 'leave'):
            player_in = input("That's not a valid input. Try again! ")
        if player_in == "buy":
            item = input("What would you like to purchase? ").capitalize() ##
            while item not in self.shop.all_shop:
                item = input("That's not a shop item. Try again! ").capitalize()
                ## ^ this does what check_item does but gives user unlimited retries
            if self.shop.check_item(item): # <
                if self.shop.get_price(item) <= self.profit:
                    if self.profit >= self.shop.get_price(item):
                        self.unlock_item(item)
                        self.shop.buy_item(item)
                        print("Thank you for your business!\n")
                else:
                    print("You can't afford this item.\n")
            # if self.shop.check_item(item):
            #     if self.shop.get_price(item) <= self.proft:                   if item price is less than or equal to profit...
            #         self.shop.buy_item(item)                                  *(if we remove unlock_item)
            #         print("Thank you for your business!\n")
            #     elif self.shop.get_price(item) > self.profit:                 if item price is greater than profit...
            #         print("You can't afford this item.\n")
            # else:
            #     print("We don't have this item.\n") ## what 'while item not in shop' does
        elif player_in == "leave":
            print("Thanks for stopping by!\n")
            self.prompt_request() ## go back to menu options ?
            
    def start(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        print("\nWelcome to Bakery Simulator!\n")
        print("Your job is to type ingredients in the correct order, given a scrambled recipe. ")
        print("The more ingredients you get right, the higher your score and tips. ")
        print("To learn more about how to play, check the README.md file!\n")
        start = input("Press enter to start baking :D\n")
        if start or not start:
            time.sleep(.5)
            print("﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
            self.day_profit()
#Ethan Gustave's Function

    def create_customers(self, num):
        """Creates a list of customers from the amount specified for the day

        Args: 
            num(int): the number of customers to be generated based on ad level.
            customers_path(str): the path of the txt file to be used to import
                customer names.

        Returns: 
            customer_final (list): A list of customer names.
        """ 
        customer_final = []
        indices = []
        
        count = 0 
        while count < num:
        #     curr = choice(self.customers).strip()
        #     customer_final.append(curr)
        #     count += 1
        # return customer_final
            
            curr = choice(self.customers).strip()

            if curr not in indices:
                customer_final.append(curr)
                indices.append(curr)
                count += 1
            else:
                customer_final.append(curr)
                indices.append(self.customers[curr])
            #count += 1
        
        return customer_final


#Kyle Tice's Function

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
    # defines the correct order of ingredients
    correct_order = recipe_dict[current_dish]
    
    shuffled = correct_order[:]
    shuffle(shuffled)
    print(f"{customer_name} walked in!")
    print(f"\nDish: {current_dish}")
    print("Ingredients (shuffled):")

    # builds the user-inputted list of ingredients
    for ingredient in shuffled:
        print(f"- {ingredient}")

    print("\nEnter the ingredients in the correct order:")

    user_list = []

    
    for i in range(len(correct_order)):
        user_input = input(f"Step {i+1}: ").strip()
        user_list.append(user_input)
        if user_input == 'q':
            quit()

    print("Cooking...\n")
    time.sleep(.5)
    print("Done!")
    time.sleep(.5)
    score = rate_dish(user_list, correct_order)
    print(f"\nYou scored: {score}/4\n")

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
    print("\nRanked ingredients (best to worst):")
    for item in ranked:
        print(f"- {item}")

    # score based on correct position
    score = sum(
        1 for i in range(len(correct_list))
        if i < len(user_list) and user_list[i] == correct_list[i]
    )

    return score


def main(shop_path, customer_path, expense_rate=None):
    game = Game(shop_path, customer_path)
    game.day_profit(False, customer_path)
    game.start()
    
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("shop_path")
    parser.add_argument("customer_path")
    parser.add_argument("--expense-rate", type=float, default=None)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    main(args.shop_path, args.customer_path, args.expense_rate)
    
# python3 simulator_main.py shop_data.JSON customers.txt 