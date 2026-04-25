import json

class Shop:
    
    def __init__(self, shop_path):
        
        with open(shop_path, 'r') as f:
            shop_data = json.load(f)
        
        self.recipe_stock = list(shop_data["Recipies"])
        self.recipe_prices = list(shop_data["Recipe prices"].values())
        
        self.ad_stock = list(shop_data["Ad level"])
        self.ad_prices = list(shop_data["Ad prices"].values())
        
    def buy_item(self, item_name):
        """Checks if item is able to be bought. 
            
            Takes:
                item_name: the name of the item to be bought
            Returns:
                True & removes item if valid, otherwise returns false.
            
            """
        if(item_name in self.recipe_stock):
            item_index = self.recipe_stock.index(item_name)
            self.recipe_stock.pop(item_index)
            self.recipe_prices.pop(item_index)
            return True
        elif(item_name in self.ad_stock):
            item_index = self.ad_stock.index(item_name)
            self.ad_prices_stock.pop(item_index)
            self.ad_prices.pop(item_index)
            return True
        else:
            return False
        
    def display_stock(self):
        print("Welcome in! How can I help you?\n")
        print("Recipies: \n")
        
        for i in self.recipe_stock:
            print(f"""{i}\t
                  Price: {self.recipe_prices[self.recipe_stock.index(i)]}""")
        print("\nUpgrades:")
        for i in self.ad_stock:
            print(f"""{i}\t
                  Price: {self.ad_prices[self.ad_stock.index(i)]}""")
            
        
        
        
        
        
    