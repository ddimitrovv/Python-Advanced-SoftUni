# Create a function named flights that receive a different number of arguments
# representing the information about the flights for a day:
#     • the destination of each flight
#     • the count of passengers that are boarding the plane
#     • a string "Finish"
# You need to take each argument and make a dictionary with the plane’s destination as a key
# and the passengers as a value of the corresponding key.
# If there are more than one flight to the same destination,
# you should count all the passengers that flew to the destination.
# You should modify the dictionary until the current argument is equal to "Finish".
# Note: Submit only the function in the judge system
# Input
#     • There will be no input, just parameters passed to your function
# Output
#     • The function should return the final dictionary
# Constrains
#     • All numbers will be valid integers in the range [0, 300]
#     • There will be no flight without given number of passengers
def flights(*args):
    destinations = [x for i, x in enumerate(args) if i % 2 == 0]
    passengers = [x for i, x in enumerate(args) if i % 2 != 0]

    flights_info = dict()
    for i in range(len(destinations)):
        if destinations[i] == 'Finish':
            break
        if destinations[i] not in flights_info:
            flights_info[destinations[i]] = 0
        flights_info[destinations[i]] += passengers[i]

    return flights_info


print(
    flights(
        'Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15
    )
)
print('-' * 30)
print(
    flights(
        'London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'
    )
)
print('-' * 30)
print(
    flights(
        'Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0
    )
)
