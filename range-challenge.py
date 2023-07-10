#!/usr/bin/env python3

def main():

    while True:
        bottles = int(input(f"\nHow many bottles of beer do you want to count down from? (max 100) "))
        if bottles > 100:
            print(f"\nPlease input a number between 1 and 100")
            continue
        else:
            break

    for count in range(bottles):
        print(f"{bottles} of bottles of beer on the wall!")
        print(f"{bottles} of bottles of beer on the wall! {bottles} bottles of beer! You take one down, pass it around!")        
        bottles -= 1

if __name__ == "__main__":
    main()
