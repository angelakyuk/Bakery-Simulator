# TO USE: python3 request_functions.py shop_data.JSON
import json
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
        self.owned_recipes = {"Sugar cookies":self.shopdata["Recipes"]["Sugar cookies"]}
        # self.owned_recipes = {r : self.shopdata["Recipes"][r] for r in self.recipes}
        self.ad_level = {"Level 1":self.shopdata["Ad Levels"]["Level 1"]}
        
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
                f"{'\n'.join(recipe_shop)}"
                '\n*Note: "Selling Price" is what your customers will pay.\n'
                f"\n------ Ad Level Shop ------\n"
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
            
    def day_end(self):
        """Display end of day stats and prompt player requests.

        Args:
            ad_level: player's current ad level.
            gross_profit: player's gross profit for the day.
        
        Side effects:
            Print to stdout.
        """
        tip_percent = random.uniform(0.05, 0.25)
        tip_amount = round(self.gross_profit * tip_percent, 2)
        net_profit = self.gross_profit + tips
        
        print("------ Today's Stats ------\n"
            f"Total customers: {self.ad_level}\n"
            f"Gross profit: ${round(self.gross_profit, 2)}\n"
            f"Tips: ${tips}\n"
            f"Net Profit: ${round(net_profit, 2)}\n"
            )
        self.prompt_request()

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