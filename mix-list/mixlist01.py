#!/usr/bin/env python3

import random

def main():
    
    #create my_list with 3 defined elements
    my_list = [ "192.168.0.5", 5060, "UP" ]

    #print index 0 of my_list
    print("The first item in the list (IP): " + my_list[0] )

    #print index 1 of my_list and convert the int to a string
    print("The second item in the list (port): " + str(my_list[1]) )

    #print index 2 of my_list
    print("The last item in the list (state): " + my_list[2] )

    #create iplist with 6 defined elements
    iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

    #print iplist IP addresses only
    print(f"IP Addresses: {iplist[3]} and {iplist[4]}")

    wordbank = ["indentation", "spaces"]

    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    #part 3 append int 4 to list wordbank
    wordbank.append(4)

    for i in wordbank:
        print(f"Part 3: {i}")

    #part 4 save input, a number between 1 and 21, as var num
    #part 5 convert var string num to int
    #bonus 2 tlgstudent length can change
    num = int(input(f"Enter a number between 1 and {len(tlgstudents)}: ")) - 1

    #part 5 cont'd slice element based on int num input
    student_name = tlgstudents[num]

    #part 6 print student_name and wordbank[2] <4> and wordbank[1] <spaces>
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    #bonus 1 randomize the student_name element picked
    print(f"{random.choice(tlgstudents)} always uses {wordbank[2]} {wordbank[1]} to indent.")

if __name__ == "__main__":
    main()
