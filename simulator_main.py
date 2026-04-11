def valid_request(request):
    """Ensure that the player's input for a menu option is valid.
    """
def fulfill_request(request):
    """Carry out the player's menu option request.
    """  
def prompt_request():
    """Prompt player for menu option requests, validate those requests and 
    fulfill them."
    
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
    validated = valid_request(request.lower())
    while validated == 'invalid':
        print("That's not a valid menu option. Try again!")
        request = input(menu_options)
        validated = valid_request(request.lower())
    fulfill_request(validated)
    more = input("Would you like to select another menu option? (Y/N). ")
    while more.lower() != 'y' and more.lower() != 'n':
        print("That's not a valid option. Try again!")
        more = input("Would you like to select another menu option? (Y/N). ")
    if more.lower() == 'y':
        prompt_request()
    elif more.lower() == 'n':
        fulfill_request('continue')