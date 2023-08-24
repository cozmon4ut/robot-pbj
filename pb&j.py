
available_ingredients = ["knife", "plate", "first_slice", "second_slice", 
                        "peanut_butter", "jelly"] # Defining what ingredients the robot has

finished_sandwich = [] # Where we will store our completed sandwich

sandwich_is_done = 0 # We need to tell the robot that the sandwich isn't done, so we initialize a variable to do so

while sandwich_is_done != 1: # While the variable sandwich_is_done is not equal to 1

    if "knife" in available_ingredients and "plate" in available_ingredients and "first_slice" not in finished_sandwich:
        # Check if we have the knife and plate, and whether or not the first slice is on the plate.
        finished_sandwich.append("first_slice")

        if "peanut_butter" in available_ingredients and "peanut_butter" not in finished_sandwich:
            # Is peanut butter on the first slice? If not, let's add it. 
            finished_sandwich.append("peanut_butter")

        if "jelly" in available_ingredients and "second_slice" in available_ingredients and "jelly" not in finished_sandwich:
            # Do we have both the second slice and jelly in our ingredients? If so, put the jelly on the second slice.

            finished_sandwich.append("jelly")
            finished_sandwich.append("second_slice")
        
        print(finished_sandwich) # Display that we've put the ingredients in the correct order
        print("\nThe sandwich is finished, my work here is done.")

        sandwich_is_done += 1 # Add one at the end to signify that the sandwich is done