# Initialises key-value dictionary (hashmap), where we wil
# store the data.
marks = {}

# Adds key-value pairs to the dictionary.
marks["Alice"] = 95
marks["Bob"] = 80
marks["Charlie"] = 90

# Retrieves/deletes/checks the 'value' associated with the
# specified 'key'.
print(marks["Alice"])      # 95
del marks["Bob"]
print("Charlie" in marks)  # True
