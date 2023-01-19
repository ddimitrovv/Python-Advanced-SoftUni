# Create a function called even_odd_filter() that can receive a different number of named arguments.
# The keys will be "even" and/or "odd", and the values will be a list of numbers.
# When the key is "odd", you should extract only the odd numbers from its list.
# When the key is "even", you should extract only the even numbers from its list.
# The function should return a dictionary sorted by the length of the lists in descending order.
# There will be no case of lists with the same length.
# Submit only your function in the judge system.

def even_odd_filter(**kwargs):
    new_dict = dict()
    for key, value in kwargs.items():
        check = 0 if key == 'even' else 1
        new_value = [x for x in value if x % 2 == check]
        new_dict[key] = new_value
    sorted_dict = dict(sorted(new_dict.items(), key=lambda x: len(x[1]), reverse=True))

    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
