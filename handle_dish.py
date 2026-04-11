import random

def handle_dish(current_dish, difficulty, recipe_dict):
    """
    Handles the playing stage of each dish by giving inputs to the user. Their
    performance is decided by the order in which the ingredients are typed.

    Args: 
        current_dish (String): the current food dish being made
        recipe_dict (dict): dictionary of foods and associated ingredient lists

    Side Effects:
        Prompts user for extra inputs (active game stage)
    
    Returns:
        None
    """

    
    correct_order = recipe_dict[current_dish]

    
    shuffled = correct_order[:]
    random.shuffle(shuffled)

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