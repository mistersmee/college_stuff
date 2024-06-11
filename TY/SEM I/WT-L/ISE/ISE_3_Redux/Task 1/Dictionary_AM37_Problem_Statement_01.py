#capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}

# Define Empty Dictionary
capitals = {}

# Add above element to the Dictionary
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}

# Check type of Dictionary
print(type(capitals))

# Print all Element from Dictionary
print(capitals.items())

# Print only 1 and 3 element from Dictionary
print(capitals.get("Maharashtra"))
print(capitals.get("Telangana"))

# Add 2 More new states and thie capitals to the Dictionary
capitals["Uttar Pradesh"] = "Lucknow"
capitals["Madhya Pradesh"] = "Bhopal"

# Print all Element from Dictionary
print(capitals.items())

# Delete 4th element from the Dictionary
del capitals["Karnataka"]

# Print all Element from Dictionary
print(capitals.items())
