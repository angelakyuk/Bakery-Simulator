import json
from personal import Shop

class Shop:
    """Provide and update information about shop items.
    
    Attributes:
        recipe_shop (dict of {str:tuple(int, int)}): A dictionary of recipe
            shop information. Keys are recipe names. Values are tuples of the
            recipe's price for the player and selling price to customers.
        ad_shop (dict of {str:tuple(int, int)}): A dictionary of ad level shop
            information. Keys are the ad level. Values are tuples of the level's 
            price for the player and the number of customers they'll serve at 
            that level.
        unlockable (dict of {str:str}): A dictionary of the lock status of shop
            items. Keys are recipe or ad level names. Values are "Locked",
            "Owned", or and empty string "".
        gamedata (dict): A dictionary with the following keys:
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
    """
    def __init__(self, shop_path):
        
        """Initialize ShopData object.
        Args:
            shop_path: The path to the file which populates the ShopData object.
        Side effects:
            Set attributes unlockable, recipe_shop, and ad_shop.
        """
        
        with open(shop_path, 'r') as f:
            shopdata = json.load(f)
        
        self.recipes = [r for r in shopdata["Recipes"]]
        self.ad_levels = [a for a in shopdata["Ad levels"]]
        self.owned_recipes = {self.recipes[0]}
        self.ad_level = {self.ad_levels[0]}
        
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
        
        # Old Code, may pull from later
        """ with open(shop_path, 'r') as f:
            shop_data = json.load(f)
        
        self.recipe_stock = list(shop_data["Recipies"])
        self.recipe_prices = list(shop_data["Recipe prices"].values())
        
        recipes = []
        
        self.ad_stock = list(shop_data["Ad level"])
        self.ad_prices = list(shop_data["Ad prices"].values())"""
        
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
                   self.owned else " "}"
                   for a, prices in self.ad_shop.items()]
        return (f"------ Recipe Shop ------\n"
                f"Recipe | Purchase Price | Selling Price | Lock Status\n"
                f"{recipe_shop.join('\n')}"
                '*Note: "Selling Price" is what your customers will pay.\n'
                f"------ Ad Level Shop ------\n"
                f"Ad Level | Purchase Price | Customers | Lock Status"
                f"{ad_shop.join('\n')}"
                #'''*Note: "Customers" is how many customers you'll serve in a'''
                #'''day.\n'''
        )
        
    def check_item(self, item_name):
        """Checks if item request is valid. 
            
            Takes:
                item_name: the name of the item to be bought
            Returns:
                True & removes item if valid, otherwise returns false.
            
            """
        if(item_name in self.recipe_shop):
            return True
        elif(item_name in self.ad_shop):
            return True
        else:
            return False
    
    

            
        
        
        
        
        
    