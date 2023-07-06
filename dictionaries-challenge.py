#!/usr/bin/env python3


def main():

    marvelchars = {
    "Starlord":
      {"real name": "peter quill",
       "powers": "dance moves",
       "archenemy": "Thanos"},

    "Mystique":
      {"real name": "raven darkholme",
       "powers": "shape shifter",
       "archenemy": "Professor X"},

    "Hulk":
      {"real name": "bruce banner",
       "powers": "super strength",
       "archenemy": "adrenaline"}
                  }
    char_name = input(f"Which character do you want to know about? (Starlord, Mystique, Hulk)\n").lower().title()           
    while char_name not in marvelchars.keys():
        print(f"Character unknown!")
        char_name = input(f"Which character do you want to know about? (Starlord, Mystique, Hulk)\n").lower().title()
    
    char_stat = input(f"What statistic do you want to know about? (real name, powers, archenemy)\n").lower()
    while char_stat not in marvelchars.get(char_name, ''):
        print(f"Statistic unknown!")
        char_stat = input(f"What statistic do you want to know about? (real name, powers, archenemy)\n").lower()

    if(char_stat == "real name"):
        print(f"\n{char_name}'s {char_stat} is: {marvelchars.get(char_name, '').get(char_stat, '').title()}")
    else:
        print(f"\n{char_name}'s {char_stat} is: {marvelchars.get(char_name, '').get(char_stat, '')}")

main()
