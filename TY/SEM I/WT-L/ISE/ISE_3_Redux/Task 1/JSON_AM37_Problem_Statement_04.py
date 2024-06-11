import json

# Data to be given as input to JSON file
course_items = [{"course_name": "Python"}, {"course_name": "SQLAlchemy"}, {"course_name": "NodeJS"}]

# Convert Python list to JSON string
course_items_json = json.dumps(course_items)

# Save JSON string to file
with open('course.json', 'w') as outfile:
    json.dump(course_items, outfile)

# Read JSON data from file
with open('course.json', 'r') as infile:
    course_items_loaded = json.load(infile)

# Print JSON data
print(course_items_loaded)
