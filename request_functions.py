def valid_request(self, request):
    """Ensure that the player's input for a menu option request is valid.

    Args:
        request (str): player's input when asked if they want a certain menu 
        option.

    Returns:
        str: the player's input if it's valid. If input is invalid, 'invalid'.
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
    """Carry out player's menu option request.

    Args:
        request: player's menu option request.

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
        ad_level: player's current ad level.
        gross_profit: player's gross profit for the day.
    
    Side effects:
        Print to stdout.
    """
    expenses = round(self.gross_profit * random.rand(), 2)
    print("------ Today's Stats ------\n"
        f"Total customers: {self.ad_level}\n"
        # show ad level?
        f"Gross profit: ${round(self.gross_profit, 2)}\n"
        f"Expenses: ${expenses}\n"
        f"Net Profit: ${round(self.gross_profit - expenses, 2)}\n"
        )
    self.prompt_request()