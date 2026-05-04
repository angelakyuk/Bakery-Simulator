from random import shuffle

def handle_dish(current_dish, recipe_dict):
    """

    Author: Kyle Tice
    
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


    score = rateDish(user_list, correct_order)

    print(f"\nYou scored: {score}/{len(correct_order)}")

    return score



def rateDish(user_list, correct_list):
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