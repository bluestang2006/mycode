#!/usr/bin/env python3

#create my_list with 3 defined elements
my_list = [ "192.168.0.5", 5060, "UP" ]

#print index 0 of my_list
print("The first item in the list (P): " + my_list[0] )

#print index 1 of my_list and convert the int to a string
print("The second item in the list (port): " + str(my_list[1]) )

#print index 2 of my_list
print("The last item in the list (state): " + my_list[2] )

#create iplist with 6 defined elements
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#print iplist IP addresses only
print(f"IP Addresses: {iplist[3]} and {iplist[4]}")
