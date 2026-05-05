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
        ad_levels (list of str): A list of all ad levels.
        unlockable (dict of {str:str}): A dictionary of the lock status of shop
            items. Keys are recipe or ad level names. Values are "Locked",
            "Owned", or an empty string "".
        recipe_shop (dict of {str:tuple(int, int)}): A dictionary of recipe
            shop information. Keys are recipe names. Values are tuples of the
            recipe's price for the player and selling price to customers.
        ad_shop (dict of {str:tuple(int, int)}): A dictionary of ad level shop
            information. Keys are the ad level. Values are tuples of the level's 
            price for the player and the number of customers they'll serve at 
            that level.
    """
    def __init__(self, shop_path):
        """Initialize ShopData object.
        
        Args:
            shop_path: The path to the file which populates the ShopData object.
            ### is this the JSON file that has shop data?
            ### shop_path: The path to the JSON file that has the game's shop information.
        Side effects:
            Set attributes shopdata, recipes, ad_levels, unlockable, recipe_shop, 
                and ad_shop.
        """
        with open(shop_path, 'r') as f:
            self.shopdata = json.load(f)
            self.shopdata = dict(self.shopdata)
            # turned JSON file into dict
        
        self.recipes = [r for r in self.shopdata["Recipes"]]
        self.ad_levels = [a for a in self.shopdata["Ad levels"]]
        self.owned_recipes = {self.recipes[0]} # <
        self.ad_level = {self.ad_levels[0]} # <
        # i think we should keep these two in Game so that this class has general shop
        # info and Game has the player's stats, like owned recipes/ad level and their profit
        all_shop = self.recipes.extend(self.ad_levels)
        self.unlockable = {i : "Locked" for i in all_shop}
        self.unlockable["Sugar cookies"] = "Owned"
        self.unlockable["Level 1"] = "Owned"
        self.recipe_shop = {r : (self.shopdata["Recipe prices"][r], 
                                 self.shopdata["Selling prices"][r]) 
                            for r in self.recipes}
        self.ad_shop = {a : (self.shopdata["Ad prices"][a], 
                             self.shopdata["Ad levels"][a]) 
                        for a in self.ad_levels}
        
    def __str__(self):
        """Provide an informal string representation for the game's shop, which
        includes recipes and ad levels.

        Returns:
            str: The informal representation of the game's shop.
        """
        recipe_shop = [f"{r} | {prices[0]} | {prices[1]} | {"Owned" if r in 
                       self.owned_recipes else "Locked"}" 
                       for r, prices in self.recipe_shop.items()]
        ad_shop = [f"{a} | {prices[0]} | {prices[1]} | {"Current" if a in 
                   self.ad_level.keys() else ""}"
                   # self.ad_level is the player's current ad level
                   for a, prices in self.ad_shop.items()]
        return (f"------ Recipe Shop ------\n"
                f"Recipe | Purchase Price | Selling Price | Lock Status\n"
                f"{recipe_shop.join('\n')}"
                '*Note: "Selling Price" is what your customers will pay.\n'
                f"------ Ad Level Shop ------\n"
                f"Ad Level | Purchase Price | Customers | Lock Status"
                f"{ad_shop.join('\n')}"
                #'''*Note: "Customers" is how many customers you'll serve in'''
                #'''a day.\n'''
        )
        
    #Shop methods below by Ethan Gustave
    
    def owned(self, item_name):
        """Checks if item is owned.
            
            Takes: ### Args?
                item_name: the name of the item to be checked
            Returns:
                True if item is owned, otherwise returns False.
                # Bool: ?
            """
        if(self.unlockable[item_name] == "Owned"):
        # if self.unlockable[item_name] == "Owned":
            return True
        else:
            return False
        
    def check_item(self, item_name):
        """Checks if item request is valid. 
            
            Takes: ### Args?
                item_name: the name of the item to be bought
            Returns:
                True if valid, otherwise returns False.
                # Bool?
            
            """
        if(item_name in self.recipe_shop):
        # if item_name in self.recipe_shop:
            return True
        elif(item_name in self.ad_shop):
            return True
        else:
            return False
    
    def buy_item(self, item_name):
        """Attempts to buy an item from the shop.
        
        Takes: ### Args?
            item_name: the name of the item to be bought
        Returns:
            True: If the item is bought
            False: if the item name isn't valid or the item is already unlocked.
            # Bool?
        Side Effects: 
            - Prints to console depending on result of method
            - Changes unlockable dictionary entry from "Locked" to "Owned" if
                item is bought.
                ### Changes the value of an item in the dictionary unlockable 
                ### from "Locked" to "Owned" if the item is bought?
        
        """
        
        if(item_name in self.unlockable):
        # if item_name in self.unlockable:
            if(self.unlockable[item_name] == "Owned"):
            # if self.unlockable[item_name] == "Owned":
                print("You already own this!\n")
                return False
            else:
                self.unlockable[item_name] == "Owned"
                # will we add sarayu's handle_unlocks function to make sure 
                # player has enough money?
                print("Thank you for your business!")
                return True
        else:
            print("We don't have this item.")
            return False

class Game:
    """GameState
    
    Attributes:
            owned_recipes (dict of {str:list[str]}): A dictionary of recipes the
                player owns. Keys are recipe names. Values are the recipe's 
                ingredients.
            ad_level (dict of {str:int}): A dictionary of the player's current 
                ad level. The key is the ad level (e.g. "Level 1"). The value is
                the number of customers they will serve.
            profit (int): How much money the player currently has.
    """
    def __init__(self, gamedata):
        """_summary_

        Args:
            gamedata (str): A filepath to a JSON file with game data.
                    
        Side effects: Sets attributes owned_recipes, ad_level, and profit.
        """
        self.owned_recipes = {self.recipes[0]}
        self.ad_level = {self.ad_levels[0]}
        self.profit = 0
        
    def valid_request(self, request):
        """Ensure that the player's input for a menu option request is valid.
    
        Args:
            request (str): The player's input when asked if they want a certain 
                menu option.
    
        Returns:
            str: The player's input if it's valid. If the input is invalid, 
                returns 'invalid'.
        """
        valid_requests = ('shop', 'recipes', 'continue', 'end game')
        if not isinstance(request, str):
            return 'invalid'
        else:
            if request in valid_requests:
                return request
            else:
                return 'invalid'
            
    def fulfill_request(self, request):
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
                f"{recipes.join('\n')}")
        elif request == 'shop':
        # shop function
            pass
        elif request == 'continue':
        # start new day function
            pass
        elif request == 'end game':
            print("Thanks for playing!")
            quit()
            
    def prompt_request(self):
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
        self.fulfill_request(validated)
        more = input("Would you like to select another menu option? (Y/N). ")
        while more.lower() not in ('y', 'n'):
            print("That's not a valid option. Try again!")
            more = input("Would you like to select another menu option? (Y/N). ")
        if more.lower() == 'y':
            self.prompt_request()
        elif more.lower() == 'n':
            self.fulfill_request('continue')
            
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
          f"Expenses: ${expenses}\n"
          f"Current profit: ${round(self.profit - expenses, 2)}\n"
          )
        self.prompt_request()

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

    for name, i in recipes.items():
        i["unlocked"] = True if money >= i["price"] else i["unlocked"] = False

    return recipes

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


def main(filepath):
    game = Game(filepath)