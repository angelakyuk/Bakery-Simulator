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
