print('''           ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   |
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-./uuu\.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""` ''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure✊🏻")

choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == 'left':
    choice2 = input("You're at a lake. There's an island at middle of the lake. Type 'swim' to swim across the lake, type 'wait' to wait until a boat arrives: ").lower()
    if choice2 == 'wait':
        choice3 = input("There are three doors over here viz. red,blue and yellow. Type the one that you wanna enter: ").lower()
        if choice3 == 'red':
            print("You're burned by fire🔥, Game over🫥")
        elif choice3 == 'blue':
            print("You've been eaten by beasts👺, Game over😱")
        elif choice3 == 'yellow':
            print("Congratulations🎉!! You've found the treasure⛳️")
        else:
            print("You lost😞")
    else:
        print("You've attacked by an angry trout🐟, You lost😢")
else:
    print("You've fallen into a hole🕳️.You're dead☠️, Game over☹️")


