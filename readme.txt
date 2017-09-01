This is a text-based game I created for two projects for a class I took on Python. I have worked on it a bit since. Below is the README that was submitted with the project submission; however, it does not necessarily reflect the changes I have made since.

----------------------------------

The Destroyer's Destiny
    A Game by Vishnu Nair
    CSC 11300 Projects 1 & 2

To start the game, run the file "launch.py".

.py files included with the game:
    * battle.py - handles the battle mechanic
    * dungeon.py - handles the dungeon mechanic
    * exit.py - handles the game exit sequence as well as saving the game
    * game.py - holds the main game loop/sequence
    * globals.py - holds all globals variables and functions that will be referenced by every other module in the game
    * home_screen.py - handles the home screen
    * launch.py - the game launch module
    * player.py - handles the player class
    * shop.py - handles the shop mechanic
    * sidequest.py - handles the sidequest mechanic
    * start_state.py - handles the start sequence for the game
    * terminal.py - handles the terminal sequence
    * center_square.py [NEW] - handles the minigames/activities associated with Center Square
    * date.py [NEW] - handles the date mechanic
    * outside,py [NEW] - contains the definition for the city class and handles the player's city traversal
    * weather.py [NEW] - handles the weather mechanic

Other data files:
    * caves_hideaways.txt - holds names for dungeons for the sidequest mechanic
    * dialogue.csv - holds all dialogue, dialogue types, and stage jump targets
    * loot.csv - holds all loot names and their values
    * main_enemies.txt - holds the names of regular enemies that can be encountered during the main quest
    * people.csv - contains the names and genders of people for the sidequest mechanic
    * potions.csv - holds all potion names, powers, types, and costs
    * provinces.txt - holds list of all Imperial provinces
    * rare_loot.csv - holds all rare loot names and their values
    * side_enemies.txt - hold names for all enemies that can be encountered in sidequests
    * weapons.csv - holds weapon names, powers, and costs
    * arena_enemies.txt [NEW] - holds the names of all enemies that can be encountered in the battle arena
    * outdoor_statements.csv [NEW] - contains the statements that will be printed when the player first goes outside
    * American Roulette.gif [NEW] - the layout for the American Roulette board
    * European Roulette.gif [NEW] - the layout for the European Roulette board

Changes from Project 1:
    * NEW: Game now keeps track of dates based on a fictional calendar.
    * NEW: Game now determines the weather for each day, including temperature and condition (based on the current season).
    * NEW: The player can now traverse his/her home city, allowing them to visit certain locations. Accordingly, the shops have been moved into this mechanic.
    * NEW: The player can now perform a power attack once per battle which deals 25% more damage.
    * NEW: Added a few mini-games: roulette, battle arena, and battle practice area.
    * NEW: Colored text now printed in certain situations.
    * NEW: On launch, the game now changes the terminal window size to 28 rows by 103 columns in terminals that support the changing of windows sizes using escape character sequences.
        * Source: "https://stackoverflow.com/questions/6418678/resize-the-terminal-with-python".
    * CHANGED: Save data is now written to and loaded from JSON files.
    * CHANGED: The game over exception now works correctly.
    * CHANGED: Made game easier/playable at higher levels.
    * CHANGED: When Ctrl-C is pressed, a message indicating that the player has left the game is now printed instead of a KeyboardInterrupt traceback.
    * CHANGED: Other minor fixes and enhancements.
