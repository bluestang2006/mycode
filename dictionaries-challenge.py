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
    
    while True:
        char_name = input(f"Which character do you want to know about? (Starlord, Mystique, Hulk)\n").lower().title()
        if not marvelchars.get(char_name):
            print(f"Character unknown!")
            continue
        else:
            break

    while True:
        char_stat = input(f"What statistic do you want to know about? (real name, powers, archenemy)\n").lower()
        if not marvelchars.get(char_name).get(char_stat):
            print(f"Statistic unknown!")
            continue
        else:
            break

    if(char_stat == "real name"):
        print(f"\n{char_name}'s {char_stat} is: {marvelchars.get(char_name, '').get(char_stat, '').title()}")
    else:
        print(f"\n{char_name}'s {char_stat} is: {marvelchars.get(char_name, '').get(char_stat, '')}")

main()
