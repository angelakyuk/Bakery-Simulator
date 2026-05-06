# Bakery-Simulator
A text-based bakery simulator game.

# How to run Bakery Simulator
To play the game, enter the files simulator_main.py and shop_data.JSON (e.g. python3 simulator_main.py shop_data.JSON).

User input notes: 
* Entering "n" when asked if you want another menu option automatically starts the next round.
* Inputs are case insensitive and unlimited retries.

# Files
### Project Files
**LICENSE**: An MIT license for this project.

**customers.txt**: A text file containing possible customer names.

**shop_data.JSON**: A JSON file containing game data.

**simulator_main.py**: The main game file that contains all necessary classes and 
functions to run Bakery Simulator.

### Project Draft Files
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

### Non-Project Files
**collab_exercise.txt**: The file submitted for "Exercise: Collaborative programming".

# Attribution
|  Method/Function | Primary Author | Technique Demonstrated |
| ---------------  | -------------- | ---------------------- |
| `day_profit`     | Sarayu Vanam   | Optional parameters     |
| `parse_args`     | Sarayu Vanam   | ArgumentParser class from argparse module |
| `__str__`        | Angela Kyuk    | Magic method that's not `__init__` |
| `__init__` (Shop)| Angela Kyuk    | Comprehensions|
| `check_item`     | Ethan Gustave  | Conditional expression | 
| `create_customer`| Ethan Gustave  | `with` statement       |
| `handle_dish`    | Kyle Tice      | f-string containing an expression |
| `rate_dish`      | Kyle Tice      | key function (lambda) with sorted |


# Annotated Bibliography
Built-in Types. (n.d.). Python Documentation. Retrieved May 5, 2026, from https://docs.python.org/3/library/stdtypes.html

This is the official Python website that has descriptions and tutorials for 
built-in types. I used this website to learn more about the .join() string method
and case manipulation, specifically .capitalize().

Python Join Two Lists. (n.d.). Retrieved May 5, 2026, from https://www.w3schools.com/python/gloss_python_join_lists.asp

This website has tutorials for several coding languages. I used this website to 
recall how to set a variable to two concatenated lists using `+`.