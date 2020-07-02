# Testing for different components


# Testing for summary component
# - I was trying to figure out a way to make it so the formatting wouldn't screw with the column walls
# - I figured out the way to do this was to manually set the character length of the area before putting the string into it.
# - Once the string was put in it would take up a certain amount of charcters instead of just adding on
length = 15  # The character length that i wish to manually set


string = "hello" # String to be displayed
# Left aligned
print('{1:>{0}}'.format(length, string))
# Right Aligned
print('{1:^{0}}'.format(length, string))