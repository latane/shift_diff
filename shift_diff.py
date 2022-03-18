#!/usr/bin/env python3
import os
import pickle
from locations import Location, Workday

def first_time_setup(c):
    loc_dict = {}
    for i in range(0, c):
        name = input("Location Name")
        loc_dict[name] = Location(name)
        #trusting stuff for now
        base = input('What is your base rate?\n')
        two = input("What is your second shift diff?\n")
        three = input("what is your third shift diff\n")
        WE = input("What is your weekend diff?\n")
        stack = False
        bool_resp = input("Press 'N' if your diff does not stack, any key for yes\n")
        if bool_resp.lower() != "n":
            stack = True
        loc_dict[name].set_rates(base, two, three, WE, stack)
    return loc_dict
    

if __name__ == "__main__":
    location_dict = {}
    day_list = []
    try:
        with open('saved_locations', 'rb') as f:
            location_dict = pickle.load(f)
    except EOFError:
        print("Error with Saved File")
        # debug delete
        os.remove('saved_locations')
    except FileNotFoundError:
        new_load = True
        with open('saved_locations', 'wb') as f:
            pass
        c = 0
        while c < 1:
            try:
                c = int(input("How many locations?\n"))
            except ValueError:
                print("Try using a number")
        location_dict = first_time_setup(c)

    for key, value in location_dict:
        print(key, value)