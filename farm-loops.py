#!/usr/bin/env python3

def main():

    farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]
    
    while True:
        for x in farms:
            print(f"{x.get('name')}")
        choice = input(f"\nChoose a farm from the list above to see its animals: ")
        if choice.lower() == "southwest farm":
            veg = ["carrots", "celery"]
            for x in farms[0]["agriculture"]:
                print(f"{x}")
            break
        elif choice.lower() == "northeast farm":
            for x in farms[1]["agriculture"]:
                print(f"{x}")
            break
        elif choice.lower() == "west farm":
            for x in farms[3]["agriculture"]:
                print(f"{x}")
            break
        elif choice.lower() == "east farm":
            break
        else:
            print(f"\nFarm does not exist! Please input a valid farm")
            continue


if __name__ == "__main__":
    main()
