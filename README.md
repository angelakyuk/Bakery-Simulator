# Bakery-Simulator:
This is a text-based bakery simulator game. Your goal is to type ingredients in 
the right order, given a scrambled recipe, in order to get tips from customers.
You'll be able to purchase ad levels, which increase the number of customers you 
serve, and recipes, which have higher base selling prices. There's no set end of 
this game, but you can end the game when you're at the menu or during baking 
(see: Menu Options).

## A Run-Down
### Start
When you start the game, you'll be greeted with a welcome text. To start baking, 
press enter. You'll start at ad level 1, meaning you'll serve 3 customers, with 
a recipe for sugar cookies. To learn more about ad levels and recipes, check out 
shop_data.JSON.

### Baking
For every customer you serve, you'll see their order amount and recipe. You'll 
be given a scrambled recipe that you need to enter in the right order. When 
you're done, your recipe will be ranked from correct to incorrect and you'll get 
a score. This score is used to determine your tips, which will be added to your 
revenue. If you want to end the game while baking, enter 'q'

### End of Day
At the end of the day, which is after you've served all customers, you'll see 
your daily stats. This includes number of customers served, tips, revenue, 
expenses, daily profit, and total profit. You'll also get to choose some menu 
option.

### Determining Profit
**Tips**: Each order's score divided by 2.

**Revenue**: Profit from the day's orders, including tips. Each order's profit 
is the baked good's selling price multiplied by the order amount.

**Expenses**: If an argument is given for the optional parameter `expense_rate`, 
that'll be applied to revenue. Otherwise, a random percentage will be generated.

**Daily profit**: Revenue minus expenses.

**Total profit**: Daily profit added up.

### Menu Options
**Recipes**: See the name and ingredients of recipes you own.

**Shop**: The shop will be printed and you'll be asked if you want to buy an 
item or leave. After buying an item, you can buy another item or leave the shop. 
If you want to leave the shop while in 'buy', enter 'q' to go back to the main 
menu.

**Continue**: Continue to the next day.

**End**: End the game.

After choosing a menu option, you will be asked if you want to select another 
one. If you enter 'y', the menu will reprint. If you enter 'n', the game will 
continue to the next day.

### Inputs
You'll be able to re-enter requests an unlimited amount of time

# How to run Bakery Simulator
Required Files:
* simulator_main.py
* shop_data.JSON
* customers.txt

Optional Command Line Arguments
* --expense-rate 
To play the game, enter the files simulator_main.py, shop_data.JSON, customers.txt (e.g. python3 simulator_main.py shop_data.JSON customers.txt).
It's optional but if you want to enter an expense_rate you can add the command --expense-rate $rate at the end. (e.g. python3 simulator_main.py shop_data.JSON --expense-rate 0.25)

User input notes: 
* Entering "n" when asked if you want another menu option automatically starts the next round.
* Inputs are case insensitive and unlimited retries.

# Files
## Project Files
**LICENSE**: An MIT license for this project.

**customers.txt**: A text file containing possible customer names.

**shop_data.JSON**: A JSON file containing game data.

**simulator_main.py**: The main game file that contains all necessary classes and 
functions to run Bakery Simulator.

## Project Draft Files
**create_customers.py**: Ethan Gustave's draft of the create_customers function.

**game_demo.py**: Presentation live demo. Starts at menu option, allows game play, 
and ends with daily stats (draft) and another menu option prompt.

**handle_dish.py**: Kyle Tice's draft of the handle_dish and rate_dish functions.

**handle_unlocks.py**: Sarayu Vanam's draft of the handle_unlocks function.

**personal.py**: All of Angela Kyuk's function and class drafts/brainstorms.

**request_functions.py**: Angela Kyuk's drafts of valid_request, fulfill_request, 
prompt_request, and day_end functions.

**shop.py**: Draft of the Shop class. First draft written by Ethan Gustave. Second
draft written by Angela Kyuk and edited by Ethan Gustave.

## Non-Project Files
**collab_exercise.txt**: The file submitted for "Exercise: Collaborative programming".

# Attribution Table
|  Method/Function | Primary Author | Technique Demonstrated |
| ---------------  | -------------- | ---------------------- |
| `day_profit`     | Sarayu Vanam   | Optional parameters    |
| `parse_args`     | Sarayu Vanam   | ArgumentParser         |
| `__str__`        | Angela Kyuk    | Magic method that's not `__init__` |
| `__init__` (Shop)| Angela Kyuk    | Comprehensions|
| `owned`          | Ethan Gustave  | Conditional expression | 
| `create_customer`| Ethan Gustave  | `with` statement       |
| `handle_dish`    | Kyle Tice      | f-string containing an expression |
| `rate_dish`      | Kyle Tice      | key function (lambda) with sorted |


# Annotated Bibliography
Built-in Types. (n.d.). Python Documentation. Retrieved May 5, 2026, from https://docs.python.org/3/library/stdtypes.html

This is the official Python website that has descriptions and tutorials for 
built-in types. I used this website to learn more about the .join() string method
and case manipulation, specifically .capitalize().

How to format numbers as currency strings in Python. (18:42:30+00:00). GeeksforGeeks. https://www.geeksforgeeks.org/python/how-to-format-numbers-as-currency-strings-in-python/

This website has tutorials for several coding languages. I used this website to 
learn how to format numbers as currency, particularly how to always have two decimal points

Python Join Two Lists. (n.d.). Retrieved May 5, 2026, from https://www.w3schools.com/python/gloss_python_join_lists.asp

This website has tutorials for several coding languages. I used this website to 
recall how to set a variable to two concatenated lists using `+`.