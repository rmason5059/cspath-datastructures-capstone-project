from collections import namedtuple
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

import sys


Restaurant = namedtuple("Restaurant", ["rest_type", "name", "price", "rating", "address"])


def pretty_print(ll):
    current_node = ll.get_head_node()
    while current_node:
        rest_data = current_node.get_value()
        print("********************************")
        print("Name:      {}\n".format(rest_data.name))
        print("Rating:    {}/5\n".format(rest_data.rating))
        print("Price:     {}/5\n".format(rest_data.price))
        print("Address:   {}\n".format(rest_data.address))
        current_node = current_node.get_next_node()


def handle_user_input(letter_to_type_hashmap):
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n").lower())
    # Check to see if the first letter of the input is in our hash map
    result = letter_to_type_hashmap.retrieve(user_input[0]).get_head_node()
    if result.get_value():
        # Since we found an entry in our hash map that corresponds to our input, traverse the hash map
        current_node = result
        # initialize a choices list
        current_food_options = ""
        count = 0
        # While the current node exists...
        while current_node:
            # If we find the user's input in the current node, increment count
            if current_node.get_value().startswith(user_input):
                current_food_options += "{} ".format(current_node.get_value())
                count += 1
                current_best_match = current_node.get_value()
                current_node = current_node.get_next_node()

            else:
                # Didn't find a match, move on to the next entry
                current_node = current_node.get_next_node()

        if count > 1:
            print("You have {0} choices, narrow down your search by adding more letters to your choice:\n".format(count))
            print("Your choices are: {0}\n".format(current_food_options))
            # We have too many choices, let's try again
            restaurant = handle_user_input(letter_to_type_hashmap)

        else:
            # Current best match will be your restaurant
            restaurant = current_best_match
            print("You have narrowed your search down to {0}".format(restaurant.title()))
            answer = input("Would you like to view {0} restaurants? [y/n]\n".format(restaurant.title()))
            if answer.lower() == 'y':
                return restaurant
            else:
                restaurant = handle_user_input(letter_to_type_hashmap)

        return restaurant
    else:
        sys.exit("Nothing found for your search criteria: {0}".format(user_input))

#Printing the Welcome Message
print_welcome()

# Let's create a set of types
restaurant_types = {i[0] for i in restaurant_data}
array_size_types = len(restaurant_types)
type_to_data_hashmap = HashMap(array_size_types)

# Ok, now create a set of first letters for our hash map
first_letters = {i[0] for i in types}
array_size_letters = len(first_letters)
letter_to_type_hashmap = HashMap(array_size_letters)

#Write code to insert food types into a data structure here. The data is in data.py

for i in first_letters:
    ll = LinkedList()
    for j in types:
        if j.startswith(i) and ll.head_node.get_value():
            ll.insert_beginning(j)
        elif j.startswith(i) and not ll.head_node.get_value():
            ll = LinkedList(j)

    letter_to_type_hashmap.assign(i, ll)

#Write code to insert restaurant data into a data structure here. The data is in data.py

for i in types:
    ll = LinkedList()
    for j in restaurant_data:
        if j[0] == i and ll.head_node.get_value():
            nt = Restaurant(j[0], j[1], j[2], j[3], j[4])
            ll.insert_beginning(nt)
        elif j[0] == i and not ll.head_node.get_value():
            nt = Restaurant(j[0], j[1], j[2], j[3], j[4])
            ll = LinkedList(nt)
    type_to_data_hashmap.assign(i, ll)

#Write code for user interaction here
while True:
    #Search for user_input in food types data structure here

    restaurant = handle_user_input(letter_to_type_hashmap)
    print("You chose {0}".format(restaurant.title()))

    choice = type_to_data_hashmap.retrieve(restaurant)

    pretty_print(choice)

    answer = input("Continue searching for more restaurants? [y/n]\n")
    if answer.lower() == 'y':
        continue
    elif answer.lower() == 'n':
        print("See ya!")
        sys.exit()
    else:
        print("{0} is not a valid choice".format(answer))
        continue

