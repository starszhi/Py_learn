my_name = 'Zed A.Show'
my_age = 35 #not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# print(f"Let's talk about {my_name}.")
print("Let's talk about {0}.".format(my_name))
print(f"He is {my_height} inches tall.")
print(f"He is {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teech are usually {my_teeth} depending on the coffee.")

#This line is tricky,try to get it exactly right
total = my_age + my_height + my_weight
print(f"If i add {my_age},{my_height},{my_weight} I get {total}.")
