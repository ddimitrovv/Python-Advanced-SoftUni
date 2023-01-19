# Create a function called age_assignment() that receives a different number of names
# and a different number of key-value pairs.
# The key will be a single letter (the first letter of each name) and the value - a number (age).
# Find it's first letter in the key-value pairs for each name and assign the age to the person's name.
# Then, sort the names in ascending order (alphabetically) and return the information for each person
# on a new line in the format: "{name} is {age} years old."
# Submit only the function in the judge system.

def age_assignment(*args, **kwargs):
    output = dict()
    for name in args:
        first_letter = name[0]
        output[name] = kwargs[first_letter]

    output = [f'{name} is {age} years old.' for name, age in sorted(output.items(), key=lambda x: x[0])]
    return '\n'.join(output)


# ---- TEST CODE----

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
