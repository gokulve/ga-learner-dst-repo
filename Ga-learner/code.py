# --------------
# Create the lists 
class_1 =['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 =['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class = class_1 + class_2
# Append the list
new_class.append('Peter Warden')
# Print updated list
print (new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)


# Create the Dictionary

courses = {"Math":65,"English":70,"History":80,"French":70,"Science":60}

# Slice the dict and stores  the all subjects marks in variable
marks = [courses.get('Math'), courses.get('English'), courses.get('History'), courses.get('French'), courses.get('Science')]
#Total = courses.get('Math') + courses.get('English') + courses.get('History') + courses.get('French') + courses.get('Science')

# Store the all the subject in one variable `Total`
Total=sum(marks)
# Print the total
print("Total:",Total)
# Insert percentage formula
percentage = Total/500*100
# Print the percentage
print ("Percentage:", percentage)

# Create the Dictionary
mathematics ={"Geoffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,"Hilary Mason":70,"Corinna Cortes":66,
"Peter Warden":75}

# Given string
max_marks_scored = max(courses,key = courses.get)
print(max_marks_scored)
topper=max(mathematics,key = mathematics.get)
print("Tooper:",topper)
# Create variable first_name 
first_name=topper.split()[0]
# Create variable Last_name and store last two element in the list
last_name=topper.split()[1]
# Concatenate the string
certificate_name =last_name+" " +first_name
# print the full_name
print("Full name",certificate_name)
# print the name in upper case
certificate_name=certificate_name.upper()
print("certificate_name is'",certificate_name,"'")
# Code ends here


